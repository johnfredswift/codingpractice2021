import functions as fn

fn.PrintHello()

list = fn.SLinkedList()
list.headval = fn.Node("First")
secondElement = fn.Node("Second")
thirdElement = fn.Node("Third")

#Links the first element to the headed 
list.headval.nextval = secondElement

# Link second Node to third node
thirdElement.nextval = thirdElement

list.ListPrint()
