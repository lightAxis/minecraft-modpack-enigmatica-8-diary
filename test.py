#!/usr/bin/env python3

from TagLinker.TagExtractor.DefaultTagExtractor import DefaultTagExtractor

from TagLinker.TagParser.DescriptionTagParser import DescriptionTagParser

from TagLinker.EnumStructs import *


from TagLinker.TagGenerator import *

if __name__ == "__main__":
    aa = DefaultTagExtractor()

    taginfos: List[tag_desc_t] = aa.extractTagInfosFromFile("test.md")

    bb = DescriptionTagParser()
    for tag in taginfos:
        print(tag)
        bb.ParseDescs_inContent(tag.Content)

    pass
