<h1>
    <a href="https://gitlab.com/whoatemybutter/pyini/">
        <img src="https://i.imgur.com/WzB0vDv.png" alt="PyINI" width="100" height="100">
        PyINI
    </a>
</h1>

# PyINI

[![Version: 2.0](https://img.shields.io/badge/version-2.0-brightgreen)](https://gitlab.com/whoatemybutter/pyini/-/tags)
[![License: GPLv3+](https://img.shields.io/badge/license-GPLv3+-blue)](https://gitlab.com/whoatemybutter/pyini/-/blob/master/LICENSE)
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


## Getting Started

### Prerequisites

- [Python ≥3.6](https://www.python.org/downloads/)

### Installation
 
Once Python 3 is installed alongside [Pip](https://www.w3schools.com/python/python_pip.asp):

```bash
python3 -m pip install pyini
```

## Support

PyINI supports:
* Section nesting (up to two sections)
* Global declarations
* Reading and writing INI data
* Arrays
* Booleans

## Usage

```python
import pyini

with open("my_ini_file.ini") as file:
    # Load INI data through file
    ini: dict = pyini.load(file)
    # Above is the same as:
    pyini.loads(file.read())
    
    # Write dictionary to file as INI data
    pyini.dump(ini, file)
    # Return dictionary as string of INI data
    pyini.dumps(ini)
```

Any dictionary can ``pyini.dump()`` to valid INI data.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

If there is an individual issue you would like to bring attention to, please 
[open one here](https://gitlab.com/whoatemybutter/pyini/issues/new).

## License

Distributed under the [GPLv3](https://choosealicense.com/licenses/gpl-3.0/) license.

See the included [LICENSE](https://gitlab.com/whoatemybutte7/pyini/blob/master/LICENSE) for the full text,
or visit [GNU's website](https://www.gnu.org/licenses/gpl-3.0.en.html).
