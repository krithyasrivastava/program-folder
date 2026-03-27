arr= [10,20,30,40,60,70]
print(arr)
arr.append(100)
arr.remove(20)
print(arr)
for i in arr:
    print(i)
key= 10
if key in arr:
    print("mil gya")
else:
    print("not fond")

arr[3]= 200   
print(arr)

arr.sort()
print(arr)