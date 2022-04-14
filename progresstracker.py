#Keeping Track

import datetime
from time import strftime
#create a file using 'w' fuction in line 7 by replacing with fucntion 'a'
#open the file
dtfile = open("ENTERYOURFILENAME.txt", 'a') 
dtfile.writelines('\n-----------------------------New Entry----------------------------\n\n')

#create a class for the date using the datetime module
class datetime():
    string = datetime.date.today().__str__() #you have to return time in str in oder for it to be appended to the file
    print(string)
    dtfile.write('---------Entry Date: '+string)
datetime()

#create a class for time and use the time module to get strftime format function -string-format-time
class time():
    string = strftime('%H:%M:%S %p') #turns the time into a string by using a tuple
    print(string)
    dtfile.write('\n'+'---------Entry Time: '+string+'\n')
time()

#start user progress function
print("\nWelcome!\n")
print('USER MANAUL: [Yes = Y] [No = N] [Done = D] [Personalized = P] [Automated = A]')
print('Press P for Personal\nPress A for Automated\n')

user_choice = input("Pick type of selection: ")
acti_done = " Complete "
acti_not_done = " Incomplete "
input_yes = "Y"
input_no = "N"
input_done = "D"
done_msgA = ("Automated entry done.\nSee you later!")
done_msgP = ("Personalized entry done.\nSee you later!")
comp_question = "Did you finish: "
auto_list = ["Study: ", "Workout: ", "Clean: ", "Entry 'D' to finish: "]
try_again = "Please Try Again."
p_personal = "P"
a_auto = "A"
user_p_entry = ("What activity would you like to record: ")


class entrytype():

    if user_choice == p_personal:
        while True: 
            user_ent = input(user_p_entry)                 
            ans0 = input(comp_question)
            if ans0 == input_yes:
                print(acti_done)
                dtfile.writelines("\n"+user_ent+':'+acti_done)
            elif ans0 == input_no:
                print(acti_not_done)
                dtfile.writelines('\n'+user_ent+':'+acti_not_done)
            elif user_ent == input_done:
                print(done_msgP)
                dtfile.writelines('\n'+done_msgP)
                break              
            else:
                print(try_again)
       
    elif user_choice == a_auto:
        while True:
            ans0 = input(comp_question+auto_list[0])    
            if ans0 == input_yes:
                print(acti_done)
                dtfile.writelines('\n'+auto_list[0]+acti_done)                
            elif ans0 == input_no:
                print(acti_not_done)
                dtfile.writelines('\n'+auto_list[0]+acti_not_done)
            else:
                print(try_again)

            ans1 = input(comp_question+auto_list[1])
            if ans1 == input_yes:
                print(acti_done)
                dtfile.writelines('\n'+auto_list[1]+acti_done)
            elif ans1 == input_no:
                print(acti_not_done)
                dtfile.writelines('\n'+auto_list[1]+acti_not_done)
            else:
                print(try_again)
                
            ans2 = input(comp_question+auto_list[2])
            if ans2 == input_yes:
                print(acti_done)
                dtfile.writelines('\n'+auto_list[2]+acti_done)
            elif ans2 == input_no:
                print(acti_not_done)
                dtfile.writelines('\n'+auto_list[2]+acti_not_done)   
            elif user_choice == input_done:
                print(done_msgA)
                dtfile.writelines('\n'+done_msgA)
                break   
            else:
                print(try_again)             
entrytype()
dtfile.writelines('\n\n---------------------------End of Entry---------------------------\n\n')
dtfile.close()



