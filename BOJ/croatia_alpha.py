#백준 크로아티아 알파벳 실버5 2941번

# alpha = {0: 'c=', 1: 'c-', 2: 'dz=', 3: 'd-', 4: 'lj', 5: 'nj', 6: 's=', 7: 'z='}
# count = 0
data = input()
lists= ['c=','c-','dz=','d-','lj','nj','s=','z=']
res = data
for i in lists:
    res = res.replace(i,'a')
print(len(res))


# datalen = len(data)
#
# if 'dz=' in data:
#     if data.count('dz=') == data.count('z='):
#         count -= 1
#
# for i in lists:
#     if i in data:
#         if data.count(i) > 1 and i != 'z=':
#             count += data.count(i)
#             datalen -= len(i)*data.count(i)
#             if datalen == 0:
#                 break
#         count += 1
#         datalen -= len(i)
# count += datalen
# print(count)

# wordlen  = 0
# for i in range(len(alpha)):
#     temp = data.find(alpha[i])
#     if temp != -1:
#         count += 1
#         if data.count('dz=') == 0 and data.count('z=') == 0:
#             joongbok = data.count(alpha[i])
#             if joongbok != 1:
#                 count += joongbok-1
#                 if len(alpha[i]) == 2:
#                     lists.append(2)
#                 else:
#                     lists.append(3)
#
#         if len(alpha[i]) == 2:
#             lists.append(2)
#         else:
#             lists.append(3)
#
# print(lists)
# for a in lists:
#     wordlen += a
# totallen = len(data) - wordlen
# count += totallen
# print(count)