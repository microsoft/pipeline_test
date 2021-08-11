#!/usr/bin/env python

# Copyright (c) Microsoft Corporation
# Licensed under the MIT License.

import os
from setuptools import setup, find_packages


# Read description from the README.md
with open("README.md", "r") as fh:
    long_description = fh.read()


# Pull out all dependencies in requirements.txt for the batchkit library only.
rootdir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(rootdir, 'requirements.txt')) as reqs:
    required = reqs.read().splitlines()
deps = []
toggle = False
for line in required:
    if "### batchkit" in line:
        toggle = True
        continue
    elif "###" in line:
        toggle = False
    elif len(line) > 0 and line[0] != "#" and toggle:
        deps.append(line)


# Package specification for batchkit library.
setup(
    name='joshc_repo',
    version='0.0.0.6',
    author='Josh Clemons',
    author_email='clemonsjoshua6@microsoft.com',
    description="None",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/JoshBClemons/test_repo',
    packages=["joshc_repo"],
    install_requires=deps,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
    scripts=[],
)
