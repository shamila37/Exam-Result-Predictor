
#PART 1 - (A) - Outcomes


credits_at_pass  = int(input("Please enter your credits at pass  : "))
credits_at_defer = int(input("Please enter your credit at defer  : "))
credits_at_fail  = int(input("Please enter your credit at fail   : "))


if   120 == credits_at_pass :
    print("Progress")
elif 100 == credits_at_pass :
    print("Progress (module trailer)")
elif 60 <= ( credits_at_pass + credits_at_defer ) :
    print("Do not Progress – module retriever")
else :
    print("Exclude")



#Shamila Gunarathna
#20223147
