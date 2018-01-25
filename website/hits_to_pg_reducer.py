import sys

count = 0

for line in sys.stdin:
    thispath = line.strip()

    if thispath == '/assets/js/the-associates.js':
        count += 1

print count



## another way
# import sys

# number_of_visit = 0

# for line in sys.stdin:
    # if line.strip() == '/assets/js/the-associates.js':
        # number_of_visit += 1

# print number_of_visit