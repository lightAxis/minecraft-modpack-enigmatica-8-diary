#!/usr/bin/env python3

from ..EnumStructs import *

import os
from typing import List, Dict, Tuple, Optional
from abc import *
import copy

# # Name
# Desc


class NameDescExtractor(metaclass=ABCMeta):
    @abstractclassmethod
    def extractFromFileLines(self, lines: List[str]) -> Tuple[bool, str, str]:
        pass

    @abstractclassmethod
    def extractFromFilePath(self, filepath: str) -> Tuple[bool, str, str]:
        pass
