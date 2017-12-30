import zlib
import struct
import numpy as np

def adler32(data):
    return zlib.adler32(data) & 0xFFFFFFFF

def crc32(data):
    return zlib.crc32(data) & 0xFFFFFFFF

def sum32(data):
    return np.sum(np.fromstring(data, dtype=np.uint8)) & 0xFFFFFFFF

def fletcher32(data, init=0xFFFF):
    c0 = init
    c1 = init
    checksum = 0
    if len(data) % 2:
        data += '\x00'

    shorts = np.fromstring(data, dtype=np.uint16)
    for i in xrange(shorts.size):
        c0 += shorts[i]
        c1 += c0
        if (i % 360) == 0:
            c0 = (c0 & 0xFFFF) + (c0 >> 16)
            c1 = (c1 & 0xFFFF) + (c1 >> 16)

    c0 = (c0 & 0xFFFF) + (c0 >> 16)
    c1 = (c1 & 0xFFFF) + (c1 >> 16)
    checksum = (c1 << 16) | c0

    return checksum & 0xFFFFFFFF;
        
        
    
    
