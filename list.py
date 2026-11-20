# marks=[40,89,56,53,42,81,40]
# print(marks)
# print(type(marks))#type list 
# print(marks[5]) #list index out of range
# print(len(marks))#lenth of list
# marks[0]="manya"#list is mutable
# print(marks)
# print(marks[1:4])#dosen't include ending values
# print(marks[-4:-2])#negitive indexing



nums=[10,20,30,40,50,60]
print(nums[0])
print(nums[-1])
print(nums[1:4]) 
print(nums[::-1])
nums.append(70)
print(nums)
nums.pop()
print(nums)
#append adds an element at the end
#insert an elements  at specfic postion
#remove the element at specfic postion
#pop:remove the element and returen the  element
#clear: removes all elements
#index: returns the index of an element 
#count:count  the occerence of elements
# nums=[1,2,3,4,5,6]
# events=[]
# #traditional loop apprach
# for n in nums:
#     if n%2==0:
#         events.append(n**2)
# #one line list comprehesion
# evens_comp=[n**2 for n in nums if n%2==0]