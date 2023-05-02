#!/usr/bin/env python3

from ..EnumStructs import *
from .TagParser import TagParser
from ..LinkExtractors.LinkExtractor import LinkExtractor
from ..NameDescExtractors.NameDescExtractor import NameDescExtractor
from ..Extractors_t import *

import os
from typing import List, Dict, Optional
from abc import *
import copy


class DescriptionTagParser(TagParser):
    def getParserType(self) -> str:
        return "description"

    def ParseDescs_inContent(self, tagInfo: tag_desc_t, extractors: Extractors_t) -> List[tag_source_t]:
        return_tag_sources: List[tag_source_t] = []

        temp_tag_source_t: tag_source_t = None

        is_extracting_linkDesc: bool = False
        for line in tagInfo.Content:

            # extract link contents from line
            extractedLinkContent = extractors.Link.ExtractFromLine(line)

            # check if link_pair_t exists
            temp_link_pair_t: link_pair_t = None
            for linkContent in extractedLinkContent:
                if (type(linkContent) != str):
                    temp_link_pair_t = linkContent
                    break

            if (temp_link_pair_t != None):
                is_extracting_linkDesc = True
                temp_tag_source_t = tag_source_t()
                temp_tag_source_t.Content = tagInfo.Content
                temp_tag_source_t.SourceName = tagInfo.FileName
                temp_tag_source_t.SourceDesc = tagInfo.FileDesc
                temp_tag_source_t.SourcePath = tagInfo.FilePath
                temp_tag_source_t.TargetName = temp_link_pair_t.Name
                TargetFileDir: str = os.path.dirname(
                    temp_tag_source_t.SourcePath)
                temp_tag_source_t.TargetPath = os.path.join(
                    TargetFileDir, temp_link_pair_t.LinkPath)
                return_tag_sources.append(temp_tag_source_t)
                continue

            if (is_extracting_linkDesc):
                temp_tag_source_t.TargetDesc.append(line)
                continue

        return return_tag_sources
