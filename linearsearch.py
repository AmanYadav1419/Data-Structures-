
def search(arr,n):
    return next((i+1 for i in range(num) if n==arr[i]), -1)
            
            
arr = []
num = int(input("Enter the length of array:"))
print("Enter the value of integers for array:")
for _ in range(num):
    a = int(input())
    arr.append(a)

n = int(input("Enter the number to be searched:"))

result = search(arr,n)

if result == -1:
    print("Number not present in the array")
else:
    print("Position of the number in array:", result)