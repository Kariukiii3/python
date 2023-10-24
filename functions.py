# # built-in functions
# num = int(input("enter number:"))
# print(f"absolute of {num} is {abs(num)}")
#
# # custom function
# def Kariuki():
#     print("my name is kariuki")
# Kariuki()
#
# def add():
#     num1= int(input("enter  1st number: "))
#     num2= int(input("enter 2nd number: "))
#     print(f"the sum is {num1+num2}")
# add()
#
# def toshiba():
#     student=["Ian", "mark","ken","john"]
#     print(student)
# toshiba()

# def my_funtion(chakula):
#     for i in chakula:
#         print(i)
# fruits=["mangoes","pineaples", "bananas"]
#
# my_funtion(fruits)
#
# jina="python expt"
#
# for j in jina:
#     if(j !=0):
#         print(j)

x=["python","exceptions","try"]
try:
    for i in range(5):
        print(f"the index and elements from list is {i,x[i]}")
except:
    print("index out of range")
