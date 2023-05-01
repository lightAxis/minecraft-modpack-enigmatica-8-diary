#!/usr/bin/env python3

from ..EnumStructs import *
from .TagParser import TagParser

import os
from typing import List, Dict, Optional
from abc import *
import copy


class DescriptionTagParser(TagParser):
    def getParserType(self) -> str:
        return "description"

    def ParseDescs_inContent(self, content: List[str]) -> List[tag_source_t]:
        return_tag_sources: List[tag_source_t] = []

        temp_tag_source_t: tag_source_t = None

        is_extracting_linkDesc: bool = False
        for line in content:
            line_nameOpen = line.find("[")
            line_nameClose = line.find("](")
            line_linkClose = line.find(")")

            if (line_nameOpen > -1 and line_nameClose > -1 and line_linkClose > -1):
                is_extracting_linkDesc = True
                temp_tag_source_t = tag_source_t()
                temp_tag_source_t.Content = content
                temp_tag_source_t.
                continue

        return return_tag_sources
