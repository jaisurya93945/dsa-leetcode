class DSU:

    def __init__(self):
        self.parent = {}
        self.size = {}

    def add(self, x):
        self.parent[x] = x
        self.size[x] = 1

    def find(self, x):

        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        px = self.find(x)
        py = self.find(y)

        if px == py:
            return

        if self.size[px] < self.size[py]:
            px, py = py, px

        self.parent[py] = px
        self.size[px] += self.size[py]


class Solution:

    def longestConsecutive(self, nums):

        dsu = DSU()

        for num in nums:
            dsu.add(num)

        for num in nums:

            if num + 1 in dsu.parent:
                dsu.union(num, num + 1)

        answer = 0

        for root in dsu.parent:
            answer = max(
                answer,
                dsu.size[dsu.find(root)]
            )

        return answer
