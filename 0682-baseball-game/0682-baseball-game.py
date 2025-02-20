class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in range(0,len(operations)):
            if operations[i]=='C':
                deleted_ele=stack.pop(-1)
            elif operations[i]=='D':
                double_ele=(stack[-1])*2
                stack.append(double_ele)
            elif len(stack)>0 and operations[i]=='+':
                adding=(stack[-1])+int(stack[-2])
                stack.append(adding)
            else:
                stack.append(int(operations[i]))
        return sum(stack)
        