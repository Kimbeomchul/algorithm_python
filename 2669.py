#백준 2669번 직사각형 네개의 합집합의 면적 구하기  // 한국정보올림피아드 기출

count =0
lists = [[0 for _ in range(101)]for _ in range(101)]
for _ in range(4):
    q,w,e,r = list(map(int,input().split()))
    for i in range(w,r):
        for j in range(q,e):
            lists[i][j] = 1

for i in lists:
    count += sum(i)

print(count)