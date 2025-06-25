#CASE SENSITIVE
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8
print("\n age,Age,aGe,AGE,a_g_e,_age,age_,_AGE_  equals to" , str(age), str(Age), str(aGe),str(AGE), str(a_g_e), str(_age), str(age_), str(_AGE_), "respectively" )

print()
print()

#print ID
n = 300
m = n
print("Id-m", id(m))

m = 400
print("id-m", id(m))


print()
print()


#PRINTId_optimization



print()
print()

#reassign
var = 23.5
print("THis is the original int we assigned to var:", str(var))
var = "Now I am going to become a string"
print("Now we truned the int to a string which says:", var)


print()
print()


#Variables
n = 300
print("n = ", str(n))

print()

a=b=c=1300
print("If we make a,b, and c equal eachother then a,b, and c equals", str(a),str(b),str(c))

print()

print("300 is a", str(type(300)),"data type")

print()

n=m
m=400
print(" m = n \n m =400 \n Then n =400")
