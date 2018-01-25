
def mapper():

    for line in sys.stdin:
        ## extract the log fields
        data = line.replace('[','').replace(']','').replace('"','').split(' ')
        ## data = (IP, ID, username, dt [date+time], timezone, method, path,
            ## qspr [query-string + protocol/request], status, size)
        if len(data) == 10:
            IP, ID, username, datetime, timezone, method, path, qspr, code, size = data
            print "{0}".format(path)
