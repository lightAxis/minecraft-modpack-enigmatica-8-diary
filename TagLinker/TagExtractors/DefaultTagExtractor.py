#!/usr/bin/env python3


from ..EnumStructs import *
from .TagExtractor import TagExtractor

import os
from typing import List, Dict, Optional
from abc import *
import copy

# tag_<source/target>_open:[tagStyle]:[tagName]
# tag_close
# whitespace & \n is not allowed


class DefaultTagExtractor(TagExtractor):

    def extractFromLine(self, line: str) -> Optional[tag_desc_t]:
        comment_in: int = line.find("<!--") > -1
        comment_out: int = line.find("-->") > -1
        if ((not comment_in) or (not comment_out)):
            return None

        comment_tag_source_open: bool = line.find("tag_source_open:") > -1
        comment_tag_target_open: bool = line.find("tag_target_open:") > -1

        adjusted_line = line.replace(" ", "")
        adjusted_line = adjusted_line.replace("<!--", "")
        adjusted_line = adjusted_line.replace("-->", "")
        adjusted_line = adjusted_line.replace("\n", "")
        split = adjusted_line.split(':')

        if (comment_tag_source_open):
            if (len(split) != 3):
                raise Exception(
                    "at line: " + line + " /tag source opened, strange number of ':', must be tag_source_open:tagStyle:tagName")

            temp_tag_desc_t: tag_desc_t = tag_desc_t()
            temp_tag_desc_t.Type = TagType.OPEN
            temp_tag_desc_t.Direction = TagDirection.SOURCE
            temp_tag_desc_t.TagStyle = split[1]
            temp_tag_desc_t.TagName = split[2]
            temp_tag_desc_t.TagStr = line
            return temp_tag_desc_t

        if (comment_tag_target_open):

            if (len(split) != 3):
                raise Exception(
                    "at line: " + line + " /tag target opened, strange number of ':', must be tag_target_open:tagStyle:tagName")
            temp_tag_desc_t: tag_desc_t = tag_desc_t()
            temp_tag_desc_t.Type = TagType.OPEN
            temp_tag_desc_t.Direction = TagDirection.TARGET
            temp_tag_desc_t.TagStyle = split[1]
            temp_tag_desc_t.TagName = split[2]
            temp_tag_desc_t.TagStr = line
            return temp_tag_desc_t

        comment_tag_close: bool = line.find("tag_close") > -1
        if (comment_tag_close):
            if (len(split) != 1):
                raise Exception(
                    "at line: " + line + "/tag closed, strange number of ':', must be tag_close")
            temp_tag_desc_t: tag_desc_t = tag_desc_t()
            temp_tag_desc_t.Type = TagType.CLOSE
            temp_tag_desc_t.TagStr = line
            return temp_tag_desc_t

        comment_tag_arg: bool = line.find("tag_arg:") > -1
        if (comment_tag_arg):
            if (len(split) != 3):
                raise Exception("at line : " + line +
                                "/tag arg, strange number of ':', must be tag_arg:argKey:argValue")
            temp_tag_desc_t: tag_desc_t = tag_desc_t()
            temp_tag_desc_t.Type = TagType.ARGUMENT
            temp_tag_desc_t.TagStyle = split[1]
            temp_tag_desc_t.TagName = split[2]
            temp_tag_desc_t.TagStr = line
            return temp_tag_desc_t

        return None
