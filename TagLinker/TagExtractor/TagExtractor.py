#!/usr/bin/env python3

from ..EnumStructs import *

import os
from typing import List, Dict, Tuple, Optional
from abc import *
import copy

# tag_<source/target>_open:[tagStyle]:[tagName]
# tag_close
# whitespace & \n is not allowed


class TagExtractor(metaclass=ABCMeta):
    @abstractmethod
    def _extractInfoFromLine(self, line: str) -> Optional[tag_desc_t]:
        pass

    @abstractclassmethod
    def _extractNameDescFromLines(self, lines: List[str]) -> Tuple[bool, str, str]:
        pass

    def extractTagInfosFromFile(self, filepath: str) -> List[tag_desc_t]:
        temp_tag_descs: List[tag_desc_t] = []

        f = open(filepath, 'r')
        lines = f.readlines()
        f.close()

        extracting_content: bool = False
        curr_tag_desc: tag_desc_t = None
        line_num: int = 0
        lastTagLine_num: int = 0
        for line in lines:
            line_num = line_num + 1

            tag_desc = self._extractInfoFromLine(line)

            # cut lines outside of tag area
            if (not extracting_content and tag_desc == None):
                continue

            # is extracting content, and line is pure, append to content lines
            if (extracting_content and tag_desc == None):
                curr_tag_desc.Content.append(line)
                continue

            # detecting open tag
            if tag_desc.Type == TagType.OPEN:
                if (extracting_content):
                    raise Exception("at file : " + filepath +
                                    "\nat line #" + str(line_num)+" : " + line +
                                    "\nopening tag twice before close previous tag")
                extracting_content = True
                curr_tag_desc = copy.deepcopy(tag_desc)
                lastTagLine_num = line_num
                continue

            # detecting close tag
            if tag_desc.Type == TagType.CLOSE:
                if (not extracting_content):
                    raise Exception("at file : " + filepath +
                                    "\nat line #" + str(line_num)+" : " + line +
                                    "\nclosing tag twice before open new tag")
                extracting_content = False
                curr_tag_desc.FilePath = filepath
                temp_tag_descs.append(curr_tag_desc)
                lastTagLine_num = line_num
                curr_tag_desc = None
                continue

        if (curr_tag_desc != None):
            raise Exception("at file : " + filepath +
                            "\nat line #" +
                            str(lastTagLine_num) + " : TagName : " +
                            curr_tag_desc.TagName +
                            "\nnot closing the opened tag")

        return temp_tag_descs
