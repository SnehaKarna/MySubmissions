class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = list(zip(position, speed))

        # Sort by position
        cars.sort()

        stack = []

        # Process from closest to target
        for pos, spd in cars[::-1]:

            time = (target - pos) / spd

            # New fleet
            if not stack or time > stack[-1]:
                stack.append(time)

            # Else: joins fleet ahead (do nothing)

        return len(stack)