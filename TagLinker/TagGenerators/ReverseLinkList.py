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

    def Generate_Content(self, tagInfo: tag_desc_t, tagsources: List[tag_source_t], extractors: Extractors_t) -> List[str]:
        new_lines: List[str] = []

        dir = os.path.dirname(tagInfo.FilePath)

        sortedTagSources = sorted(
            tagsources, key=operator.attrgetter('SourceName'))

        for tagSource in sortedTagSources:
            if (tagInfo.FileName != tagSource.TargetName):
                continue

            linkpair: link_pair_t = link_pair_t()
            linkpair.Name = tagSource.SourceName
            linkpair.LinkPath = os.path.relpath(tagSource.SourcePath, dir)
            line1 = extractors.Link.GenerateLinkPairStr(linkpair)
            line2 = tagSource.TargetDesc[0][0:-1]
            new_lines.append("|"+line1+"|"+line2+"|\n")

        if (len(new_lines) >= 1):
            new_lines.insert(0, "|--|--|\n")
            new_lines.insert(0, "|항목|내용|\n")

        return new_lines
