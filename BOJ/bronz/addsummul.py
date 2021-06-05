#
# n = int(input())
# m = int(input())
#
# print(n+m)
# print(n-m)
# print(n*m)


# data = list(map(int,input().split()))
# adder = 0
# for i in range(len(data)):
#     adder += data[i] * data[i]
# print(adder % 10)

# n,m= map(int,input().split())
# data = list(map(int,input().split()))
#
# for i in data:
#     if i < m:
#         print(i,end=" ")

# n = int(input())
# data = []
# lists=[]
# for i in range(n):
#     x,y= list(map(int,input().split()))
#     data.append(x+y)
#     lists.append([x,y])
# for a in range(len(data)):
#     print('Case #'+str(a+1)+':',lists[a][0],'+',lists[a][1],'=',data[a])

# data = list(map(int,input().split()))
# data.sort()
# print(data[1])
# x = int(input())
# y = int(input())
# z = int(input())
# total = x * y * z
# total = str(total)
# data = [0] * 10
# for i in range(len(total)):
#     if total[i] == '0':
#         data[0] += 1
#     elif total[i] == '1':
#         data[1] += 1
#     elif total[i] == '2':
#         data[2] += 1
#     elif total[i] == '3':
#         data[3] += 1
#     elif total[i] == '4':
#         data[4] += 1
#     elif total[i] == '5':
#         data[5] += 1
#     elif total[i] == '6':
#         data[6] += 1
#     elif total[i] == '7':
#         data[7] += 1
#     elif total[i] == '8':
#         data[8] += 1
#     elif total[i] == '9':
#         data[9] += 1
#
# for a in data:
#     print(a)

# n = int(input())
# data = list(input())
# total = 0
# for i in data:
#     total += int(i)
# print(total)


# n = int(input())
# data =[]
# total_list= []
# for i in range(n):
#     data.append(input())
# for b in range(len(data)):
#     total = 0
#     adder = 1
#     for a in data[b]:
#         if a == "O":
#             total += adder
#             adder += 1
#         elif a == "X":
#             adder = 1
#     total_list.append(total)
# for x in total_list:
#     print(x)
#

# n , m = map(int,input().split())
# prime = []
# data = 0
# for i in range(2,n+1):
#     data = n % i
#     print(data)
#     if data != 0:
#         if i // 2 <= 1 or i//3 <= 1 or i//5 <= 1 :
#             prime.append(i)
# print(prime)



