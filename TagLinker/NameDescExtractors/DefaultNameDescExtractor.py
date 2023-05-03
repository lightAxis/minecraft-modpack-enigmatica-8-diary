#!/usr/bin/env python3

from ..EnumStructs import *

import os
from typing import List, Dict, Tuple, Optional
from abc import *
import copy

from .NameDescExtractor import NameDescExtractor


class DefaultNameDescExtractor(NameDescExtractor):
    def extractFromFileLines(self, lines: List[str]) -> Tuple[bool, str, str]:
        find_name: bool = False
        resultDesc: str = ""
        resultName: str = ""
        for line in lines:
            NameIndex = line.find("# ")

            if (NameIndex >= 0):
                find_name = True
                line = line.replace("\n", "")
                resultName = line[NameIndex+2:]
                continue

            line_no_space = line.replace(" ", "")
            line_no_space = line_no_space.replace("\n", "")
            if (line_no_space == "" and find_name):
                continue

            if (find_name):
                resultDesc = line
                break

        isOK: bool = False
        if (resultDesc != None and resultName != None):
            isOK = True

        return isOK, resultName, resultDesc

    def extractFromFilePath(self, filepath: str) -> Tuple[bool, str, str]:
        resultName: str = None
        resultDesc: str = None

        f = open(filepath, 'r')
        lines = f.readlines()
        f.close()

        return self.extractFromFileLines(lines)
