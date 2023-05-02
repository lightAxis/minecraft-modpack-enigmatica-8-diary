#!/usr/bin/env python3

from ..EnumStructs import *
from .LinkExtractor import LinkExtractor

import os
from typing import List, Dict, Tuple, Optional
from abc import *
import copy


class DefaultLinkExtractor(LinkExtractor):
    def __init__(self):
        super().__init__()

    def ExtractFromLine(self, line: str) -> List[Union[str, link_pair_t]]:
        temp_line_contents: List[Union[str, link_pair_t]] = []

        while True:
            line_nameOpen: int = line.find("[")
            line_nameClose: int = line.find("](")
            line_linkClose: int = line.find(")")

            line_nameOpen_nameClose: bool = line_nameOpen < line_nameClose
            line_nameClose_linkClose: bool = line_nameClose < line_linkClose

            line_nameOpen_exist: bool = line_nameOpen > -1
            line_nameClose_exist: bool = line_nameClose > -1
            line_linkClose_exist: bool = line_linkClose > -1

            if (line_nameOpen_nameClose and line_nameClose_linkClose and
               line_nameOpen_exist and line_nameClose_exist and line_linkClose_exist):

                temp_line_contents.append(line[0:line_nameOpen])

                temp_linkpair_t: link_pair_t = link_pair_t()
                temp_linkpair_t.Name = line[line_nameOpen+1:line_nameClose]
                temp_linkpair_t.LinkPath = line[line_nameClose +
                                                2:line_linkClose]
                temp_line_contents.append(temp_linkpair_t)

                line = line[line_linkClose+1:]
                continue

            temp_line_contents.append(line)
            break

        self._lineContents = temp_line_contents

        return temp_line_contents
