#명령프롬프트 백준 1032번 브론즈1

n = int(input())
lists = [input() for i in range(n)]
ans = list(lists[0])
for i in range(1, n):
    for count in range(len(ans)):
        if lists[i][count] != ans[count] and ans[count] != '?':
            ans[count] = '?'

print(''.join(ans))