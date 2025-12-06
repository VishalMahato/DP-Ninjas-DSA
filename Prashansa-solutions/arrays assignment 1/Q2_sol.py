#Q2. Print Array Elements After Multiplying by 5
#Write a program that multiplies every element in the given array by 5 and prints the updated array

#Create an array
arr=[1,2,3,4,5]
#empty array to store the multiplied values
new_arr=[]
#goes through eavh element one by one
for x in arr:
    #multiplying by 5
    y=x*5
    #add new values
    new_arr.append(y)
    #print the values
    print("Array after multiplying by 5:" ,new_arr)