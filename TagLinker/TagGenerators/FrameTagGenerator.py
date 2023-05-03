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


class FrameTagGenerator(TagGenerator):
    def getGeneratorType(self) -> str:
        return "frame"

    def Generate_Content(self, tagInfo: tag_desc_t, tagsources: List[tag_source_t], extractors: Extractors_t) -> List[str]:
        new_lines: List[str] = []

        dir = os.path.dirname(tagInfo.FilePath)
        for tagsource in tagsources:
            for line in tagsource.Content:
                extractors.Link.ExtractFromLine(line)
                linkpairs = extractors.Link.getLineContents()
                for linkpair in linkpairs:
                    if (type(linkpair) == str):
                        continue

                    dir_of_source = os.path.dirname(tagsource.SourcePath)
                    path_from_origin = os.path.join(
                        dir_of_source, linkpair.LinkPath)
                    dir_of_target = os.path.dirname(tagInfo.FilePath)
                    linkpair.LinkPath = os.path.relpath(
                        path_from_origin, dir_of_target)
                new_lines.append(extractors.Link.GenerateLineStr())

        return new_lines
