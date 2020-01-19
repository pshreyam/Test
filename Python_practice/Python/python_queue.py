class Queue:
    
    def __init__(self,max_queue_size):
        self.max_queue_size=max_queue_size
        self.queue_list=[]
    
    def enqueue(self,element):
        if not (self.isFull()):
            self.queue_list.insert(0,element)
        else:
            print ("Cannot enqueue.")
    
    def dequeue(self):
        if not (self.isEmpty()):
            return self.queue_list.pop()
        else:
            print ("Cannot dequeue.")

    def isEmpty(self):
        if len (self.queue_list)==0:
            return True    
    
    def isFull(self):
        if len (self.queue_list)>=self.max_queue_size:
            return True
    
    def view_queue(self):
        print (self.queue_list)



##Application of Queue
q1=Queue(5)
q1.enqueue("1")
q1.enqueue("2")
q1.enqueue("3")
q1.enqueue("4")
q1.enqueue("5")
q1.view_queue()
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
q1.view_queue()
q1.dequeue()
