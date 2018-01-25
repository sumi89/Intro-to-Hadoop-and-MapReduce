import sys

path = None
count = 0
maxpath = None
maxcount = 0

for line in sys.stdin:
    thispath = line.strip()

    ## 'path' means first path
    if path and path == thispath:
        count += 1

    else:
        if maxcount < count:
            maxcount = count
            maxpath = path

        path = thispath
        count = 1

if path != None:
    if maxcount < count:
        maxcount = count
        maxpath = path

print maxpath, "\t", maxcount
