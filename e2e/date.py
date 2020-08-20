import time

input = "Wed Aug 05 04:21:47 UTC 2020"
output = time.strptime(input, '%a %b %d %H:%M:%S %Z %Y')
print(output)

# default formatting - "%a %b %d %H:%M:%S %Y"
print(time.strptime('Wed Sep 19 14:55:02 2018'))