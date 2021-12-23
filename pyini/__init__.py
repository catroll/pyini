#!/usr/bin/env python3
# coding=utf-8
# encoding=utf-8
# pylint: disable=W0311
r"""INI <https://en.wikipedia.org/wiki/INI_file> is a configuration file
format commonly used in Microsoft Windows operating systems and for
plain & simple sectioned key-value storage.

:mod:`PyINI` is a INI file reader & writer
with a structure similar to Python's :mod:`json` module.

INI data is read and returned as a dictionary,
and dictionaries can be written as INI files.

Function structure is similar to ``json``,
with the corresponding ``load()``, ``loads()``, ``dump()``, and ``dumps()`` functions.

* ``load()``: INI file object -> INI dictionary
* ``loads()``: INI string -> INI dictionary
* ``dump()``: INI dictionary -> **into** file object
* ``dumps()``: INI dictionary -> INI string

Translating INI data to dictionary::

	>>> import pyini
	>>> with open("my_ini_file.ini") as ini:
	...     pyini.load(ini)
	{'owner': {'name': 'John Doe', 'organization': 'Acme Widgets Inc.'}}
	>>> pyini.loads(ini.read())
	{'owner': {'name': 'John Doe', 'organization': 'Acme Widgets Inc.'}}

Translating dictionary to INI data::

	>>> import pyini
	>>> myini = {"a": "b", "c": {"d": "e"}}
	>>> with open("blank_ini_file.ini", "w") as data:
	...     pyini.dump(myini, data)

	>>> pyini.dumps({"a": "b", "c": {"d": "e"}})
	'a=b\n[c]\nd=e'
"""
from __future__ import annotations

import ast

__version__: str = "2.0"


def count_char_startuntil(line: str, char: str) -> int:
	"""
	Count number of ``char`` in ``line``, beginning from the start of ``line``.
	If ``char`` does not start ``line``, 0 will **always** be returned.

	:param line: String to search
	:type line: str
	:param char: Character to match
	:type char: str
	:returns: Number of matched characters starting from line
	"""
	count: int = 0
	for character in line:
		if character == char:
			count += 1
		else:
			break
	return count


def parse_bracketted(line: str) -> str:
	"""
	Given a INI header value such as ``"[[a]]"``, return a string of the header name.

	:param line: Line to parse
	:type line: str
	:returns: Header name
	:rtype: str
	"""
	charc: int = count_char_startuntil(line, "[")
	return line.split("[" * charc)[1].split("]" * charc)[0]


def strip_value_comments(line: str) -> str:
	"""
	Given a line comment, return the text without the comment delimiter.

	:param line: Comment line
	:type line: str
	:returns: Line without comment delimiter
	:rtype: str
	"""
	return line.split(";")[0].split("#")[0].strip()


def value_parse(value: str):
	"""
	Attempt to return real form of a string representation of a value.
	If value cannot be typed into anything, the same value is returned as-is.

	Given string ``"[1,2,3]"``, list ``[1, 2, 3]`` is returned.
	Given string ``"a"``, string ``"a"`` is returned.

	:param value: String representation of any valid type
	:type value: str
	:returns: Literal evaluation of representation
	"""
	try:
		return ast.literal_eval(value)
	except (ValueError, SyntaxError):
		return value


def load(obj) -> dict:
	"""
	Given a valid file object, return a dictionary representation of the INI data.
	Similar to :py:func:`json.load()`, ``obj`` must support ``.read()``.

	:param obj: File path
	:type obj: Any that supports read()
	:returns: INI data as a dictionary
	:rtype: dict
	"""
	return loads(obj.read())


def loads(text: str) -> dict:
	"""
	Given a string, return a dictionary representation of the INI data.

	:param text: INI data
	:type text: str
	:returns: Dictionary of INI data
	:rtype: dict
	"""
	exported: dict = {}
	current: str | None = None
	rcode: list = list(enumerate(str(text).splitlines(False)))
	for content in rcode:
		if content[1].startswith("["):
			current = parse_bracketted(content[1])
			exported[current] = {}
		elif "=" in content[1]:
			key, value = [x.strip() for x in content[1].split("=", 1)]
			if value.endswith("\\"):
				rind = content[0]
				while value.endswith("\\"):
					value = value[:-1]
					value += rcode[rind + 1][1]
					rind += 1
					del rcode[rind]
			if current is not None:
				exported[current][key] = value_parse(strip_value_comments(value))
			else:
				exported[key] = value_parse(strip_value_comments(value))
	return exported


def dump(inidata: dict, obj) -> None:
	"""
	Write dictionary to an writeable object as an INI file.

	* ``obj`` must have ``write()``.
	* ``obj`` will **not** be closed after.

	Returns nothing.

	:param inidata: Dictionary data
	:type inidata: dict
	:param obj: Object to write to
	"""
	obj.write(dumps(inidata))


def dumps(inidata: dict) -> str:
	"""
	Given a dictionary, return that same dictionary in INI format, as a string.

	:param inidata: Dictionary data
	:type inidata: dict
	:return: String of INI data
	:rtype: str
	"""
	ret: str = ""
	for key, value in inidata.items():
		if isinstance(value, dict):
			ret += f"[{key}]\n"
			for subkey, subvalue in value.items():
				ret += f"{subkey}={subvalue}\n"
		else:
			ret += f"{key}={value}\n"
	# Fix newline at end
	ret = ret[:-1] if ret[-1] == "\n" else ret
	return ret
