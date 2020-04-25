#!/usr/bin/env python3
# coding=utf-8
"""
Python INI file manipulator

To open an ini file, pass a string or a file stream to the 'INI' class.

Edit the INI as if the INI class is a dictionary full of dictionaries.
'__default__' maps to items without a group.

Forked from https://github.com/PolyEdge/PyINI/ by WhoAteMyButter, for Python 3."""
from io import TextIOWrapper


class INI:
    """Base INI class"""
    class INIGroup:
        """
        Group in an INI file, like "[group]"
        """
        def __init__(self, name: str):
            """Read INI from file object or string given -> INI object"""
            self.name = str(name)
            self.items = []

        def __setitem__(self, item: str, val: str):
            if not isinstance(item, str):
                raise TypeError("Invalid subscript type")
            for index in range(0, len(self.items)):
                if self.items[index][0] == item:
                    self.items[index][1] = val
                    return
            self.items.append([item, val])

        def __getitem__(self, item: str) -> str:
            if not isinstance(item, str):
                raise TypeError("Invalid subscript type")
            for index in range(0, len(self.items)):
                if self.items[index][0] == item:
                    return self.items[index][1]
            raise IndexError("Key " + str(item) + " not found.")

        def __delitem__(self, item: str):
            if not isinstance(item, str):
                raise TypeError("Invalid subscript type")
            for index in range(0, len(self.items)):
                if self.items[index][0] == item:
                    del self.items[index]
                    return
            raise IndexError("Key " + str(item) + " not found.")

        def __iter__(self) -> iter:
            return iter({index[0]: index[1] for index in self.items if index[0] != -1})

        def __repr__(self) -> str:
            return (
                "<INI group {"
                + (
                    ", ".join(
                        [
                            """ + str(index[0]) + "": "" + str(index[1]) + """
                            for index in self.items
                            if index[0] != -1
                        ]
                    )
                )
                + "}>"
            )

        def add_blank_line(self):
            """
            Add a blank line
            """
            self.items.append([-1, "blankline"])

        def add_comment(self, comment: str):
            """
            :param comment:
            """
            self.items.append([-1, "comment", comment])

        def add_raw(self, raw: str):
            """
            :param raw:
            """
            self.items.append([-1, "raw", raw])

    def __init__(self, ini: (TextIOWrapper, str)):
        if isinstance(ini, TextIOWrapper):
            if str(ini.mode).lower().strip() == "r":
                data = ini.read()
                ini.close()
            else:
                raise ValueError("File object does not support reading ("r") mode")
        else:
            if isinstance(ini, str):
                data = str(ini)
            else:
                raise TypeError(
                    'Expected "str" or "io.TextIOWrapper" but got '
                    + str(ini.__class__).split()[1][:-1] + "; are you using open()?"
                )
        self.groups = [self.INIGroup("__default__")]
        for index in [y.strip() for y in str(data).rsplit(sep="\n")]:
            if index == "":
                self.groups[-1].add_blank_line()
            elif index[0] in ["#", ";"]:
                self.groups[-1].add_comment(index[1:])
            elif index[0] == "[":
                self.groups.append(self.INIGroup(index[1:-1]))
            elif len(index.split("=", 1)) > 1:
                self.groups[-1][index.split("=", 1)[0].strip()] = index.split("=", 1)[1].strip()
            elif len(index.split(":", 1)) > 1:
                self.groups[-1][index.split(":", 1)[0].strip()] = index.split(":", 1)[1].strip()
            else:
                self.groups[-1].add_raw(index)

    def create_group(self, name: str):
        """
        :param name:
        """
        for index in range(0, len(self.groups)):
            if self.groups[index].name == name:
                raise TypeError("cannot create existing INI group.")
        self.groups.append(self.INIGroup(name))

    def dump(self, stream: TextIOWrapper = None):
        """
        :param stream:
        :return:
        """
        output = []
        for index in self.groups:
            if index.name != "__default__":
                output.append("[" + index.name + "]")
            for item in index.items:
                if (item[0] == -1) and (item[1] == "blankline"):
                    output.append("")
                elif (item[0] == -1) and (item[1] == "comment"):
                    output.append("#" + item[2])
                elif (item[0] == -1) and (item[1] == "raw"):
                    output.append(item[2])
                else:
                    output.append(str(item[0]) + " = " + str(item[1]))
        output = "\n".join(output)
        if stream is None:
            return output
        elif str(stream.mode).lower().strip() in ["w", "w+"] and not stream.closed:
            stream.write(output)
            stream.close()
        elif stream.closed:
            raise IOError("Cannot write to closed stream")
        else:
            raise ValueError("Invalid file mode")

    def __setitem__(self, item, val):
        raise TypeError("cannot assign to base INI group")

    def __getitem__(self, item: str):
        if not isinstance(item, str):
            raise TypeError("Invalid subscript type")
        for index in range(0, len(self.groups)):
            if str(self.groups[index].name).lower() == item.lower():
                return self.groups[index]
        raise IndexError("Key " + str(item) + " not found.")

    def __delitem__(self, item: str):
        if not isinstance(item, str):
            raise TypeError("Invalid subscript type")
        for index in range(0, len(self.groups)):
            if str(self.groups[index].name).lower() == item.lower():
                del self.groups[index]
                return
        raise TypeError("cannot delete nonexisting INI group.")

    def __iter__(self):
        return iter({index.name: index for index in self.groups})

    def __repr__(self):
        return "<ini group collection [" + \
               (", ".join(["\"" + index.name + "\"" for index in self.groups])) + \
               "]>"
