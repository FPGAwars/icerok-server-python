[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]


# icerok-server
Receive data from the icerok circuits on the FPGA

## Installation

```
pip install -U icerok_server
```


## Developers

### First clone

Make sure you create a virtual environment

* Install `python3-venv`

```
sudo apt install python3-venv
```

* Create the virtual environment

```
cd icerok-server-python
python3 -m venv env
```

* Start the virtual environment
```

. env/bin/activate
```

* Install `flit`

```
pip install flit
```

### Run all the checks

```
tox
```

### Execute `icerok-server`

```
python3 app.py
```

### Publish in TestPyPi

```
flit publish --repository pypitest
```

### Publish package

* Increase version number in `icerok_server/version.py`
* Execute:
```
flit publish
```

### Release

Steps for Releasing a new version

1. Increase the version number in `icerok_server/version.py`
2. Create the release in Github
3. Automatically an action will be executed and the package will be published in Pypi

## Credits

* Thanks to [Anton Zhiyanov](https://github.com/nalgeon) for this wonderful article: [How to make an awesome Python package in 2021](https://antonz.org/python-packaging/) 

<!-- Badges -->
[pypi-image]: https://img.shields.io/pypi/v/icerok_server
[pypi-url]: https://pypi.org/project/icerok_server/
[build-image]: https://github.com/FPGAwars/icerok-server-python/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/FPGAwars/icerok-server-python/actions/workflows/build.yml