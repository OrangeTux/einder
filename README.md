[![Build Status](https://travis-ci.org/OrangeTux/einder.svg?branch=master)](https://travis-ci.org/OrangeTux/einder)
[![PyPI](https://img.shields.io/pypi/v/einder.svg)](https://pypi.python.org/pypi/einder/)

# Einder

Einder is an API wrapper for the set-top boxes SMT C7400 and SMT C7401. In the
Netherlands these boxes are sold by a big Dutch cable operator under the name
Horizon Box. The name Einder is a Dutch synonym for horizon.

I'd like to thank [@kuijp][kuijp] for his work on
[horizoncontrol][horizoncontrol]. This is just a shameless Python rip off.

## Installation

```shell
$ pip install einder
```

## Usage

```python
from einder import Client

c = Client("192.168.1.245")
c.toggle_power()

```

the `einder.Client` can also be used as a context manager:

```python
from einder import Client

with Client(ip="192.168.1.245", port=5900) as c:
    c.select_channel(501)
```

## License

This software is licensed under the [MIT license][license].

[horizoncontrol]: https://github.com/kuijp/horizoncontrol
[kuijp]: https://github.com/kuijp
[license]: LICENSE
