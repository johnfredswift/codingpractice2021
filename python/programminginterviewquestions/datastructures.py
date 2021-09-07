class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None    

    def ListPrint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval



# list = ds.SLinkedList()
# list.headval = ds.Node("First")
# secondElement = ds.Node("Second")
# thirdElement = ds.Node("Third")

# #Links the first element to the headed 
# list.headval.nextval = secondElement

# # Link second Node to third node
# thirdElement.nextval = thirdElement

# list.ListPrint()