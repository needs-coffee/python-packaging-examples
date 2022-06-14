#!/usr/bin/env python3

# for cleaning the dist files created in the demo projects

import os
import re
from send2trash import send2trash

project_root = os.path.dirname(os.path.realpath(__file__))
project_dirs = [
    os.path.join(project_root, dir)
    for dir in os.listdir(project_root)
    if (os.path.isdir(dir) and re.search(r"^\d{2}", dir))
]

for dir in project_dirs:
    for x in os.listdir(dir):
        if x == "dist":
            try:
                send2trash(os.path.join(dir, x))
                print(f"deleted dist from {dir}")
            except Exception as e:
                print(f"unable to delete dist from {dir} Exception: {e}")
        elif x.endswith("egg-info"):
            try:
                send2trash(os.path.join(dir, x))
                print(f"deleted egg.info from {dir}")
            except Exception as e:
                print(f"unable to delete egg.info from {dir} Exception: {e}")
        elif x == "hello_world":
            sub_path = os.path.join(dir, x, "__pycache__")
            if os.path.isdir(sub_path):
                try:
                    send2trash(sub_path)
                    print(f"deleted __pycache__ from {sub_path}")
                except Exception as e:
                    print(
                        "unable to delete __pycache__ "
                        + f"from {sub_path} Exception: {e}"
                    )
