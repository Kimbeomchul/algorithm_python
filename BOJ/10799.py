#백준 10799 쇠막대기 한국정보올림피아드 기출

n = list(input())

count = 0
stack = []

for i in range(len(n)):
    if n[i] == '(':
        stack.append('(')

    else:
        if n[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
print(count)