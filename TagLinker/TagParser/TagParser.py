#!/usr/bin/env python3

from ..EnumStructs import *

import os
from typing import List, Dict, Optional
from abc import *
import copy


class TagParser(metaclass=ABCMeta):

    @abstractclassmethod
    def ParseDescs_inContent(self, content: List[str]) -> List[tag_source_t]:
        pass

    @abstractclassmethod
    def getParserType(self) -> str:
        pass
