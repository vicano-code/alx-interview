#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered 
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
- Prototype: def canUnlockAll(boxes)
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
   -There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""

def canUnlockAll(boxes):
  boxesSize = len(boxes)

  # remove keys from boxes with its own key inside
  # and concatenate the lists in boxes list
  key = 0
  newList = []
  for keyList in boxes:
    if key in keyList:
      keyList.remove(key)
    newList = [*newList, *keyList]
    key += 1
  
  # sort the newList
  sortedNewList = sorted(newList)

  # Get unique List using set
  uniqueKeyList = set(sortedNewList)

  # Check if keys for all boxes are present in uniqueKeyList
  # note that first box boxes[0] is unlocked so start from key 1
  for i in range(1, boxesSize):
    if i not in uniqueKeyList:
      return False
  
  return True