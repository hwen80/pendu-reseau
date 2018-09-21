#!/usr/bin/env python
# coding: utf-8
import socket, pickle, struct

def create_socket(addr):
    s = socket.socket()
    port = 12345
    s.connect((addr, port))
    return s

def msg_send(s, msg):
    msg = struct.pack('>I', len(msg)) + msg
    s.sendall(msg)

def msg_rec(s):
    raw_msg_len = recvall(s, 4)
    if not raw_msg_len:
        return None
    msg_len = struct.unpack('>I', raw_msg_len)[0]
    return recvall(s, msg_len)

def recvall(s, n):
    data = b''
    while len(data) < n:
        packet = s.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

s = create_socket('10.0.8.1')
data = []
input = ""
while not "exit" in data:
    data = pickle.loads(msg_rec(s))
    print(data[0])
    if "input" in data:
        input = raw_input()
        msg = pickle.dumps(input)
        msg_send(s, msg)
print("Fin de partie.")
s.close()
