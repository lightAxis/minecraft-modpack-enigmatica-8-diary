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


class LinkListTagGenerator(TagGenerator):
    def getGeneratorType(self) -> str:
        return "link_list"

    def Generate_Content(self, tagInfo: tag_desc_t, tagsources: List[tag_source_t], extractors: Extractors_t) -> List[str]:
        new_lines: List[str] = []

        if (tagInfo.ArgDict.get("file_dir") == None):
            raise Exception(
                "link_list target target must have tag_arg:file_dir")
