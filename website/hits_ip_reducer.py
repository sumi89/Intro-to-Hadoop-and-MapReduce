import sys

count = 0

for line in sys.stdin:
    thisip = line.strip()

    if thisip == '10.99.99.186':
        count += 1

print count


## another way
# import sys

# number_of_visit = 0

# for line in sys.stdin:
   # if line.strip() == '10.99.99.186':
        # number_of_visit += 1

# print number_of_visit