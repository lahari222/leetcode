class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            elif i=='+' and len(stack)>1:
                second=stack.pop()
                first=stack.pop()
                result=first+second
                stack.append(result)
            elif i=='-' and len(stack)>1:
                second=stack.pop()
                first=stack.pop()
                result=first-second
                stack.append(result)
            elif i=='*' and len(stack)>1:
                second=stack.pop()
                first=stack.pop()
                result=first*second
                stack.append(result)
            else:
                second=stack.pop()
                first=stack.pop()
                result=int(first/second)
                stack.append(result)
        return stack[-1]
        