import heapq

class PriorityQueue:
    """
    Simple implementation of a priority queue. 
    """

    def __init__(self):
        self.__heap: list = []

    def push(self, t: tuple):
        """
        Adds an element to the queue.

        t: tuple
            Element to be added, preferebly a tuple. The elements position will be
            determined by comparing the tuples elements to existing elements in the queue.
            In case of a tie the tuples the next element will be considered as a tie breaker.
        """
        heapq.heappush(
            self.__heap, 
            t
        )

    def pop(self):
        """
        Pops the element with the minimum metric.
        """
        return heapq.heappop(self.__heap)

    def is_element(self, element, key=lambda x: x):
        """
        Checks whether a given element is part of the queue. A custom key may be
        specified.

        element
            Element to check for the first occurence in the queue.
        key
            Custom key function for determining equality.
        """
        for element in self.__heap:
            if key(element) == e:
                return True
        return False

    def __len__(self):
        return len(self.__heap)

    def __str__(self):
        return str(self.__heap)