(window.webpackJsonp=window.webpackJsonp||[]).push([[81],{412:function(t,a,s){t.exports=s.p+"assets/img/TagLinker.da091fff.png"},602:function(t,a,s){"use strict";s.r(a);var n=s(7),e=Object(n.a)({},(function(){var t=this,a=t._self._c;return a("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[a("h1",{attrs:{id:"taglinker"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#taglinker"}},[t._v("#")]),t._v(" TagLinker")]),t._v(" "),a("p",[t._v("Simple tag based text generator between markdown files for this repo.")]),t._v(" "),a("ul",[a("li",[a("a",{attrs:{href:"#quick-start"}},[t._v("Quick Start")])]),t._v(" "),a("li",[a("a",{attrs:{href:"#basic-concepts"}},[t._v("Basic Concepts")]),t._v(" "),a("ul",[a("li",[a("a",{attrs:{href:"#extracting-tag-information"}},[t._v("Extracting Tag Information")])]),t._v(" "),a("li",[a("a",{attrs:{href:"#processing-the-tag-contents"}},[t._v("Processing the Tag Contents")])]),t._v(" "),a("li",[a("a",{attrs:{href:"#generating-the-tag-contents"}},[t._v("Generating the Tag Contents")])])])]),t._v(" "),a("li",[a("a",{attrs:{href:"#class-diagram"}},[t._v("Class Diagram")])])]),t._v(" "),a("h2",{attrs:{id:"quick-start"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#quick-start"}},[t._v("#")]),t._v(" Quick Start")]),t._v(" "),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("#!/usr/bin/env python3")]),t._v("\n\n"),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" TagLinker "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("*")]),t._v("\n\n"),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("if")]),t._v(" __name__ "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("==")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"__main__"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    tagLinker "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" TagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("set_TagExtractor"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("DefaultTagExtractor"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("set_NameDescExtractor"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("DefaultNameDescExtractor"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("set_LinkExtractor"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("DefaultLinkExtractor"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("add_TagParser"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("LinkListTagParser"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("add_TagParser"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("CopyTagParser"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("add_TagGenerator"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("ReverseLinkListTagGenerator"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("add_TagGenerator"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("FrameTagGenerator"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("add_BlackListFilePath"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"docs/Ko/externalSource/TagLinkerReadme/readme.md"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n\n    tagLinker"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("LinkTargets"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"docs/Ko"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n    "),a("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("pass")]),t._v("\n\n")])])]),a("h2",{attrs:{id:"basic-concepts"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#basic-concepts"}},[t._v("#")]),t._v(" Basic Concepts")]),t._v(" "),a("p",[t._v("TagLinker will extract informations from "),a("code",[t._v("source")]),t._v(" and generate strings to "),a("code",[t._v("target")])]),t._v(" "),a("p",[t._v("The tag open and close pair is in form of comment like this :")]),t._v(" "),a("div",{staticClass:"language-Markdown extra-class"},[a("pre",{pre:!0,attrs:{class:"language-markdown"}},[a("code",[a("span",{pre:!0,attrs:{class:"token title important"}},[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("#")]),t._v(" Source")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_open_source:tagStyle1:tagName --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:argName1:argContent --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:argName2:argContent --\x3e")]),t._v("\ncontent1\ncontent2\ncontent3\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_close --\x3e")]),t._v("\n\n"),a("span",{pre:!0,attrs:{class:"token title important"}},[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("#")]),t._v(" Target")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_open_target:tagStyle2:tagName --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:argName3:argContent --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:argName4:argContent --\x3e")]),t._v("\ngenerated content1\ngenerated content2\ngenerated content3\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_close --\x3e")]),t._v("\n")])])]),a("h3",{attrs:{id:"extracting-tag-information"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#extracting-tag-information"}},[t._v("#")]),t._v(" Extracting Tag Information")]),t._v(" "),a("p",[t._v("TagLinker will firstly extract all tag information in files with "),a("code",[t._v("tag_desc_t")]),t._v(" struct. It has various fields to describe tag pairs."),a("br"),t._v("\nBelow is Extractors used in this stage :")]),t._v(" "),a("ul",[a("li",[a("strong",[t._v("LinkExtractor")]),a("br"),t._v("\nExtract link information from string or generate string with link."),a("br"),t._v("\nNow we have DefaultLinkExtrator.")]),t._v(" "),a("li",[a("strong",[t._v("NameDescExtractor")]),a("br"),t._v("\nExtract name of current file"),a("br"),t._v("\n(different with filename, if the file content starts with # ASDF, then fileName is ASDF)."),a("br"),t._v("\nNow we have DefaultNameDescExtractor")]),t._v(" "),a("li",[a("strong",[t._v("TagExtractor")]),a("br"),t._v("\nExtract tag info from commented lines. tag is open, closed, target, source, tagName and tagStyle, tag args etc."),a("br"),t._v("\nNow we have DefaultTagExtractor")])]),t._v(" "),a("p",[a("strong",[t._v("You can make custom Extractors by inherit abstract classes of each.")])]),t._v(" "),a("p",[t._v("Example: ./asdf/tag_test1.md")]),t._v(" "),a("div",{staticClass:"language-markdown extra-class"},[a("pre",{pre:!0,attrs:{class:"language-markdown"}},[a("code",[a("span",{pre:!0,attrs:{class:"token title important"}},[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("#")]),t._v(" filename")]),t._v("\n\nfiledesc\n\n... \n\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_open_source:link_list:contrib --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:preset:presetName --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:arg1:argv1 --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token list punctuation"}},[t._v("-")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token url"}},[t._v("["),a("span",{pre:!0,attrs:{class:"token content"}},[t._v("content111")]),t._v("]("),a("span",{pre:!0,attrs:{class:"token url"}},[t._v("link1.md")]),t._v(")")]),t._v("  \ncontent111_desc\n"),a("span",{pre:!0,attrs:{class:"token list punctuation"}},[t._v("-")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token url"}},[t._v("["),a("span",{pre:!0,attrs:{class:"token content"}},[t._v("content222")]),t._v("]("),a("span",{pre:!0,attrs:{class:"token url"}},[t._v("link2.md")]),t._v(")")]),t._v("  \n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_close --\x3e")]),t._v("\n\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_open_target:reverse_link_list:contrib --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_close --\x3e")]),t._v("\n...\n")])])]),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# extracted tag_desc_t")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    FilePath"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"./asdf/tag_test1.md"')]),t._v("\n    FileName"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"filename"')]),t._v("\n    FileDesc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"filedesc"')]),t._v("\n    Type"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" TagType "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" TagType"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("OPEN\n    Direction"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" TagDirection "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" TagDirection"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("SOURCE\n\n    TagStyle"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"link_list"')]),t._v("\n    TagName"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"contrib"')]),t._v("\n    TagStr"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"\x3c!-- tag_open:source:link_list:contrib --\x3e"')]),t._v("\n\n    Content"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" List"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"- [content111](link1.md)  \\n"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"content111_desc\\n"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n\n    ArgDict"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" Dict"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"preset"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"presetName"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"arg1"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"argv1"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    FilePath"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"./asdf/tag_test1.md"')]),t._v("\n    FileName"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"filename"')]),t._v("\n    FileDesc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"filedesc"')]),t._v("\n    Type"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" TagType "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" TagType"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("OPEN\n    Direction"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" TagDirection "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" TagDirection"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("TARGET\n    TagStyle"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"reverse_link_list"')]),t._v("\n    TagName"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"contrib"')]),t._v("\n    TagStr"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"\x3c!-- tag_open:target:reverse_link_list:contrib --\x3e"')]),t._v("\n    Content"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" List"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n    ArgDict"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" Dict"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n\n")])])]),a("h3",{attrs:{id:"processing-the-tag-contents"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#processing-the-tag-contents"}},[t._v("#")]),t._v(" Processing the Tag Contents")]),t._v(" "),a("p",[t._v("TagLinker will process tag contents("),a("code",[t._v("tag_desc_t")]),t._v(") to "),a("code",[t._v("tag_source_t")]),t._v(" struct by using different tag exctractors attached. Extracted tag infos will come out as a struct "),a("code",[t._v("tag_desc_t")]),t._v(".")]),t._v(" "),a("ul",[a("li",[a("strong",[t._v("TagParser")]),a("br"),t._v("\nParse the tag_desc_t into tag_source_t based on tagStyle field."),a("br"),t._v("\nNow we have CopyTagParser, LinkListTagParser")])]),t._v(" "),a("p",[a("strong",[t._v("You can make custom Parsers by inherit abstract classes of each.")])]),t._v(" "),a("p",[t._v("Example:")]),t._v(" "),a("div",{staticClass:"language-python extra-class"},[a("pre",{pre:!0,attrs:{class:"language-python"}},[a("code",[a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# processed tag_desc_t above to list of tag_source_t, using ")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    TargetName"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"content111"')]),t._v("\n    TargetDesc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" List"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"content111_desc\\n"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n    TargetPath"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"./asdf/link1.md"')]),t._v("\n    SourceName"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"filename"')]),t._v("\n    SourcePath"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"./asdf/tag_test1.md"')]),t._v("\n    SourceDesc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"filedesc"')]),t._v("\n    Content"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" List"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"- [content111](link1.md)  \\n"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"content111_desc\\n"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    TargetName"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"content222"')]),t._v("\n    TargetDesc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" List"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"content222_desc\\n"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n    TargetPath"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"./asdf/link2.md"')]),t._v("\n    SourceName"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"filename"')]),t._v("\n    SourcePath"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"./asdf/tag_test1.md"')]),t._v("\n    SourceDesc"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"filedesc"')]),t._v("\n    Content"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" List"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"- [content111](link1.md)  \\n"')]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),a("span",{pre:!0,attrs:{class:"token string"}},[t._v('"content111_desc\\n"')]),t._v(" "),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n")])])]),a("p",[t._v("Extraction method of tag content into tag_desc_t is determined by tagStyle."),a("br"),t._v("\nIt is related to TagExtractors classes attached to TagLinker. TagLinker can have multiple TagExtractors so can extract various type of tagStyle contents.")]),t._v(" "),a("h3",{attrs:{id:"generating-the-tag-contents"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#generating-the-tag-contents"}},[t._v("#")]),t._v(" Generating the Tag Contents")]),t._v(" "),a("p",[t._v("TagLinker will now generate contents between tag_target tag pair. It will using matching TagGenerator with TagStyle."),a("br"),t._v("\nEach TagGenerator will use list of tag_source_t. But only with the same TagName will be used to generate contents.")]),t._v(" "),a("ul",[a("li",[a("strong",[t._v("TagGenerator")]),a("br"),t._v("\nGenerate the string between tag target comment pair."),a("br"),t._v("\nfilters list of tag_source_t with tagName, using ones only with same tagName."),a("br"),t._v("\nnow we have FrameTagGenerator, ReverseLinkListGenerator.")])]),t._v(" "),a("p",[a("strong",[t._v("You can make custom Generators by inherit abstract classes of each.")])]),t._v(" "),a("p",[t._v("Example: file ./asdf/link1.md")]),t._v(" "),a("div",{staticClass:"language-markdown extra-class"},[a("pre",{pre:!0,attrs:{class:"language-markdown"}},[a("code",[a("span",{pre:!0,attrs:{class:"token title important"}},[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("#")]),t._v(" content111")]),t._v("\n\nlink1_desc\n\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_open_target:reverse_link_list:contrib --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:header:### hhh --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:list_type:table --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:table_header: | name | desc | --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_arg:desc_type:target --\x3e")]),t._v("\n"),a("span",{pre:!0,attrs:{class:"token title important"}},[a("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("###")]),t._v(" hhh")]),t._v("\n| name | desc |\n|"),a("span",{pre:!0,attrs:{class:"token url"}},[t._v("["),a("span",{pre:!0,attrs:{class:"token content"}},[t._v("filename")]),t._v("]("),a("span",{pre:!0,attrs:{class:"token url"}},[t._v("./asdf/tag_test1.md")]),t._v(")")]),t._v("|content111_desc|\n"),a("span",{pre:!0,attrs:{class:"token comment"}},[t._v("\x3c!-- tag_close --\x3e")]),t._v("\n")])])]),a("h2",{attrs:{id:"class-diagram"}},[a("a",{staticClass:"header-anchor",attrs:{href:"#class-diagram"}},[t._v("#")]),t._v(" Class Diagram")]),t._v(" "),a("p",[a("img",{attrs:{src:s(412),alt:"asdf"}})])])}),[],!1,null,null,null);a.default=e.exports}}]);