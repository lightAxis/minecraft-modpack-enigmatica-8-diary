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


class ContributionListTagGenerator(TagGenerator):
    def getGeneratorType(self) -> str:
        return "contribution_list"

    def Generate_Content(self, tagInfo: tag_desc_t, tagsources: List[tag_source_t], extractors: Extractors_t) -> List[str]:
        new_lines: List[str] = []

        dir = os.path.dirname(tagInfo.FilePath)

        sortedTagSources = sorted(
            tagsources, key=operator.attrgetter('SourceName'))
        for tagSource in sortedTagSources:
            if (tagInfo.FileName != tagSource.TargetName):
                continue
            # reverse link to tagSource
            line1 = "- [" + tagSource.SourceName + \
                "](" + os.path.relpath(tagSource.SourcePath, dir)+")  \n"
            # description is same
            lines2 = tagSource.TargetDesc
            new_lines.append(line1)
            new_lines.extend(lines2)

        return new_lines
