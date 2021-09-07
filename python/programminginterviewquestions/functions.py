def PrintHello():
    print("Hello World!")

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