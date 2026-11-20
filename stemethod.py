# set1={1,2,3,6,5,7}
# set2={2,4,6,8,10}
# print(set1.union(set2))
# print(set1.intersection(set2))


# store following word meaning in a python dictonary
# dict={
#     "cat":"a small animal",
#     "table":["a piece of furniture","list of facts & figures"]
# }
# print(dict)


# you are given a list of subjects for student assume one classroom is requred for 1 subject hoe many classrooms are needed by all student
# python,java,c++,python ,js,java,phython,java,c++,c 

# subject={
#    "c++","js","python","java","c","java","python","c++"        }
# print(len(subject))


student={}
x=int(input("enter pyt m1: "))
student.update({"pyt":x})
y=int(input("enter java m2:"))
student.update({"java":y})
z=int(input("enter c++ m3:"))
student.update({"c++":z})
print(student)
