def strlen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter
def strrev(str):
    rstr=""
    l=strlen(str)
    while l > 0:
        rstr=rstr+str[l-1]
        l = l - 1
    return rstr
    
def strcat(st1,st2):
    return(st1+st2)

def strcmp(st1,st2):
    if st1==st2:
        print(st1+"and"+st2+"are same")
    elif st1>st2:
        print(st1+" comes after "+st2+" in the dictionary")
    else:
        print(st1=" comes before "+st2+" in the dictionary")
        print("string function: \n1. string length \n2. string reverse \n 3. string concatenation \n 4. string comparison \n 5. exit")

while True:
        n=int(input("enter your choice:"))
        if n == 1:
            str = input("enter a string:")
            print("length of the string is:",strlen(str))
        elif(n==2):
            str=input("enter a string:")
            print("reversed string is:",strrev(str))
        elif(n==3):
            st1=input("enter the first string:")
            st2=input("enter the second string:")
            print("concatenated string is:",strcat(st1,st2))
        elif(n==4):
            str1=input("enter the first string:")
            str2=input("enter the second string:")
            strcmp(str1,str2)
        elif(n==5):
            print("exited")
            break
        else:
            print("invalid choice")
        
        
