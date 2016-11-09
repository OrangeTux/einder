import socket
import struct

from einder import keys
from einder.exceptions import AuthenticationError


class Client:
    """ The set-top box Client. """
    def __init__(self, ip, port=5900):
        self.ip = ip
        self.port = port

        self.con = None

        self.connect()
        self.authorize()

    def connect(self):
        """ Connect sets up the connection with the Horizon box. """
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.con.connect((self.ip, self.port))

    def disconnect(self):
        """ Disconnect closes the connection to the Horizon box. """
        if self.con is not None:
            self.con.close()

    def authorize(self):
        """ Use the magic of a unicorn and summon the set-top box so it listens
        to us.

                            /
                       ,.. /
                     ,'   ';
          ,,.__    _,' /';  .
         :','  ~~~~    '. '~
        :' (   )         )::,
        '. '. .=----=..-~  .;'
         '  ;'  ::   ':.  '"
           (:   ':    ;)
            \\   '"  ./
             '"      '"

        Seriously, I've no idea what I'm doing here.
        """
        # Read the version of the set-top box and write it back. Why? I've no
        # idea.
        version = self.con.makefile().readline()
        self.con.send(version.encode())

        # The set-top box returns with 2 bytes. I've no idea what they mean.
        self.con.recv(2)

        # The following reads and writes are used to authenticate. But I don't
        # fully understand what is going on.
        self.con.send(struct.pack('>B', 1))
        msg = self.con.recv(4)
        response = struct.unpack(">I", msg)

        if response[0] != 0:
            raise AuthenticationError()

        # Dunno where this is good for. But otherwise the client doesn't work.
        self.con.send(b'0')

    def send_key(self, key):
        """ Send a key to the Horizon box. """
        cmd = struct.pack(">BBBBBBH", 4, 1, 0, 0, 0, 0, key)
        self.con.send(cmd)

        cmd = struct.pack(">BBBBBBH", 4, 0, 0, 0, 0, 0, key)
        self.con.send(cmd)

    def toggle_power(self):
        """ Toggle the power state of the set-top box. """
        self.send_key(keys.POWER)

    def select_channel(self, channel):
        """ Select a channel.

        :param channel: Number of channel.
        """
        for i in str(channel):
            key = int(i) + 0xe300
            self.send_key(key)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.disconnect()
