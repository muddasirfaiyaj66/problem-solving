class Solution(object):
    def leastInterval(self, tasks, n):
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        max_freq = max(freq.values())
        max_freq_count = sum(1 for task in freq if freq[task] == max_freq)

        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length + max_freq_count

        return max(len(tasks), empty_slots)

sol=Solution()
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

print(sol.leastInterval(tasks,n))