
#PART 1 - (C) - Multiple Outcomes


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

while student :
    get_credits()
    if 120 == credits_at_pass :
        print("Progress")
    elif 100 == credits_at_pass :
        print("Progress (module trailer)")
    elif 60 <= ( credits_at_pass + credits_at_defer ) :
        print("Do not Progress – module retriever")
    else :
        print("Exclude")

    if "q" == input("\nWould you like to enter another set of data? \n"
                      "Enter 'y' for yes or 'q' to quit and view results: "):
        
    
        student = False




#Shamila Gunarathna
#20223147
