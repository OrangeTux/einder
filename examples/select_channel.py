#!/usr/bin/env python
from einder import Client

with Client('192.168.1.245') as c:
    c.select_channel(501)
