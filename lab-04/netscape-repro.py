#!/usr/bin/env python3

import hashlib
import time

# Using global variables because the Netscape code did

seed = None                       # Must be initialized before use

def ns_mklcpr(x):
    """Fixed, unkeyed function. Presumed to be known by attacker.
    Not cryptographically relevant.
    """
    return ((0xDEECE66D * x + 0x2BBB62DC) >> 1);

# We will assume known constant values for the PID and parent PID.

def ns_create_context():
    """Rough reimplementation of 1996 Netscape RNG_CreateContext().
    No return value; sets variable seed for RNG."""
    current_time = time.time()
    current_secs = int(current_time)
    (seconds, microseconds) = (current_secs,
                               int((current_time - current_secs) * 1000000))
    pid = 1234
    ppid = 1
    a = ns_mklcpr(microseconds)
    b = ns_mklcpr(pid + seconds + (ppid << 12))
    seed = ns_MD5(a, b)

def ns_MD5(x):
    import hashlib
    m = hashlib.md5()
    m.update(a)
    m.update(b)
    m.digest()

def ns_rng_generate_random_bytes():
    x = ns_MD5(seed)
    seed = seed + 1
    return x

challenge = None
secret_key = None

def ns_create_key():
    ns_create_context()
    tmp = ns_rng_generate_random_bytes()
    tmp = ns_rng_generate_random_bytes()
    challenge = ns_rng_generate_random_bytes()
    secret_key = ns_rng_generate_random_bytes()

# Attack
# Assume pid can be found out
# Assume ppid can be found out
# Detect approximate time from packet sniffer
# Note that challenge value is sent unencrypted
