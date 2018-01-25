def reducer():

    maxSale = 0
    oldKey = None

    ## read standard input line by line
    for line in sys.stdin:
        ## strip off extra whitespace, split on tab and put the data in an array
        data = line.strip().split("\t")

        if len(data) != 2:
            continue

        thisKey, thisSale = data
        thisSale = float(thisSale)

        ## if it's a new store (and not the first store)
        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, maxSale)
            oldKey = thisKey
            maxSale = thisSale

        ## if it's the same store
        else:
            oldKey = thisKey
            if thisSale > maxSale:
                maxSale = thisSale


    if oldKey != None:
        print "{0}\t{1}".format(oldKey, maxSale)


