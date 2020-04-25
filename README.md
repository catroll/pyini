<h1><a href="https://gitlab.com/whoatemybutte7/pyini/"><img src="https://i.imgur.com/Doy9cmm.png" alt="PyINI" width="70" height="70"></p> PyINI</a></h1>

## Python INI File Manipulator
Forked from [https://github.com/PolyEdge/PyINI](https://github.com/PolyEdge/PyINI), updated for Python 3.

[![Version: 1.0](https://img.shields.io/badge/version-1.0-brightgreen)](https://gitlab.com/whoatemybutte7/pyini/-/tags)
[![License: GPLv3+](https://img.shields.io/badge/license-GPLv3+-blue)](https://gitlab.com/whoatemybutte7/pyini/-/blob/master/LICENSE)
[![Pylint: 10.0/10.0](https://img.shields.io/badge/pylint-10.0/10.10-red)]()
[![Dependencies: 0](https://img.shields.io/badge/dependencies-0-orange)]()

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Support](#support)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)


## Getting Started

### Prerequisites

- [Python ≥3.6](https://www.python.org/downloads/)

### Installation
 
Once Python 3 is installed alongwith [Pip](https://www.w3schools.com/python/python_pip.asp):

```bash
python3 -m pip install git+https://gitlab.com/whoatemybutte7/pyini.git@master
```

## Support

PyINI supports:
* (**\#**) Hash Comments
* (**\;**) Semicolon Comments
* (**\[\]**) Case-insensitive Groups
* (**\=**) Equals Delimiter
* (**\:**) Colon Delimiter

## Usage

```python
import pyini

with open("/tmp/file.ini") as f:
  ini = pyini.INI(f)

# Geting group list
repr(ini)

# Get items within a group
print(ini["group1"].items)

# Set a value for a key of group
ini["group1"]["key"] = "New Value"

# Set a value for a key without a group
ini["__default__"]["key"] = "New Value"

# Delete a key of a group
del(ini["group1"]["key"])

# Delete a key without a group
del(ini["__default__"]["key"])

# Create a new group
ini.create_group("group2")

# Delete a group
del(ini["group2"])

# To read the INI
print(ini.dump())

# To write to a file; 'stream' must be open(), or have .write()
ini.dump(stream=open("/tmp/newfile.ini", "w"))
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

If there is an individual issue you would like to bring attention to, please 
[open one here](https://gitlab.com/whoatemybutte7/pyini/issues/new).

## License

Distributed under the [GPLv3](https://choosealicense.com/licenses/gpl-3.0/) license.

See the included [LICENSE](https://gitlab.com/whoatemybutte7/pyini/blob/master/LICENSE) for the full text, or
 visit [GNU's website](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Contact

* <a href="https://discordapp.com"><img src="https://i.imgur.com/uJxRK5x.png" width="16"/> Discord</a> - `WhoAteMyButter#5864`
* <a href="https://gitlab.com/whoatemybutte7"><img src="https://i.imgur.com/xZaRvQA.png" width="16"/> GitLab</a> - `whoatemybutte7`

## Acknowledgements

* <a href="https://github.com/PolyEdge/PyINI"><img src="https://i.imgur.com/yqJ2Esg.png" width="16"/> GitHub - `PolyEdge: PyINI`</a>