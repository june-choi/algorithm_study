# 계속 오류가 발생하는 부분이 있어 구글링 통해 코드 수정했습니닷 ...

while(True):
    str = input()
    stack = [] 

    if str == '.': 
        break

    for s in str:
        if s == '(' or s == '[': 
            stack.append(s)
        elif s == ')': 
            if len(stack) != 0 and stack[-1] == '(': 
                stack.pop()
            else: 
                stack.append(s)
                break
        elif s == ']': 
            if len(stack) != 0 and stack[-1] == '[': 
                stack.pop()
            else: 
                stack.append(s)
                break

    if len(stack) == 0: 
        print('yes')
    else: 
        print('no')