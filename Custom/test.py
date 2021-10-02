import time
import sys
states = ["[***]", "[ **]", "[  *]", "[ **]", "[***]", "[** ]", "[*  ]", "[** ]"]
states2 = ["[|]", "[/]", "[-]", "[\]"]
count = 0
current = states2
while True:
    if count == len(current):
        count = 0
    sys.stdout.write('\r{0} Loading Program {0}'.format(current[count]))
    sys.stdout.flush()
    time.sleep(0.2)
    count = count + 1
sys.stdout.write('\n')