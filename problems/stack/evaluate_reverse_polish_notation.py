from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        ops = {'+', '-', '*', '/'}
        #  ["1","3","+","3","/","4","-"]
        # ["4","2","3","13","5","/","+"]
        # 4, 3 [/]
        # last two
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                elif token == "/":
                    result = int(first / second)
                stack.append(result)

        return int(stack.pop())
