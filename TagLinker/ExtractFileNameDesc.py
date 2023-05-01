#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
from .EnumStructs import *


def ExtractFileNameDescFromFilePath(filepath: str) -> Tuple[bool, str, str]:
    resultName: str = None
    resultDesc: str = None

    f = open(filepath, 'r')
    lines = f.readlines()
    f.close()

    find_name: bool = False
    for line in lines:
        NameIndex = line.find("# ")

        if (NameIndex >= 0):
            find_name = True
            line = line.replace("\n", "")
            desc_temp.Name = line[NameIndex+1:]
            continue

        line_no_space = line.replace(" ", "")
        line_no_space = line_no_space.replace("\n", "")
        if (line_no_space == "" and find_name):
            continue

        if (find_name):
            desc_temp.Desc = line
            break

    isOK: bool = False
    if (resultDesc != None and resultName != None):
        isOK = True

    return isOK, resultName, resultDesc
