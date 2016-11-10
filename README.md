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

`einder.Client` controls the set-top box by sending bytes. These bytes
represent the buttons of a remote control. You can find all supported keys
in [`einder.keys`][keys]. The example shows how to send keys.

```python
import time

from einder import Client
from einder import keys

# Replace IP with the IP of your set-top box. The port parameter is optional,
# by default its 5900.
c = Client("192.168.1.245", port=5900)

c.power_on()

# Wait a few seconds the set-top box to start.
time.sleep(5)

# Select channel 501.
c.send_key(keys.NUM_5)
c.send_key(keys.NUM_0)
c.send_key(keys.NUM_1)

# For selecting a channel einder.Client offers a small helper function.
c.select_channel(501)

# No watch some TV...

c.power_off()
c.disconnect()
```

The `einder.Client` can also be used as a context manager:

```python
from einder import Client

with Client("192.168.1.245") as c:
    c.select_channel(501)
```

## License

This software is licensed under the [MIT license][license].

[horizoncontrol]: https://github.com/kuijp/horizoncontrol
[keys]: einder/keys.py
[kuijp]: https://github.com/kuijp
[license]: LICENSE
