#!/usr/bin/env python3

from TagLinker.LinkExtractors import *
from TagLinker.NameDescExtractors import *
from TagLinker.TagExtractors import *
from TagLinker.TagParsers import *
from TagLinker.TagGenerators import *

from TagLinker.EnumStructs import *

from TagLinker.Extractors_t import *


# from TagLinker.TagGenerators import *

if __name__ == "__main__":
    tagExt = DefaultTagExtractor()
    nameDescExt = DefaultNameDescExtractor()

    tagInfos: List[tag_desc_t] = []

    fileList: List[str] = ["test.md", "test2.md"]

    for file in fileList:
        temp_tagInfos = tagExt.extractFromFile(file)
        isOK, Name, Desc = nameDescExt.extractFromFilePath(file)
        for temp_tagInfo in temp_tagInfos:
            temp_tagInfo.FileName = Name
            temp_tagInfo.FileDesc = Desc
            temp_tagInfo.FilePath = file
        tagInfos.extend(temp_tagInfos)

    linkExt = DefaultLinkExtractor()

    Extractors: Extractors_t = Extractors_t()
    Extractors.Link = linkExt
    Extractors.NameDesc = nameDescExt
    Extractors.Tag = tagExt

    print("--------check descripotion tag parser!----------\n")

    Parsers: Dict[str, TagParser] = dict()
    descParser = DescriptionTagParser()
    copyParser = CopyTagParser()
    Parsers[descParser.getParserType()] = descParser
    Parsers[copyParser.getParserType()] = copyParser

    tagSourcesDict: Dict[str, List[tag_source_t]] = dict()
    for taginfo in tagInfos:
        # if no matching tag style, continue
        if (Parsers.get(taginfo.TagStyle) == None):
            continue

        # if tag is not source type, continue
        if (taginfo.Direction != TagDirection.SOURCE):
            continue

        # get tag parser for this tag
        tagParser = Parsers[taginfo.TagStyle]

        # extract tag souce descs from tag info
        tagSourceDescs = tagParser.ParseDescs_inContent(
            taginfo, Extractors)

        # add to tag source descs Dict
        if (tagSourcesDict.get(taginfo.TagName) == None):
            tagSourcesDict[taginfo.TagName] = []
        tagSourcesDict[taginfo.TagName].extend(tagSourceDescs)

    print("-----------check contribution list tag generator------------")

    contGen = ContributionListTagGenerator()
    Generators: Dict[str, TagGenerator] = dict()
    Generators[contGen.getGeneratorType()] = contGen

    for taginfo in tagInfos:
        # if no matching tag style, continue
        if (Generators.get(taginfo.TagStyle) == None):
            continue

        # if tag is not source type, continue
        if (taginfo.Direction != TagDirection.TARGET):
            continue

        # get tag generator for this tag
        tagGenerator = Generators[taginfo.TagStyle]

        f = open(taginfo.FilePath, 'r')
        lines = f.readlines()
        f.close

        if (tagSourcesDict.get(taginfo.TagName) == None):
            continue

        new_lines = tagGenerator.Generate_inLines(
            lines, taginfo, tagSourcesDict[taginfo.TagName], Extractors)

        f = open(taginfo.FilePath+"new", 'w')
        f.writelines(new_lines)
        f.close()

        print("------------")

    pass
