## Summary  
Merging two sorted lists can be achieved with a couple of if statements and a loop.  
However, the code becomes difficult to maintain for more than 2 lists.  

Sometimes it's better to just used a tried and tested data structure like a queue.  

Example input:  
[[1,4,5],[1,3,4],[2,6]]


## Code:  

**Initial notes**
we want complexity of O(m+n) for m + n elements, O(m+n+o) for m+n+o elements etc.  
problems:  
we can't access all the nodes at once  
above 2 lists, simple splicing will create too many "if" statements  



Complexity Analysis (from Leetcode)  

Time complexity: O(N log k) where `k` is the number of linked lists.  
The comparison cost will be reduced to O(log k) for every pop and insertion to priority queue. But finding the node with the smallest value just costs O(1) time.  
There are N nodes in the final linked list.  

Space complexity :  
O(n) Creating a new linked list costs O(n) space.  
O(k) The code above present applies in-place method which cost O(1) space. And the priority queue (often implemented with heaps) costs O(k) space (it's far less than N in most situations).  

---

Lessons learned:  
- it's worth talking about the operations a given data structure does well: Does it sort fast? Does it give you the smallest element fast?  
