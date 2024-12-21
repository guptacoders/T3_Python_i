# Stacks and Queues. Write a class SQ that defines a data structure that can behave as both a queue (FIFO) or a stack (LIFO), 
# There are five methods that should be implemented:
# 1.	make a constructor with a valid parameter 
# 2.	shift() returns the first element and removes it from the list. Also, use the custom(raise) exception in this method.
# 3.	unshift() "pushes" a new element to the front or head of the list
# 4.	push() adds a new element to the end of a list
# 5.	pop() returns the last element and removes it from the list
# 6.	remove() returns the maximum element of the list and removes it from the list.
# 7.	Create the object and call all methods of the SQ class.

class SQ:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = data

    def shift(self):
        if len(self.data) == 0:
            raise Exception("The list is empty. Cannot shift.")
        return self.data.pop(0)

    def unshift(self, value):
        self.data.insert(0, value)

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            raise Exception("The list is empty. Cannot pop.")
        return self.data.pop()

    def remove(self):
        if len(self.data) == 0:
            raise Exception("The list is empty. Cannot remove the max element.")
        max_element = max(self.data)
        self.data.remove(max_element)
        return max_element
try:
    sq = SQ([])

    sq.push(9)
    print("After push:", sq.data)

    sq.unshift(0)
    print("After unshift:", sq.data)

    shifted_element = sq.shift()
    print("Shifted element:", shifted_element)
    print("After shift:", sq.data)

    popped_element = sq.pop()
    print("Popped element:", popped_element)
    print("After pop:", sq.data)

    max_element = sq.remove()
    print("Removed max element:", max_element)
    print("After remove:", sq.data)

except Exception as e:
    print(e)
