#!/usr/bin/env python3

from enum import IntEnum
from dataclasses import dataclass, field
from typing import List, Dict
import os
import sys
import argparse

@dataclass
class desc_t:
    Name: str = ""
    RelPath: str = ""
    Desc: str = ""

def __make_embed_line_by_desc(desc:desc_t):
    line1 = "- ["+desc.Name+"]("+desc.RelPath+")  \n"
    line2 = desc.Desc
    return line1, line2


def __embed_name_desc(mainPath:str, descs:List[desc_t]):
    f = open(mainPath, 'r')
    lines = f.readlines()
    f.close()

    new_lines: List[str] = []
    writing_desc:bool= False

    for line in lines:
        line_no_space = line.replace(" ", "")
        if(line_no_space.find("<!--systems_list_dest_open-->") >=0):
            print("start embedding systems list..")
            writing_desc = True
            new_lines.append(line)
            for desc in descs:
                line1, line2 = __make_embed_line_by_desc(desc)
                new_lines.append(line1)
                new_lines.append(line2)
                print("Name: " + desc.Name)
            continue

        if(line_no_space.find("<!--systems_list_dest_close-->") >=0):
            print("close embedding systems list...")
            writing_desc = False
            new_lines.append(line)
            continue

        if(writing_desc):
            continue
            
        new_lines.append(line)

    f = open(mainPath, 'w')
    f.writelines(new_lines)
    f.close()

def __parse_name_desc(mdPath:str, mainPath:str):
    desc_temp : desc_t = desc_t()

    f = open(mdPath, 'r')
    lines = f.readlines()
    f.close()

    find_name:bool =  False
    for line in lines:
        NameIndex = line.find("# ")

        if(NameIndex >=0):
            find_name = True
            line = line.replace("\n", "")
            desc_temp.Name = line[NameIndex+1:]
            continue   
        
        line_no_space = line.replace(" ","")
        line_no_space = line_no_space.replace("\n", "")
        if(line_no_space == "" and find_name):
            continue

        if(find_name):
            desc_temp.Desc = line
            desc_temp.RelPath = os.path.relpath(mdPath, mainPath)
            break
    
    return desc_temp


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


def generate_system_list(systemMdPath:str, systemMdsPath:str):
    filePaths:List[str] = []
    __recursive_find_files(systemMdsPath, filePaths)

    descs:List[desc_t] = []
    for filePath in filePaths:
        if filePath == systemMdPath:
            continue
        descs.append(__parse_name_desc(filePath, systemMdPath))
    

    descs.sort(key = lambda x:x.Name)
    __embed_name_desc(systemMdPath, descs)
    





if __name__ == "__main__":
    print("generating systems list..")
    generate_system_list("docs/Ko/systems/systems.md", "docs/Ko/systems")
    print("Done!")
else:
    raise NameError("Strange start point")
