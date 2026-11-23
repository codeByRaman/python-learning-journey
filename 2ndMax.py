arr = [22,22,22,22,21,20,22]

max = float('-inf')
sec_max = float('-inf')
third_max = float('-inf')
for i in range (0, len(arr)):
    if arr[i] > max:
        third_max = sec_max
        sec_max = max
        max = arr[i]
    elif arr[i] > sec_max and arr[i] != max:
        third_max = sec_max
        sec_max = arr[i]
    elif arr[i] > third_max and arr[i] != sec_max and arr[i] != max:
        third_max = arr[i]
    
if third_max == float('-inf'):
    print("There are no any third largest element in an Array")
else:
    print(third_max)