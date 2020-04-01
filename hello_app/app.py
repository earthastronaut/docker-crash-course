import time
import sys

for _ in range(100):
    print('Hello SLC Python!')
    sys.stdout.write('....')
    sys.stdout.flush()
    time.sleep(1)
