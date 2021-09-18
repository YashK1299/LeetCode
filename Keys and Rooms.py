"""
    There are n rooms labeled from 0 to n - 1 and you start in the room 0. All the rooms labeled from 1 to n are
    initially locked and you cannot enter a locked room without having its key.
    When you visit a room, you may find a set of distinct keys in it and you can use them to open locked rooms and
    enter them.
    You can visit the same room any number of times and the goal is to visit all the n rooms.
    Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true
    if you can visit all the rooms, or false otherwise.

    Example 1:
        Input: rooms = [[1],[2],[3],[]]
        Output: true
        Explanation:
        We start in room 0, and pick up key 1.
        We then go to room 1, and pick up key 2.
        We then go to room 2, and pick up key 3.
        We then go to room 3.
        Since we were able to go to every room, we return true.

    Example 2:
        Input: rooms = [[1,3],[3,0,1],[2],[0]]
        Output: false
        Explanation: We can not enter the room with number 2.

    Constraints:
        n == rooms.length
        2 <= n <= 1000
        0 <= rooms[i].length <= 1000
        1 <= sum(rooms[i].length) <= 3000
        0 <= rooms[i][j] < n
        All the values of rooms[i] are unique.
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
            DFS Approach:
                T(n) = O(V+E)
                S(n) = O(V)
        """
        seen = {0}
        stack = [0]
        while stack:
            i = stack.pop()
            for j in rooms[i]:
                if j not in seen:
                    stack.append(j)
                    seen.add(j)
        return len(seen) == len(rooms)
