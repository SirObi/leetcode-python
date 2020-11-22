Think of a line first.
Given a list of points on a straight line, get k closest.
We can actually map the two coordinates of the point onto
one point in 1D space.

We have to look at all the points in the list, so we might as
well apply the function to all of them.


Lessons learned:
It’s worth checking if you can map your input to a smaller dimension before computation (e.g. 2D to 1D, grid to line etc)
minHeap pops the smallest element by default
You can reverse a minHeap by multiplying elements by -1 before pushing


Alternative solution (though heap is a good solution, too):
Could have just sorted it, like so:

```
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
```
