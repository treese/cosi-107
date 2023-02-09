import hashlib
import struct
import time

class RNGC:
    def __init__(self, seconds=None, microseconds=None, pid=1234, ppid=1):
        # Time values used in seeding
        current_time = time.time()
        self.seconds = seconds or int(current_time)
        self.microseconds = microseconds or \
                            int((current_time - self.seconds) * 1000000)
        # Other information gathered from the system
        # Usually easy to get, so defaults to constant values
        self.pid = pid
        self.ppid = ppid

        # Computed state information
        self.seed = None
        self.challenge = None
        self.secret_key = None

    def mklcpr(self, x):
        """Fixed, unkeyed function. Presumed to be known by attacker.
        Not cryptographically relevant. Included for realism.
        """
        return ((0xDEECE66D * x + 0x2BBB62DC) >> 1)

    def create_context(self, seconds=None, microseconds=None):
        """Rough reimplementation of 1996 Netscape RNG_CreateContext().
        No return value; sets variable seed for RNG."""
        a = self.mklcpr(self.microseconds)
        b = self.mklcpr(self.pid + self.seconds + (self.ppid << 12))
        self.seed = self.MD5(a, b)

    def MD5(self, *args):
        m = hashlib.md5()
        for x in args:
            m.update(str(x).encode())
        return m.digest()

    def rng_generate_random_bytes(self):
        # Not exactly the same, but close enough.
        x = self.MD5(self.seed)
        self.seed = self.MD5(self.seed, 1)
        return x

    def create_key(self):
        self.create_context()
        tmp = self.rng_generate_random_bytes()
        tmp = self.rng_generate_random_bytes()
        self.challenge = self.rng_generate_random_bytes()
        self.secret_key = self.rng_generate_random_bytes()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
