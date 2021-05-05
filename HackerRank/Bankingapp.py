obal,ttype,tamt=int(input("Enter Old Balance:")),input("Enter Transaction Type:"),int(input("Enter Transaction Amount:"))
s=["W","w","D","d"]
#if ttype=="W" or ttype=="w":
#if ttype in "Ww":
if ttype in s[0:2]:
    if tamt>obal:
        print("Insufficient Funds")
    elif tamt==obal:
        print("Please Maintain Minimum Balance")
    else:
        cbal=obal-tamt
        print("Current Balance is:",cbal)
#elif ttype=="D" or ttype=="d":
elif ttype in s[2:4]:
    if tamt>50000:
        print("Required Pan Card")
        opt=input("Do you have Pan Card?")
        if opt=="Y" or opt=="y":
            cbal=obal+tamt
            print("Current Balance is:",cbal)
    else:
        cbal=obal+tamt
        print("Current Balance is:",cbal)
else:
    print("Invalid Operation")
