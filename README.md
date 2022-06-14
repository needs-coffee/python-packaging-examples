# Packaging with python

For a guide in packaging for python see - https://packaging.python.org/ and https://py-pkgs.org/01-introduction
There are currently several methods/tools to produce a python package. This repo contains example projects of currently accepted methods of producing python packages.

### Notes:

- Don't use eggs - old outdated binary format.
- PEP-517 is the standard of the modern build system.
- All the examples below use a hello_**world project to demonstrate different methods.
- **`setup.py` does not need to exist** - only needed if you want to build by invoking this directly or using legacy tools. This file is required using some old legacy tools (i.e. distutils) but should not be be required by any system using a PEP517 compliant build system. i.e. `build` package.
- **if `pyproject.toml` is not present or the build system is not defined** - the build system defaults to legacy mode (using setuptools)
- the most modern method of using setuptools is with only pyproject.toml to define all project metadata as per PEP 621. (example 04)
- all of the below can be built with `python -m build`
- Folders in this directory are numbered from oldest to newest standard.
- a stub `setup.py` is still needed when using c extensions or editable installs.

| Packaging style | Buildsystem   | Notes | 
| ----------------------------- | --------------------- | --------------------- |
| 01_setuppy_legacy             | setuptools (implicit) | Oldest format that still produces usable packages. All metadata defined in `setup.py` and setuptools is called implicitly. `Setup.py` is not recommended as it introduces circular dependencies                                                                                                                             |
| 02_setupcfg_legacy            | setuptools (implicit) | Alternative to above using `setup.cfg` instead of `setup.py`. `setup.py` may still be required as a stub when invoking the buildsystem. setuptools is called implictly like the above by not defining an alternative. [Reference](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)                 |
| 03_setupcfg_setuptools_modern | setuptools (explicit) | same as above but with setuptools explicitly defined as buildsystem by `pyproject.toml`. `Setup.cfg` and project remain the same. [Reference](https://setuptools.pypa.io/en/latest/userguide/declarative_config.html)                                                                                                      |
| 04_pyproject_setuptools       | setuptools (explicit) | metadata moved from `setup.cfg` to `pyproject.toml`. This is preferred as per PEP-621 but remains subject to changes. Setuptools config page show a method of getting the current version from the source control using `setuptools-scm` [Reference](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html) |
| 05_poetry                     | poetry                | uses poetry for package, venv, and build management. poetry metadata and buildsystem are defined in `pyproject.toml`. [Reference](https://python-poetry.org/docs/pyproject/)                                                                                                                                               |

### Licence
This code is licensed under the GNU GPLv3 Licence. Included dependencies and code are covered by their own licence - check project pages for details.

```
This program is free software: you can redistribute it and / or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY
without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see < https: // www.gnu.org/licenses/>.
```