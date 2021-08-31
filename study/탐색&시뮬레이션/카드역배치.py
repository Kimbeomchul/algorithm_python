card = [i for i in range(1,21)]
input_data = []
for _ in range(10):
    input_data.append(list(map(int,input().split())))

for i,j in input_data:
    temp = card[i-1:j]
    card[i-1:j] = temp[::-1]
print(card)
