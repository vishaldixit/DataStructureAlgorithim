import time


inputArray = ['nemo' for i in range(100)]

def findingNemo(array):
  t1 = time.time()
  print(t1)
   
  for first in array:
    if first == "nemo":
      print("Found nemo")

  t2 = time.time()
  
  print("Total time taken-{}".format((t2-t1)))


#findingNemo(inputArray)

boxes = [1,2,3,4,5,6]

def logFirstTowBoxes(boxes):
  print(boxes[0])
  print(boxes[1])

logFirstTowBoxes(boxes)