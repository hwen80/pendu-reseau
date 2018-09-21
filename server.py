#!/usr/bin/env python
# coding: utf-8
import socket, pickle, struct

def create_socket():
    s = socket.socket()
    host = "0.0.0.0"
    port = 12345
    s.bind((host,port))
    s.listen(5)
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
