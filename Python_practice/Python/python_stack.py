class Stack:
    def __init__(self,max_size):
        self.stack_list=[]
        self.max_size=max_size
    def push(self,element):
        if (self.isFull()):
            print("Can't push.")
        else:
            self.stack_list.append(element)
    def pop(self):
        if (self.isEmpty()):
            print("Can't pop.")
        else:
            return (self.stack_list.pop())
    def top(self):
        if (self.isEmpty()):
            print("Can't top.")
        else:
            return (self.stack_list[-1])
    def view_stack(self):
        print(self.stack_list)
    def isFull(self):
        if len(self.stack_list)>=self.max_size:
            return True
        else:
            return False
    def isEmpty(self):
        if len(self.stack_list)==0:
            return True
        else:
            return False


