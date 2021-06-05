#단어정렬 백준 1181번 실버 5

txt = [input() for x in range(int(input()))]
txt = set(txt)
txt = list(txt)
txt.sort()
txt.sort(key=len)
for i in txt:
    print(i)


