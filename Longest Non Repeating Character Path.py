"""
    You are given a tree consisting of N nodes, numbered from 0 to N-1.
    Each node contains one of the letters 'a' or 'b'.
    The tree is represented as an array A of length N. A[K] (for K from 0 to N-1)
    denotes the parent of the K-th node. Node 0 is the root node and does not have
    a parent, so the value corresponding to it in array A will always be -1.
    Letters in nodes are represented as a string S. S[K] (for K from 0 to N-1) denotes
    the letter in K-th node.

    For Example:
    S = "abbab"
    A = [-1,0,0,0,2]

    Task: Find the number of vertices on the longest path in the tree such that no pair
          of adjacent vertices on the path would contain the same letter.

    Examples:
        1.  S = "ab"
            A = [-1,0]
            result = 2
        2.  S = "abbab"
            A = [-1,0,0,0,2]
            result = 3
        3.  S = "abab"
            A = [-1,2,0,1]
            result = 2
"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, A):
    # write your code in Python 3.6
    # res = [1]
    # for i in range(1,len(A)):
    #     if S[i] != S[A[i]]:
    #         res.append(res[A[i]]+1)
    #     else:
    #         res.append(1)
    # return max(res)

    graph = {}
    for i in range(len(A)):
        if S[i]==S[A[i]] or i == -1 or A[i] == -1:
            continue
        if A[i] in graph:
            graph[A[i]].add(i)
        else:
            graph[A[i]] = set([i])
        if i in graph:
            graph[i].add(A[i])
        else:
            graph[i] = set([A[i]])
    # print(graph)

    seen = set()

    def dfs(v):
        if v in seen:
            return 0
        seen.add(v)
        maxL = 0
        for e in graph[v]:
            temp = dfs(e)
            if maxL < temp + 1:
                maxL = temp + 1
        return maxL

    res = 0
    for i in graph.keys():
        d = dfs(i)
        res = d if d > res else res
        seen = set()
    return res