#!/usr/bin/env python3

from enum import IntEnum
from dataclasses import dataclass, field
from typing import List, Dict
import os
import sys
import argparse


@dataclass 
class desc_t:
    Name:str = ""
    RelPath:str = ""
    NickName:str = ""
    Desc:str = ""

def __make_strs_for_desc_t(desc:desc_t):
    line1:str = ""
    line2:str = ""
    line1 = "- [" + desc.Name +"](" + desc.RelPath + ")  \n"
    line2 = desc.Desc
    return line1, line2

def __change_player_desc_lines(memberName:str, lines:List[str], descs:List[desc_t]):
    descs_temp:List[desc_t] = []
    lines_temp:List[str] = []

    for desc in descs:
        if(desc.NickName == memberName):
            descs_temp.append(desc)

    wait_for_desc_dest_close:bool = False

    for line in lines:
        line_removeSpace = line.replace(" ","")
        if(line_removeSpace.find("<!--player_desc_dest_open-->") >=0):
            # print("player desc dest opened")
            lines_temp.append(line)

            for desc in descs_temp:
                print("adding: "+desc.Name)
                line1, line2 = __make_strs_for_desc_t(desc)
                lines_temp.append(line1)
                lines_temp.append(line2)

            wait_for_desc_dest_close = True
            continue
        
        if(line_removeSpace.find("<!--player_desc_dest_close-->") >=0):
            # print("player desc dest closed")
            wait_for_desc_dest_close = False
            lines_temp.append(line)
            continue
        
        if(wait_for_desc_dest_close):
            continue

        lines_temp.append(line)

    return lines_temp


def __change_player_desc(memberRootPath:str, descs:List[desc_t]):
    memberList = os.listdir(memberRootPath)

    for member in memberList:
        memberPath = os.path.join(memberRootPath, member)
        memberName = os.path.splitext(member)[0]

        if os.path.isdir(memberPath):
            continue

        print(memberPath)
        f = open(memberPath,'r')
        lines = f.readlines()
        f.close()

        new_lines = __change_player_desc_lines(memberName, lines, descs)

        f = open(memberPath, 'w')
        f.writelines(new_lines)
        f.close()


def __extract_player_descs(path:str , memberRootPath:str, descs:List[desc_t]):
    Lines:List[str] = open(path,'r').readlines()

    nameGet:bool = False
    now_playerDesc:bool = False
    now_playerDescName:bool = False

    name_of_this_md:str = ""
    tempDesc_t: desc_t = desc_t()

    for line in Lines:
        nameStart = line.find("# ")
        if(nameStart >= 0 and nameGet == False):
            line = line.replace("\n","")
            line = line.replace("# ", "")
            name_of_this_md = line
            nameGet = True
            continue

        parseline = line.replace(" ", "")
        if(parseline.find("<!--player_desc_open-->") >= 0):
            now_playerDesc = True
            continue
        if(parseline.find("<!--player_desc_close-->") >= 0):
            now_playerDesc = False
            now_playerDescName = False
            continue

        

        nickStart = parseline.find('[')
        nickEnd = parseline.find(']')
        if(nickStart >= 0 and nickEnd >= 0 and now_playerDesc):
            tempDesc_t = desc_t()
            tempDesc_t.Name = name_of_this_md
            tempDesc_t.NickName = parseline[nickStart+1:nickEnd]
            tempDesc_t.RelPath = os.path.relpath(path, memberRootPath)
            now_playerDescName = True
            descs.append(tempDesc_t)
            continue

        if(now_playerDesc and now_playerDescName):
            tempDesc_t.Desc = tempDesc_t.Desc + line
            continue


    

def __recursive_find_files(dir:str, files:List[str]):
    if not os.path.exists(dir):
        raise NameError("no path is available for recursive find files")
    
    now_list:List[str]  = os.listdir(dir)

    for path in now_list:
        path = os.path.join(dir, path)
        if os.path.isfile(path) and (os.path.splitext(path)[1] == ".md"):
            files.append(path)
        elif os.path.isdir(path) :
            __recursive_find_files(path, files)
    
    return now_list


def generate_profiles(membersRootPath: str,recursive_rootdir: str):
    allFiles: List[desc_t] = []

    print("finding all files recursively..")
    __recursive_find_files(recursive_rootdir, allFiles)

    desc_ts:List[desc_t]  = []
    print("extracing description infos from tag..")
    for filepath in allFiles:
        __extract_player_descs(filepath,membersRootPath, desc_ts)

    print("generating new player description .md files...")
    __change_player_desc(membersRootPath, desc_ts)



if __name__ == "__main__":
    print("generating each member's participated items list..")
    generate_profiles("docs/Ko/members", "docs/Ko")
    print("Done!")
else:
    raise NameError("Strange start point")
