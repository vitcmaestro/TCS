permuter = []
def addr(string):
    permuter.append(string)
def permute(arr,size,length):
  if(size == 1):
      s = str("".join(arr))
      addr(s)
  for i in range(size):
    permute(arr,size-1,length)
    if(size%2 !=0):
      arr[0],arr[size-1] = arr[size-1],arr[0]
    else:
      arr[i],arr[size-1] = arr[size-1],arr[i]
a = list(map(str,input().split(" ")))
first = list(a[0])
second = a[1]
sum = int(a[0])+int(a[1])
permute(first,len(first),len(first))
print(permuter)
for i in permuter:
    if(int(i)>int(second) and int(i)< sum):
        sum = int(i)
print(sum)

