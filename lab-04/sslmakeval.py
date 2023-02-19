#!/usr/bin/env python3
#
# Compute a challenge value to be guessed

import time
import math
import sslkey

# value obtained from time.time at some point
mytimeval = 1675880328.585115

frac, seconds = math.modf(mytimeval)
seconds = int(seconds)
microseconds = int(frac * 1000000)

print(f"Seconds: {seconds}")
print(f"Microseconds: {microseconds}")

# Generate the corresponding challenge value
rc = sslkey.RNGC(seconds=seconds, microseconds=microseconds)
rc.create_key()
print(f"Challenge: {rc.challenge.hex()}")
print(f"Secret key: {rc.secret_key.hex()}")


# Do it again
print()

# value obtained from time.time at some point
mytimeval = 1675914877.862087

frac, seconds = math.modf(mytimeval)
seconds = int(seconds)
microseconds = int(frac * 1000000)

print(f"Seconds: {seconds}")
print(f"Microseconds: {microseconds}")

# Generate the corresponding challenge value
rc = sslkey.RNGC(seconds=seconds, microseconds=microseconds)
rc.create_key()
print(f"Challenge: {rc.challenge.hex()}")
print(f"Secret key: {rc.secret_key.hex()}")
