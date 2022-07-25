"""
.tsf file reverse engineering


jh, july 2022
"""

import sys

def parse(fn):
    with open(fn, 'rb') as f:
        hdr = f.read(281)
        #assert hdr[-1]==b"\x46", f"{hdr}"
        assert hdr[-1]==b"F", f"{hdr[-5:]}"
        

if __name__=="__main__":
    
    parse(sys.argv[1])


    
