# Challenge Summary
<!-- Description of the challenge -->
Implement a breadth-first traversal on a graph.

Write the following method for the Graph class:
breadth first
Arguments: Node
Return: A collection of nodes in the order they were visited.
Display the collection

## Whiteboard Process
<!-- Embedded whiteboard image -->
![](../../img/BFG.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Complexity:
- O(N^2) for time
-  O(N) For space
## Solution
<!-- Show how to run your code, and examples of it in action -->
    def breadth_first(self, node):
            queue = Queue()
            visited = set()
            output = []
            visited.add(node)
            queue.enqueue(node)
            while len(queue):
                cuttent_v = queue.dequeue()
                output.append(cuttent_v)
                neighbors = self.get_children(cuttent_v)
                for edge in neighbors:
                    vert = edge.vertex
                    if vert not in visited:
                        visited.add(vert)
                        queue.enqueue(vert)
            return output
