class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            zipped_list = list(zip(position, speed))
            zipped_list.sort(reverse=True) # sorted reverse order by first element postion
            stack = []

            for index, (p, s) in enumerate(zipped_list):
                time = (target - p) / s  # find the time for each car
                if not stack or stack[-1] < time:
                    stack.append(time)
            return len(stack)

