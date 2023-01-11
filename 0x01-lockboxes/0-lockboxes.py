#!/usr/bin/python3
'''defines canUnlockAll function'''


def canUnlockAll(boxes):
    '''
    Args:
        boxes: list
    returns:
        True or False
    '''
    # Check if the input is valid
    if not boxes:
        return False
    # Set to keep track of which boxes have been opened
    opened = set()
    # Queue for the keys
    keys = []
    # Add the keys in the first box to the queue
    # and mark the first box as opened
    keys.extend(boxes[0])
    opened.add(0)
    # BFS loop
    while keys:
        # Get the next key
        key = keys.pop(0)
        # Check if the key is a valid box index
        # and if the box has not been opened
        if 0 <= key < len(boxes) and key not in opened:
            # Add the keys in the box to the queue
            keys.extend(boxes[key])
            # Mark the box as opened
            opened.add(key)
    # Return True if all boxes have been opened, else return False
    return len(opened) == len(boxes)
