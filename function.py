# def calc_avg(a,b,c):
#     return (a+b+c)/3
# avger=calc_avg(10,3,2)
# print(avger)
# def len_list(list=[1,2,3,4]):
#    print(len(list))
# len_list()
# 

# def test(x):
#     x+=1
#     return x
# a=5
# print(test(a))
# print(a)
# def check(value):
#     if value:
#         return "Yes"
#     else:
#         return "No"
# print(check(0))
# print(check(5))
# cities=["tok","paris","london"]
# print(max(cities))
# nums=[10,20,30,40]
# result=nums[1:4][1]
# print(result)
# def cal_avg(a,b,c):
#     avg=(a+b+c)/3
#     return avg
# avg=cal_avg(1,2,3)
# print(avg)
# recursive function
# def show(n):
#     if(n==-1):    #base case stoping condition
#      return
#     print(n)
#     show(n-1)
# show(5)
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     return n*fact(n-1)
# print(fact(2))
# def cal_sum(n):
#     if(n==0):
#       return 0 
#     return cal_sum(n-1)+n

# sum=cal_sum(33)
# print(sum)
   
# position arg are the most commen fun when u call a fun python matches the arg u pass to the parameter 



# def des(animal_type,animal_name):
#     print(f"i have a {animal_type} and its name is {animal_name}")
# des("dog","tommy")
# des(animal_name="tommy",animal_type="dog")  #keyword arg allows u to pass values in any order 
# des("cow","ammu")



#a defult arg is a parameter that as a pre set if the user dosen't provide value when calling the fun py defultly uses the value if provide it overwrite the value


# orbitory position some time in advance how many arg a user  pass into a fun by add a    before a param to path all extra postion in form of tuple 
def built_model(name,layers):
    print(f"model{name}")
    print(f"model{name}")
    

