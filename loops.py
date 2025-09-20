arr = list(map(int ,input().split()))    #[1, 2, 3, 4, 5]input , Output: [5, 1, 2, 3, 4]
avv = []
for i in range(len(arr)):
    if arr[i] == arr[-1]:
        avv.insert(0, arr[i])
    else:
        avv.append(arr[i])
print(avv)
print("hey this is rahul heyyy i am rahul there are funcking ngbjhbhwgbhgw")