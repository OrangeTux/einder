import time

# A little nap is required so the test server can process requests and add them
# to its requests list before we check this list.
sleep = 0.01


def test_toggle_power(server, client):
    client.toggle_power()

    time.sleep(sleep)
    assert server.requests == [
        b'\x04\x01\x00\x00\x00\x00\xe0\x00', b'\x04\x00\x00\x00\x00\x00\xe0\x00'
    ]


def test_select_channel(server, client):
    client.select_channel(501)

    time.sleep(sleep)
    assert server.requests == [
        # key.NUM_5
        b'\x04\x01\x00\x00\x00\x00\xe3\x05', b'\x04\x00\x00\x00\x00\x00\xe3\x05',
        # key.NUM_0
        b'\x04\x01\x00\x00\x00\x00\xe3\x00', b'\x04\x00\x00\x00\x00\x00\xe3\x00',
        # key.NUM_1
        b'\x04\x01\x00\x00\x00\x00\xe3\x01', b'\x04\x00\x00\x00\x00\x00\xe3\x01',
    ]
