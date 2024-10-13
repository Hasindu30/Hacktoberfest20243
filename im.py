import heapq
 
 
def find_n_largest_elements(lst, N):
    heap = lst
    return heapq.nlargest(N, heap)
 
 
# Test the function with given inputs
lst = [4, 5, 1, 2, 9]
N = 2
print(find_n_largest_elements(lst, N))
 
lst = [81, 52, 45, 10, 3, 2, 96]
N = 3
print(find_n_largest_elements(lst, N))
