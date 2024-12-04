#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime
i = 1
while i <= 100000:
    # sleep(random.random())
    sleep(.0100)
    line = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(
            1, 255), random.randint(
            1, 255), random.randint(
                1, 255), random.randint(
                    1, 255), datetime.datetime.now(), random.choice(
                        [
                            200, 301, 400, 401, 403, 404, 405, 500]), random.randint(
                                1, 1024))
    sys.stdout.write(line)
    sys.stdout.flush()
    # print(f"'Written: {line}'", file=sys.stderr, flush=True)
    i += 1
