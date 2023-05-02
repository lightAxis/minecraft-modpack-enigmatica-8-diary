#!/usr/bin/env python3

from typing import List, Dict
import os

from TagExtractors.TagExtractor import TagExtractor
from TagExtractors.DefaultTagExtractor import DefaultTagExtractor

from TagLinker.NameDescExtractors.NameDescExtractor import NameDescExtractor
from TagLinker.NameDescExtractors.DefaultNameDescExtractor import DefaultNameDescExtractor


class TagLinker:
    def __init__(self):
        self._TagExtractor = DefaultTagExtractor()
        self._NameDescExtractor = DefaultNameDescExtractor()
        self._TagParsers = None
        self._TagGenerators = None
        pass

    def set_TagExtractor(self, ext: TagExtractor):
        self._TagExtractor = ext

    def set_NameDescExtractor(self, ext: NameDescExtractor):
        self._NameDescExtractor = ext
