marks=[40,89,56,53,42,81,40]
print(marks)
print(type(marks))#type list 
print(marks[5]) #list index out of range
print(len(marks))#lenth of list
marks[0]="manya"#list is mutable
print(marks)
print(marks[1:4])#dosen't include ending values
print(marks[-4:-2])#negitive indexing



nums=[10,20,30,40,50,60]
print(nums[0])
print(nums[-1])
print(nums[1:4]) 
print(nums[::-1])
nums.append(70)
print(nums)
nums.pop()
print(nums)


# append adds an element at the end
# insert an elements  at specfic postion
# remove the element at specfic postion
# pop:remove the element and returen the  element
# clear: removes all elements
# index: returns the index of an element 
# count:count  the occerence of elements


nums=[1,2,3,4,5,6]
events=[]
#traditional loop apprach
for n in nums:
    if n%2==0:
        events.append(n**2)
#one line list comprehesion
evens_comp=[n**2 for n in nums if n%2==0]



a=[10,20,30,40]
print(a[1:3])

a=[1,2,3]
a.append([4,5])
print(a)



a=[10,20,30]
a.insert(1,15)
print(a)


a=[1,2,2,3,2]
a.remove(2)
print(a)

a=[5,10,15,20]
print(a[-2])



lists=[10,20,30,40,50]
for i in range(lists[0,4]):
    if(lists[0]>lists[i]):
        print(lists[0])
    else:
        print(lists[i])


#Find the largest element

lists=[10,100,30,40,50,1000]
lists_large=lists[0]
for i in range(6):
    if(lists[i]>lists_large):
        lists_large=lists[i]
print(lists_large)


#Find the smallest element

num=[45,12,78,5,34,9,1]
num_smaller=num[0]
for i in range(len(num)):
    if(num[i]<num_smaller):
        num_smaller=num[i]
print(num_smaller)


#Find the sum of all elements in a list without using sum().

num = [10, 20, 30, 40, 50,20]
total=0
for i in range(len(num)):
    total+=num[i]
print(total)


#Count even and odd numbers in a list.

n = [10, 15, 20, 25, 30, 35, 40]
even_count=0
odd_count=0
for i in range(len(n)):
    if(n[i]%2==0):
        even_count += 1
    else:
         odd_count += 1
print(even_count)
print(odd_count)