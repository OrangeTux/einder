#!/usr/bin/env python
from einder import Client

with Client('192.168.1.245') as c:
    c.toggle_power()
