#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List, Dict, Union, Tuple
from enum import Enum

from .TagExtractors.TagExtractor import TagExtractor
from .LinkExtractors.LinkExtractor import LinkExtractor
from .NameDescExtractors.NameDescExtractor import NameDescExtractor


@dataclass
class Extractors_t:
    Link: LinkExtractor = None
    NameDesc: NameDescExtractor = None
    Tag: TagExtractor = None
