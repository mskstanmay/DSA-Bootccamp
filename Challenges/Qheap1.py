# Not 100% correct 
import heapq

def heap_operations(queries):
    heap = []
    for query in queries:
        if query[0] == 1:  # Insert
            heapq.heappush(heap, query[1])
        elif query[0] == 2:  # Delete
            heap.remove(query[1])
            heapq.heapify(heap)
        elif query[0] == 3:  # Print minimum
            print(heap[0])

if __name__ == '__main__':
    q = int(input().strip())  # Number of queries
    queries = []
    
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    
    heap_operations(queries)


# Correct with less time complexity 
    
import heapq

def heap_operations(queries):
    heap = []
    deleted = set()

    for query in queries:
        if query[0] == 1:  # Insert
            heapq.heappush(heap, query[1])
        elif query[0] == 2:  # Delete
            deleted.add(query[1])
        elif query[0] == 3:  # Print minimum
            while heap[0] in deleted:
                heapq.heappop(heap)
            print(heap[0])

if __name__ == '__main__':
    q = int(input().strip())  # Number of queries
    queries = []
    
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    
    heap_operations(queries)
