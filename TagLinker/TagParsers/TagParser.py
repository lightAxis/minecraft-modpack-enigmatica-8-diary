#!/usr/bin/env python3

from ..EnumStructs import *
from ..LinkExtractors.LinkExtractor import LinkExtractor
from ..NameDescExtractors.NameDescExtractor import NameDescExtractor
from ..Extractors_t import *

import os
from typing import List, Dict, Optional
from abc import *
import copy


class TagParser(metaclass=ABCMeta):

    @abstractclassmethod
    def ParseDescs_inContent(self, tagInfo: tag_desc_t, extractors: Extractors_t) -> List[tag_source_t]:
        pass

    @abstractclassmethod
    def getParserType(self) -> str:
        pass
