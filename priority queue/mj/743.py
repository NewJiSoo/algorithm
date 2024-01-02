# https://leetcode.com/problems/network-delay-time/description/?orderBy=most_votes

from collections import defaultdict
import heapq


class Solution(object):
    def networkDelayTime(self, times, n, k):
        # graph = {}
        # for time in times:
        #     if time[0] not in graph:
        #         graph[time[0]] = []
        #     graph[time[0]].append((time[2], time[1]))

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        costs = {}
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_v))
        print(costs)
        for i in range(1, n + 1):
            if i not in costs:
                return -1
        return max(costs.values())


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

s = Solution()
print(s.networkDelayTime(times, n, k))
