# Stacks and Queues
<!-- Short summary or background information -->
### Stack:
A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

### Queue
A Queue is a linear structure that follows a particular order in which the operations are performed.

## Challenge
<!-- Description of the challenge -->
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
- This object should be aware of a default empty value assigned to top when the stack is created.
- Define a method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
- Define a method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
- Should raise exception when called on empty stack
- Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
Should raise exception when called on empty stack
- Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
- Create a Queue class that has a front property. It creates an empty - Queue when instantiated.
This object should be aware of a default empty value assigned to front when the queue is created.
- Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
- Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
- Should raise exception when called on empty queue

- Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
Should raise exception when called on empty queue
- Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### Big(O) for Stack Operations:
- Push O(1)
- pop O(1)
- Peek O(1)
- IsEmpty O(1)

### Big(O) for Queue Operations:
- Enqueue O(1)
- Dequeue O(1)
- Peek O(1)
- IsEmpty O(1)

## API
<!-- Description of each method publicly available to your Stack and Queue-->
### Common terminology for a Queue is:
- Enqueue - Nodes or items that are added to the queue.
- Dequeue - Nodes or items that are removed from the queue. If called - when the queue is empty an exception will be raised.
- Peek - When you peek you will view the value of the front Node in the - queue. If called when the queue is empty an exception will be raised.
- IsEmpty - returns true when queue is empty otherwise returns false.


### Common terminology for a stack is:
- Push - Nodes or items that are put into the stack are pushed
- Pop - Nodes or items that are removed from the stack are popped. When - you attempt to pop an empty stack an exception will be raised.
- Peek - When you peek you will view the value of the top Node in the - stack. When you attempt to peek an empty stack an exception will be raised.

- IsEmpty - returns true when stack is empty otherwise returns false.