import random
import time


seed_value = time.time_ns()

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
