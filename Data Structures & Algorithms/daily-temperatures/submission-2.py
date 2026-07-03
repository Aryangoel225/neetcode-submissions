class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (temp, index)
        res = [0] * len(temperatures) # res array
        for i in range (len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, idx = stack.pop()
                dist = i - idx
                res[idx] = dist
            stack.append((temperatures[i], i))
        return res


        