
#PART 4 - Dictionary (separate program)


credits_at_pass = 0
credits_at_defer = 0
credits_at_fail = 0    #At the beginning of the code, these three variables are zero.

credits_range = [0, 20, 40, 60, 80, 100, 120]               #The range they want.

def getting_student_id():
    unique_student_ID = input("Please enter Student ID: ")  #Get the student's unique ID number.
    

def getting_credit_pass() :                                 #Use to create a function.
    global credits_at_pass
    try :
        credits_at_pass = int(input("Please enter your credits at pass  : "))    #The number of credits at the pass.
    except ValueError :                                                          #Find value errors with try except part.
        print("Integer required\n")
        getting_credit_pass()
    else:
        if credits_at_pass not in credits_range :
            print("Out of range.\n")
            getting_credit_pass()

            
def getting_credit_defer() :
    global credits_at_defer
    try :
        credits_at_defer = int(input("Please enter your credit at defer  : "))    #The number of credits at the defer.
    except ValueError :                                                           #Find value errors with try except part.
        print("Integer required\n")
        getting_credit_defer()
    else:
        if credits_at_defer not in credits_range :
            print("Out of range.\n")
            getting_credit_defer()
            

def getting_credit_fail() :
    global credits_at_fail
    try :
        credits_at_fail = int(input("Please enter your credit at fail   : "))    #The number of credits at the fail.
    except ValueError :                                                          #Find value errors with try except part.
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

    if 120 != (credits_at_pass + credits_at_defer + credits_at_fail) :            #This is use to compair the total with 120.
        print("Total incorrect.\n")
        get_credits()


student = True                                                                    

progress = 0
module_trailer = 0 
module_retriever = 0 
exclude = 0

#data_file = open("Datafile.txt", "a")                                             #This use to create and open the Datafile.txt 


my_dictionary ={}         #This is the new dictionary.


outputs = [[] , [] , [] , []]
#outputs = [[progress] , [module_trailer] , [module_retriever] , [exclude]]

while student :
    student_id = getting_student_id()
    get_credits()
    if 120 == credits_at_pass :
        print("Progress")
        outputs[0].append([credits_at_pass , credits_at_defer , credits_at_fail])
    elif 100 == credits_at_pass :
        print("Progress (module trailer)")
        outputs[1].append([credits_at_pass , credits_at_defer , credits_at_fail])
    elif 60 <= ( credits_at_pass + credits_at_defer ) :
        print("Do not Progress – module retriever")
        outputs[2].append([credits_at_pass , credits_at_defer , credits_at_fail])
    else :
        print("Exclude")
        outputs[3].append([credits_at_pass , credits_at_defer , credits_at_fail])

    if "q" == input("\nWould you like to enter another set of data? \n"
                      "Enter 'y' for yes or 'q' to quit and view results: "):
      
    

        print(" ")
      
    
        student = False
        
#data_file.close()


print("-" * 63, "\nHistogram")
print("Progress", len(outputs[0]), "  :", " *" * len(outputs[0]))
print("Trailer", len(outputs[1]), "   :", " *" * len(outputs[1]))
print("Retriever", len(outputs[2]), " :", " *" * len(outputs[2]))
print("Excluded", len(outputs[3]), "  :", " *" * len(outputs[3]))
print("\n", (len(outputs[0]) + len(outputs[1]) + len(outputs[2]) + len(outputs[3])), "outcomes in total.")
print("-" * 64)

print("Part 4:")

#print(my_dictionary)

for output in outputs:
    for progress in output:
        if output == outputs[0]:
            print("Progress                  - ", progress[0], ",", progress[1], ",", progress[2])
        elif output == outputs[1]:
            print("Progress (module trailer) - ", progress[0], ",", progress[1], ",", progress[2])
        elif output == outputs[2]:
            print("Module retriever          - ", progress[0], ",", progress[1], ",", progress[2])
        elif output == outputs[3]:
            print("Exclude                   - ", progress[0], ",", progress[1], ",", progress[2])





#Shamila Gunarathna
#20223147
