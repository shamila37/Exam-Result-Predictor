
#PART 1 - (D) - Histogram


credits_at_pass = 0
credits_at_defer = 0
credits_at_fail = 0    #At the beginning of the code, these three variables are zero.

credits_range = [0, 20, 40, 60, 80, 100, 120]               #The range they want.


def getting_credit_pass() :
    global credits_at_pass
    try :
        credits_at_pass = int(input("Please enter your credits at pass  : "))    
    except ValueError :
        print("Integer required\n")
        getting_credit_pass()
    else:
        if credits_at_pass not in credits_range :
            print("Out of range.\n")
            getting_credit_pass()

            
def getting_credit_defer() :
    global credits_at_defer
    try :
        credits_at_defer = int(input("Please enter your credit at defer  : "))
    except ValueError :
        print("Integer required\n")
        getting_credit_defer()
    else:
        if credits_at_defer not in credits_range :
            print("Out of range.\n")
            getting_credit_defer()
            

def getting_credit_fail() :
    global credits_at_fail
    try :
        credits_at_fail = int(input("Please enter your credit at fail   : "))
    except ValueError :
        print("Integer required\n")
        getting_credit_fail()
    else:
        if credits_at_fail not in credits_range :
            print("Out of range.\n")
            getting_credit_fail()
            

def get_credits():
    getting_credit_pass()
    getting_credit_defer()
    getting_credit_fail()

    if 120 != (credits_at_pass + credits_at_defer + credits_at_fail) :
        print("Total incorrect.\n")
        get_credits()


student = True

progress = 0
module_trailer = 0 
module_retriever = 0 
exclude = 0

while student :
    get_credits()
    if 120 == credits_at_pass :
        print("Progress")
        progress = progress + 1
    elif 100 == credits_at_pass :
        print("Progress (module trailer)")
        module_trailer = module_trailer + 1
    elif 60 <= ( credits_at_pass + credits_at_defer ) :
        print("Do not Progress – module retriever")
        module_retriever = module_retriever + 1
    else :
        print("Exclude")
        exclude = exclude + 1

    if "q" == input("\nWould you like to enter another set of data? \n"
                      "Enter 'y' for yes or 'q' to quit and view results: "):
      
    
        student = False


print("-" * 63, "\nHistogram")
print("Progress", progress, "  :", " *" * progress)
print("Trailer", module_trailer, "   :", " *" * module_trailer)
print("Retriever", module_retriever, " :", " *" * module_retriever)
print("Excluded", exclude, "  :", " *" * exclude)
print("\n", (progress + module_trailer + module_retriever + exclude), "outcomes in total.")
print("-" * 64)



#Shamila Gunarathna
#20223147
