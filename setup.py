#!/usr/bin/env python3
# coding=utf-8
"""Setup for module pyini"""
import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyini",
    version="1.0",
    author="whoatemybutte7",
    description="Python INI File Manipulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/whoatemybutte7/pyini",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Documentation",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Environment :: Win32 (MS Windows)"
    ],
    python_requires='>=3.6',
)
