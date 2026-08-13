class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch not in "+-/*":
                stack.append(int(ch))
            else:

                a=stack.pop()
                b= stack.pop()

                if ch == "+":
                    stack.append(b + a)
                elif ch == "-":
                     stack.append(b - a)
                elif ch == "*":
                     stack.append(int(b * a))
                else:
                     stack.append(int(b / a))

        return stack[-1]   