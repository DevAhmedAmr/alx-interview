#!/usr/bin/python3
import sys
import signal
from collections import deque

linked_list = deque()
total_size = 0
running = True


def insert_sorted(tokenized, pop=True):
    global linked_list
    new_item = {
        "status code": int(tokenized[-2]),
        "file size": int(tokenized[-1])
    }
    index = 0

    for i, item in enumerate(linked_list):
        if new_item["status code"] > item["status code"]:
            index = i
            break
        else:
            index = len(linked_list)

    linked_list.insert(index, new_item)

    # if len(linked_list) > 10 and pop:
    #     linked_list.pop()

    print(f"Inserted at index {index}, deque= {linked_list}")


def handler(signum, frame):
    global running
    running = False
    print("Exiting gracefully...")
    for token in linked_list:
        print(f"{token['status code']} : {token['file size']}")
    print(len(linked_list))
    raise KeyboardInterrupt


signal.signal(signal.SIGINT, handler)

while running:
    try:
        line = sys.stdin.readline()
        if not line:
            break

        tokenized = line.split()
        print(int(tokenized[-2]))  # Assuming this is for debugging

        if not linked_list:
            print(f"Initial insert: {tokenized[-2]}, {tokenized[-1]}")
            insert_sorted(tokenized, pop=False)
            continue

        insert_sorted(tokenized)

    except BaseException as e:
        print(f"Error: {e}")
        break

print("Program terminated.")
