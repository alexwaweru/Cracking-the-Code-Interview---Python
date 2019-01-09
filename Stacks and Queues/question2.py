class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    
     def min_element(self):
         min_el = self.items[0]
         pos = 1
         while pos <= self.size()-1:
             if self.items[pos] < min_el:
                 min_el = self.items[pos]
             else:
                 pos = pos + 1
        
         return min_el


new_stack = Stack()
new_stack.push(100)
new_stack.push(101)
new_stack.push(145)
new_stack.push(19)
new_stack.push(1789)
new_stack.push(190)
new_stack.push(23)
new_stack.push(10)
new_stack.push(1001)
print(new_stack.min_element())

# Output:
# 10