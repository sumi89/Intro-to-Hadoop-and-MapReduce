def reducer():

    salesTotal = 0
    saleCount = 0
    oldKey = None

    ## read standard input line by line
    for line in sys.stdin:
        ## strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thisKey, thisSale = data
        salesTotal += float(thisSale)
        saleCount += 1

    if oldKey != None:
        print "{0}\t{1}".format(salesTotal, saleCount)


