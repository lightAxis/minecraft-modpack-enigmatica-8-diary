#!/usr/bin/env python3

from typing import List, Dict
import os

from .TagExtractors.TagExtractor import TagExtractor
from .LinkExtractors.LinkExtractor import LinkExtractor
from .NameDescExtractors.NameDescExtractor import NameDescExtractor

from .TagExtractors.DefaultTagExtractor import DefaultTagExtractor
from .LinkExtractors.DefaultLinkExtractor import DefaultLinkExtractor
from .NameDescExtractors.DefaultNameDescExtractor import DefaultNameDescExtractor

from .TagGenerators.TagGenerator import TagGenerator
from .TagParsers.TagParser import TagParser

from .EnumStructs import *
from .Extractors_t import *


class TagLinker:
    def __init__(self):
        self._TagExtractor: TagExtractor = DefaultTagExtractor()
        self._NameDescExtractor: NameDescExtractor = DefaultNameDescExtractor()
        self._LinkExtractor: LinkExtractor = DefaultLinkExtractor()
        self._TagParsers: Dict[str, TagParser] = dict()
        self._TagGenerators: Dict[str, TagGenerator] = dict()
        pass

    def __recursive_filePath_query(self, path_: str, paths: List[str]):
        if (os.path.isfile):
            if (os.path.splitext(path_)[1] == ".md"):
                paths.append(path_)
                return

        subpaths: List[str] = os.listdir(path_)

        for subpath in subpaths:
            self.__recursive_filePath_query(
                os.path.join(path_, subpath), paths)

    def set_TagExtractor(self, ext: TagExtractor):
        self._TagExtractor = ext

    def set_NameDescExtractor(self, ext: NameDescExtractor):
        self._NameDescExtractor = ext

    def set_LinkExtractor(self, ext: LinkExtractor):
        self._LinkExtractor = ext

    def add_TagParser(self, parser: TagParser):
        if (self._TagParsers.get(parser.getParserType()) != None):
            raise Exception(
                "Tag parser type already exist in TagLinker! TagType : " + parser.getParserType())

        self._TagParsers[parser.getParserType()] = parser

    def add_TagGenerator(self, generator: TagGenerator):
        if (self._TagGenerators.get(generator.getGeneratorType()) != None):
            raise Exception(
                "Tag Generator type already exist in TagLInker!, TagType : " + generator.getGeneratorType())
        self._TagGenerators[generator.getGeneratorType()] = generator

    def LinkTargets(self, dirPath: str):

        # query all file path in dir
        filePaths: List[str] = []
        self.__recursive_filePath_query(dirPath, filePaths)

        # parse every tag infos from files
        tagInfos: List[tag_desc_t] = []
        for filepath in filePaths:
            temp_tagInfos: List[tag_desc_t] = self._TagExtractor.extractFromFile(
                filepath)
            self._NameDescExtractor.extractFromFileLines
            isOK, Name, Desc = self._NameDescExtractor.extractFromFilePath(
                filepath)

            for temp_tagInfo in temp_tagInfos:
                temp_tagInfo.FileName = Name
                temp_tagInfo.FileDesc = Desc
                temp_tagInfo.FilePath = filepath

            tagInfos.extend(temp_tagInfos)

            print("extract tag info in file : " + filepath)
            for taginfo in temp_tagInfos:
                print("Type: " + taginfo.Type.name + ", Direction: "+taginfo.Direction.name +
                      ", Style: " + taginfo.TagStyle + ", Name: " + taginfo.TagName)

        # prepare for extractors
        extractors: Extractors_t = Extractors_t()
        extractors.Link = self._LinkExtractor
        extractors.NameDesc = self._NameDescExtractor
        extractors.Tag = self._TagExtractor

        # parse every tag source infos from tag infos
        tagSourcesDict: Dict[str, List[tag_source_t]] = dict()

        for taginfo in tagInfos:
            # if no matching tag style, continue
            if (self._TagParsers.get(taginfo.TagStyle) == None):
                continue

            # if tag is not source type, continue
            if (taginfo.Direction != TagDirection.SOURCE):
                continue

            # get tag parser for this tag
            tagParser = self._TagParsers[taginfo.TagStyle]

            tagSourceDescs = tagParser.ParseDescs_inContent(
                taginfo, extractors)

            print("extract tag source info in file : " + taginfo.FilePath)
            if (len(tagSourceDescs) >= 1):
                print("extracted " + str(len(tagSourceDescs)) + " tag sources")

            # add to tag source descs Dict
            if (tagSourcesDict.get(taginfo.TagName) == None):
                tagSourcesDict[taginfo.TagName] = []
                print("Registering new Tag Name : " + taginfo.TagName)
            tagSourcesDict[taginfo.TagName].extend(tagSourceDescs)

        # generate every tag target infos to files
        for taginfo in tagInfos:
            # if no matching tag style, continue
            if (self._TagGenerators.get(taginfo.TagStyle) == None):
                continue

            # if tag is not source type, continue
            if (taginfo.Direction != TagDirection.TARGET):
                continue

            # get tag generator for this tag
            tagGenerator = self._TagGenerators[taginfo.TagStyle]

            # # if not tag source found for this tag name, skip
            # if (tagSourcesDict.get(taginfo.TagName) == None):
            #     continue

            f = open(taginfo.FilePath, 'r')
            lines = f.readlines()
            f.close

            print("Generating Tag content in file : " + taginfo.FilePath)
            print("TagGenerator: " + tagGenerator.getGeneratorType())
            new_lines: List[str] = []
            tagSources: List[tag_source_t] = []
            if (tagSourcesDict.get(taginfo.TagName) != None):
                tagSources = tagSourcesDict[taginfo.TagName]
            else:
                tagSources = []

            new_lines = tagGenerator.Generate_inLines(
                lines, taginfo, tagSources, extractors)

            print("Generated " + str(len(new_lines)) + " lines inside tag")
            print("Write new file at :" + taginfo.FilePath)

            f = open(taginfo.FilePath, 'w')
            f.writelines(new_lines)
            f.close()
        pass
