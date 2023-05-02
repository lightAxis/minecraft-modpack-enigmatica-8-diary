#!/usr/bin/env python3

from ..EnumStructs import *
from ..Extractors_t import *
from ..LinkExtractors.LinkExtractor import LinkExtractor
from ..NameDescExtractors.NameDescExtractor import NameDescExtractor

import os
from typing import List, Dict, Optional
from abc import *
import copy


class TagGenerator(metaclass=ABCMeta):
    @abstractclassmethod
    def getGeneratorType(self) -> str:
        pass

    @abstractclassmethod
    def Generate_Content(self, tagInfo: tag_desc_t, tagsources: List[tag_source_t], extractors: Extractors_t) -> List[str]:
        pass

    def Generate_inLines(self, lines: List[str], tagInfo: tag_desc_t, tagsources: List[tag_source_t], extractors: Extractors_t) -> List[str]:
        new_lines: List[str] = []

        startTagGen: bool = False
        for line in lines:

            # is tag started?
            if (line == tagInfo.TagStr):
                startTagGen = True
                new_lines.append(line)
                continue

            # not tag generating, always append to lines
            if (not startTagGen):
                new_lines.append(line)
                continue

            # if line has tag info
            tag_desc = extractors.Tag.extractFromLine(line)
            if (tag_desc != None):
                if (tag_desc.Type == TagType.CLOSE):
                    # if close tag, append content line, and add close tag line
                    startTagGen = False
                    new_content_lines = self.Generate_Content(
                        tagInfo, tagsources, extractors)
                    for new_content_line in new_content_lines:
                        new_lines.append(new_content_line)
                    new_lines.append(line)
                    continue
                elif (tag_desc.Type == TagType.ARGUMENT):
                    # if argument tag, append to lines
                    new_lines.append(line)

            # if line has no tag info, ignore this line
            if (tag_desc == None):
                continue

        return new_lines

    def Generate_inTagInfo(self, tagInfo: tag_desc_t, tagsources: List[tag_source_t], extractors: Extractors_t) -> List[tag_source_t]:
        f = open(tagInfo.FilePath, "r")
        lines = f.readlines()
        f.close()

        lines = self.Generate_inLines(
            lines, tagInfo, tagsources, extractors)

        f = open(tagInfo.FilePath, "w")
        for line in lines:
            f.write()
        f.close()

        pass
