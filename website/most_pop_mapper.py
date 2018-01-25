import sys

for line in sys.stdin:
    data = line.replace('[','').replace(']','').replace('"','').split(' ')

    if len(data) == 10 :
        IP, ID, username, datetime, timezone, method, path, qspr, code, size = data
        print "{0}".format(path.replace('http://www.the-associates.co.uk',''))