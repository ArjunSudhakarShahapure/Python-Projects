#Types of Data types and vairables
#None 
#Numeric
#List
#Tuple
#Set
#String
#Range
#Dictonary

##############################################
#1.Numeric a.int b.float c.complex d.bool
num1= 23
print("Type of this is :", type(num1))

num2=23.5
print("Type of this :" , type(num2))

num3=2+12j
print("Type of this :" , type(num3))

num4=False
print("Type of this :" , type(num4))

#converting one data type to another
num5=12.4
num6=int(num5)
print("Float Type after converison:" , type(num6))

#creating complex numbers
num7=complex(num5 , num6)
print("Creating complex of num5 and num6 is :", num7)
num8=complex(num1, num4)
print("Creating complex of num1 and num4 is :", num8)
num9=complex(num1)
print("Creating complex of num1 and num10 is :", num9)

#bool
a=12
b=11
bool=a<b 
bool
bool=b<a
bool
int(True) #1
int(False) #0



list1=[12,34,12,"arjun"]
print(list1, type(list1))

set1={1,3,5,6,7,8,99}
print(set1,type(set1))

tuple1=(23,334,1,"arjun")
print(tuple1,type(tuple1))

str="arjun"
print (str, type(str))
range(100)

list(range(5))#num-1 = Index
list(range(2,22,2))#start , stop , step

dis={'name':'arjun','age':'23', 'gender':'male'}
dis
dis.keys()
dis.values()
dis['age']
