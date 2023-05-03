#!/usr/bin/env python3

from TagLinker import *

if __name__ == "__main__":
    tagLinker = TagLinker()

    tagLinker.set_TagExtractor(DefaultTagExtractor())
    tagLinker.set_NameDescExtractor(DefaultNameDescExtractor())
    tagLinker.set_LinkExtractor(DefaultLinkExtractor())

    tagLinker.add_TagParser(DescriptionTagParser())
    tagLinker.add_TagParser(CopyTagParser())

    tagLinker.add_TagGenerator(ContributionListTagGenerator())

    tagLinker.LinkTargets("docs/Ko")
    pass
