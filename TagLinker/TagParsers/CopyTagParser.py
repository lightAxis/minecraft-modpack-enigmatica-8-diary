#!/usr/bin/env python3

from ..EnumStructs import *
from .TagParser import TagParser
from ..LinkExtractors.LinkExtractor import LinkExtractor
from ..NameDescExtractors.NameDescExtractor import NameDescExtractor
from ..Extractors_t import Extractors_t

import os
from typing import List, Dict, Optional
from abc import *
import copy


class CopyTagParser(TagParser):
    def getParserType(self) -> str:
        return "copy"

    def ParseDescs_inContent(self, tagInfo: tag_desc_t, extractors: Extractors_t) -> List[tag_source_t]:
        return_tag_sources: List[tag_source_t] = []

        temp_tag_source_t: tag_source_t = tag_source_t()

        temp_tag_source_t.Content = tagInfo.Content
        temp_tag_source_t.SourceName = tagInfo.FileName
        temp_tag_source_t.SourceDesc = tagInfo.FileDesc
        temp_tag_source_t.SourcePath = tagInfo.FilePath

        return_tag_sources.append(temp_tag_source_t)
        return return_tag_sources
