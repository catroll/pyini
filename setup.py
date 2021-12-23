#!/usr/bin/env python3
# coding=utf-8
import pyini
import setuptools

with open("README.md") as fh:
	long_description = fh.read()

setuptools.setup(
	name="PyINI",
	version=pyini.__version__,
	author="WhoAteMyButter",
	description="INI data reader & writer",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://gitlab.com/whoatemybutter/pyini",
	packages=setuptools.find_packages(),
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3 :: Only",
		"Operating System :: OS Independent",
		"Topic :: Utilities",
		"Topic :: Documentation",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Environment :: Win32 (MS Windows)"
	],
	python_requires='>=3.0',
)
