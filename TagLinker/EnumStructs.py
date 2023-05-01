#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum


class TagType(Enum):
    """It this is open tag or not
    """
    OPEN = 1,
    CLOSE = 2,


class TagDirection(Enum):
    """Direction of tag matching
    """
    SOURCE = 1
    TARGET = 2


@dataclass
class tag_desc_t:
    FilePath: str = ""
    FileName: str = ""
    FileDesc: str = ""
    Type: TagType = TagType.OPEN
    Direction: TagDirection = TagDirection.SOURCE
    """Direction of this tag matching
    """
    TagStyle: str = ""
    TagName: str = ""
    Content: List[str] = field(default_factory=list)
    """Whole content lines inside this tag pair
    """


@dataclass
class tag_target_t:
    Name: str = ""
    """Name of this target document
    """
    Desc: str = ""
    """Description of this target document
    """
    Path: str = ""
    """Target document Path relative to main python exec
    """


@dataclass
class tag_source_t:
    TargetName: str = ""
    """Name of target document
    """
    TargetDesc: str = ""
    """Description of target document
    """
    TargetPath: str = ""
    """Target document path relative to main python exec
    """
    SourceName: str = ""
    """Name of source document
    """
    SourcePath: str = ""
    """Source document path relative to main python exec
    """
    SourceDesc: str = ""
    """Description of Source document
    """
    Content: List[str] = field(default_factory=list)
    """List of string, inside this tag
    """
