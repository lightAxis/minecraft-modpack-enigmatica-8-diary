#!/usr/bin/env python3

from ..EnumStructs import *

import os
from typing import List, Dict, Tuple, Optional, Union
from abc import *
import copy


class LinkExtractor(metaclass=ABCMeta):
    def __init__(self):
        self._lineContents: List[Union[str, link_pair_t]] = []

    def getLineContents(self) -> List[Union[str, link_pair_t]]:
        return self._lineContents

    def setLineContents(self, lineContents: List[Union[str, link_pair_t]]):
        self._lineContents = lineContents

    def GenerateLinkPairStr(self, linkPair_t: link_pair_t) -> str:
        return "[" + linkPair_t.Name + "](" + linkPair_t.LinkPath+")"

    def GenerateLineStr(self) -> str:
        tempStr: str = ""

        for linkPair in self._lineContents:
            if (type(linkPair) == str):
                tempStr = tempStr + linkPair
                continue

            tempStr = tempStr + self.GenerateLinkPairStr(linkPair)
            continue

        return tempStr

    @abstractclassmethod
    def ExtractFromLine(self, line: str) -> List[Union[str, link_pair_t]]:
        pass
