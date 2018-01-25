import sys

def mapper():

    for line in sys.stdin:
        data = line.replace('[','').replace(']','').replace('"','').strip()

        if len(data) == 10:
            IP, ID, username, datetime, timezone, method, path, qspr, code, size = data
            print "{0}".format(ip)