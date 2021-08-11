#!/usr/bin/env python

# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import os
from setuptools import setup, find_packages


# Pull out all dependencies in requirements.txt:
rootdir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(rootdir, 'requirements.txt')) as reqs:
    required = reqs.read().splitlines()
deps = [line for line in required if len(line) > 0 and line[0] != "#"]


# Package specification that includes every example.
setup(
    name='test_repo_examples',
    version='0.0.0.1',
    author='Josh Clemons',
    author_email='clemonsjoshua6@gmail.com',
    url='https://github.com/JoshBClemons/test_repo',

    # Since batchkit_examples are located in the same repo as the batchkit lib, we can just depend on
    # the batchkit lib source directly. As an external project, we would instead take dependency
    # on the dependency `batchkit` wheel under `install_requires`.
    packages=["batchkit", "batchkit_examples", "batchkit_examples/speech_sdk"],
    install_requires=deps,
    license="MIT",
    scripts=["batchkit_examples/speech_sdk/run-batch-client"],
)
