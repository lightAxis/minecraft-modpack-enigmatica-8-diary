#!/usr/bin/env python3

from typing import List, Dict, Tuple, Set
import os
from PIL import Image


def __recursive_image_path_get(path: str, images: List[str]):
    paths: List[str] = os.listdir(path)

    for p in paths:
        p = os.path.join(path, p)
        if os.path.isdir(p):
            __recursive_image_path_get(p, images)
        elif os.path.isfile(p):
            images.append(p)


def __adjust_image(path: str):
    print("input : " + path)
    im1 = Image.open(path)

    isExtJPG: bool = False
    savepath = path
    if os.path.splitext(path)[1] == '.jpg':
        isExtJPG = True
    else:
        print("not jpg. change to .jpg file.")
        im1 = im1.convert("RGB")

    isWidth600: bool = False
    if im1.size[0] > 720:
        target_height = 720 / im1.size[0] * im1.size[1]
        print("image width is too big:" +
              str(str(im1.size[0])) + " > 720/ resize to [720 " + str(int(target_height))+"]")
        im1 = im1.resize([720, int(target_height)])
    else:
        isWidth600 = True
    # os.remove(path)

    if isExtJPG and isWidth600:
        return

    os.remove(path)
    savepath = os.path.splitext(path)[0] + '.jpg'
    im1.save(savepath)


if __name__ == "__main__":
    # Execute when the module is not initialized from an import statement.
    print("main!")

    imagePaths: List[str] = []
    __recursive_image_path_get("docs/asset", imagePaths)

    for path in imagePaths:
        __adjust_image(path)

    # print(imagePaths)
