#!/usr/bin/env python3
#
# Demonstration of breaking the SSL stuff

import sys
import sslkey

def find_microsecond(second, challenge):
    """Find the microsecond given the second in
    which the challenge value was created and
    the observed challenge value (a bytestring)

    Arguments:
    seconds -- the second in which the challenge was likely created
    challenge -- the observed challenge (in bytestring form)
    """
    for i in range(0,1000000):
        rc = sslkey.RNGC(seconds=seconds, microseconds=i)
        rc.create_key()
        if rc.challenge == challenge:
            return (i, rc.secret_key)
    print("Microsecond not found!")
    sys.exit(1)

# Demo data
seconds = 1675880328
challenge = "806efae0e3ae69cbdc3867f7118c51f3"

(usec, key) = find_microsecond(seconds, bytes.fromhex(challenge))
print(usec, key.hex())
microseconds = 585114
print(f"Expected: {microseconds}")
print(f"Got: {usec}")
