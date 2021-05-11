[![PyPI Version][pypi-image]][pypi-url]


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
python3 icerok_server/main.py
```

### Publish in TestPyPi

```
flit publish --repository pypitest
```

### Publish package

* Increase version number in `icerok_server/__init__.py`
* Execute:
```
flit publish
```

<!-- Badges -->
[pypi-image]: https://img.shields.io/pypi/v/icerok_server
[pypi-url]: https://pypi.org/project/icerok_server/
[build-image]: https://github.com/nalgeon/podsearch-py/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/nalgeon/podsearch-py/actions/workflows/build.yml