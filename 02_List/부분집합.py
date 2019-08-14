# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             for l in range(2):
#                 bit[3] = l
                # print(bit)

# data = [1,2,3]
# bit = [0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
            # print(data, bit)


# arr = [3,6,7,1,5,4]
# n = len(arr)
#
# for i in range(1<<n):
#     for j in range(n+1):
#         if i & (1<<j):
#             print(arr[j],end=", ")
    #     print()
    # print()

# arr2 = [1,2,3]
# n = len(arr2)
# for i in range(1 << n):
#     for j in range(n):
    #     print(arr2[j], end=",")
    # print()



arr = [1,2,3,4,5,6,7,8,9,10]
for i in range(1, 1<<len(arr)):
    sum = 0
    temp = []
    for j in range(len(arr)):
        if i & (1<<j):
            sum += arr[j]
            temp.append(arr[j])
    if sum == 10:
        print(temp)