'''from math import pi
r=float(input("Input radius: "))
print("Area of circle with radius "+str(r)+" is "+str(pi*r**2))

val=input("Enter some comma seperated values: ")
list=val.split(",")
tup=tuple(list)
print("List: ",list)
print("Tupple: ",tup)

val=input("Enter filename:") #my way
list=val.split(".")
print(list[1])

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))



exam_st_date = (11,12,2014)
print( "The examination will start from : %d / %d / %d"%exam_st_date)

n=input("Enter the value: ")     #my way 
n1=int(n)
n2=int(n+n)
n3=int(n+n+n)
print(n1+n2+n3)'''


a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)







