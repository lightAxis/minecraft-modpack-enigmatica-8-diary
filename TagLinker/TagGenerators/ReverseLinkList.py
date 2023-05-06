#!/usr/bin/env python3

from ..EnumStructs import *
from ..Extractors_t import *
from ..LinkExtractors.LinkExtractor import LinkExtractor
from ..NameDescExtractors.NameDescExtractor import NameDescExtractor
from .TagGenerator import TagGenerator

import os
from typing import List, Dict, Optional
from abc import *
import copy
import operator


class ReverseLinkListTagGenerator(TagGenerator):
    def getGeneratorType(self) -> str:
        return "reverse_link_list"

    def _insert_table_header(self, lines: List[str], tagInfo: tag_desc_t):

        if (tagInfo.ArgDict.get("table_align") != None):
            lines.insert(0, tagInfo.ArgDict["table_align"]+"\n")
        else:
            lines.insert(0, "|---|---|\n")

        if (tagInfo.ArgDict.get("table_header") != None):
            lines.insert(0, tagInfo.ArgDict["table_header"]+"\n")
        else:
            lines.insert(0, "|이름|내용|\n")

    def _gen_desc_str(self, tagInfo: tag_desc_t, tagSource: tag_source_t, extractors: Extractors_t) -> str:
        desc_type: str = tagInfo.ArgDict.get("desc_type")

        temp_lines: List[str] = []
        merge_line: str = ""
        if (desc_type == None or desc_type == "target"):
            temp_lines = tagSource.TargetDesc
        elif desc_type == "source":
            temp_lines = tagSource.SourceDesc
        else:
            raise Exception(
                "ReverseLink tag generator's arg:desct_type is only allows [target, source]")

        for line in temp_lines:
            merge_line = merge_line + line
        return merge_line

    def _gen_table_item_str(self, tagInfo: tag_desc_t, tagSource: tag_source_t, extractors: Extractors_t):
        dir = os.path.dirname(tagInfo.FilePath)

        linkpair: link_pair_t = link_pair_t()
        linkpair.Name = tagSource.SourceName
        linkpair.LinkPath = os.path.relpath(tagSource.SourcePath, dir)
        line1: str = extractors.Link.GenerateLinkPairStr(linkpair)
        line2: str = self._gen_desc_str(tagInfo, tagSource, extractors)
        line2 = line2.replace("\n", "")
        return "|"+line1+"|"+line2+"|\n"
        pass

    def _gen_desc_item_strs(self, tagInfo: tag_desc_t, tagSource: tag_source_t, extractors: Extractors_t) -> List[str]:
        dir: str = os.path.dirname(tagInfo.FilePath)

        linkpair: link_pair_t = link_pair_t()
        linkpair.Name = tagSource.SourceName
        linkpair.LinkPath = os.path.relpath(tagSource.SourcePath, dir)
        line1: str = "- " + \
            extractors.Link.GenerateLinkPairStr(linkpair) + "  \n"
        line2: str = self._gen_desc_str(tagInfo, tagSource, extractors)

        temp_lines: List[str] = []
        temp_lines.append(line1)
        temp_lines.append(line2)
        return temp_lines

    def Generate_Content(self, tagInfo: tag_desc_t, tagsources: List[tag_source_t], extractors: Extractors_t) -> List[str]:
        new_lines: List[str] = []

        dir = os.path.dirname(tagInfo.FilePath)

        sortedTagSources = sorted(
            tagsources, key=operator.attrgetter('SourceName'))

        arg_preset_type: str = tagInfo.ArgDict.get("preset")
        if (arg_preset_type == "member_contribute"):
            tagInfo.ArgDict["header"] = "### 참여 목록"
            tagInfo.ArgDict["list_type"] = "table"
            tagInfo.ArgDict["table_header"] = "|문서|기여 내용|"
            tagInfo.ArgDict["desc_type"] = "target"
        elif (arg_preset_type == "systems_inside"):
            tagInfo.ArgDict["header"] = "### 보유 시설 목록"
            tagInfo.ArgDict["list_type"] = "table"
            tagInfo.ArgDict["table_header"] = "|시설|세부 사항|"
            tagInfo.ArgDict["desc_type"] = "target"
        elif (arg_preset_type == "spots_inside"):
            tagInfo.ArgDict["header"] = "### 하위 장소 목록"
            tagInfo.ArgDict["list_type"] = "table"
            tagInfo.ArgDict["table_header"] = "|시설|세부 사항|"
            tagInfo.ArgDict["desc_type"] = "source"
        elif (arg_preset_type == None):
            pass
        else:
            raise Exception(
                "ReverseLink TagGenerator, tag:preset must allow [member_contribute]")

        arg_header_name: str = tagInfo.ArgDict.get("header")

        arg_list_type: str = tagInfo.ArgDict.get("list_type")
        if (arg_list_type == None or arg_list_type == "table"):
            arg_list_type = "table"
        elif (arg_list_type == "list"):
            arg_list_type == "list"
        else:
            raise Exception(
                "ReverseLinkList TAg Generator arg: list_type must have value [list, table]")

        for tagSource in sortedTagSources:
            if (tagInfo.FileName != tagSource.TargetName):
                continue

            if (arg_list_type == "list"):
                new_lines.extend(self._gen_desc_item_strs(
                    tagInfo, tagSource, extractors))
                continue

            if (arg_list_type == "table"):
                new_lines.append(self._gen_table_item_str(
                    tagInfo, tagSource, extractors))
                continue

        if (arg_list_type == "table" and
                len(new_lines) >= 1):
            self._insert_table_header(new_lines, tagInfo)
            if (arg_header_name != None):
                new_lines.insert(0, arg_header_name+"\n")

        return new_lines
