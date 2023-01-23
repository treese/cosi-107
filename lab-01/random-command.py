import random
import time

bytes_sent = 31

try:
    import psutils
    # Get the stats of bytes sent
    bytes_sent = psutil.net_io_counters()
except ImportError:
    pass

# Get the current time in milliseconds
current_time = int(time.time() * 1000)

# Combine the IP address and time in milliseconds to create a seed
# value

seed_value = bytes_sent + current_time

random.seed(seed_value)

word_list = ["ls", "rm", "mkdir", "rmdir", "cd", "wget", "pwd", "ln",
             "sudo", "chmod", "umask", "ping", "cut", "sort", "which", "grep",
             "whereis", "finger", "w", "who", "whoami", "last", "file", "strings",
             "top", "ps", "nice", "nohup", "kill", "signal", "more", "less",
             "ifconfig", "arp", "nslookup", "cat", "uname", "history", "netstat",
             "curl", "ifconfig", "traceroute", "shred", "dig", "man", "lsof",
             "whois", "crontab", "nc", "uniq", "id", "groups", "df", "du", "dd",
             "openssl", "tar", "clear", "touch"]

random_word = random.choice(word_list)

print(random_word)
