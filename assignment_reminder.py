from datetime import datetime
from plyer import notification

name_exp = []
due = []
remaining_exp = []
remaining_due = []
now = datetime.now()


def get_data():
    while True:
        exp_name = input("\nEnter Subject name , experiment name : ")
        due_date = input("Enter Due Date of the assignment in format day/month/year : ")

        name_exp.append(exp_name)
        due.append(due_date)

        choice = input(" Add another assignment ? press y (yes) / n (no): ")
        if choice == 'n':
            break;


def save_data():

    exp_name_file = open("exp_name_file.txt","a")
    exp_date_file = open("exp_date_file.txt","a")

    for i in range(0,len(name_exp)):
        exp_name_file.write(name_exp[i])
        exp_name_file.write("\n") 
        exp_date_file.write(due[i])
        exp_date_file.write("\n")  

    exp_name_file.close()
    exp_date_file.close()

    name_exp.clear()
    due.clear()


def check_due_all():
    now = datetime.now()

    with open('exp_name_file.txt') as f:
        name_exp =  [line.rstrip() for line in f]
    f.close()

    with open('exp_date_file.txt') as f:
        due =  [line.rstrip() for line in f]
    f.close()    

    for i in range(0,len(due)):
        due_date_obj = datetime.strptime( due[i] , '%d/%m/%y')

        if ((due_date_obj.month < now.month ) or (due_date_obj.day < now.day and due_date_obj.month <= now.month ))  :
            remaining_exp.append(name_exp[i])
            remaining_due.append(due[i])

            
    print("\nDue assignments \t dates ")
    for i in range(0,len(due)):
        due_date_obj = datetime.strptime( due[i] , '%d/%m/%y')

        if ((due_date_obj.month >= now.month ) or (due_date_obj.day >= now.day and due_date_obj.month >= now.month ))  :            
          print(name_exp[i] + '\t \t ' + due[i])

    print("\nOver assignments \t  dates ")
    for i in range(0,len(remaining_due)):
       print(remaining_exp[i] + '\t \t ' + remaining_due[i])


def today_submission():
    today_dueexp = []
    count = 0

    with open('exp_name_file.txt') as f:
        name_exp =  [line.rstrip() for line in f]
    f.close()

    with open('exp_date_file.txt') as f:
        due =  [line.rstrip() for line in f]
    f.close()



    for i in range(0,len(due)):
      due_date_obj = datetime.strptime( due[i] , '%d/%m/%y')

      if due_date_obj.day == now.day and due_date_obj.day == now.day:
        today_dueexp.append(name_exp[i])
        count += 1

    
    listToStr = ' '.join([str(elem) for elem in today_dueexp])

    #if __name__ == "__main__" :
    notification.notify(
         title = " Assignments Due today ",
         message = " In Total " + str(count) + " assignment(s) " + listToStr + " due today " ,
         app_icon = "assignment.ico",
         timeout = 15, 
      )

def clear_old_assignments():

    with open('exp_name_file.txt') as f:
        name_exp =  [line.rstrip() for line in f]
    f.close()

    with open('exp_date_file.txt') as f:
        due =  [line.rstrip() for line in f]
    f.close()   

    exp_name_file = open("exp_name_file.txt","w")
    exp_date_file = open("exp_date_file.txt","w")

    for i in range(0,len(name_exp)):
      due_date_obj = datetime.strptime( due[i] , '%d/%m/%y')
      if ((due_date_obj.month > now.month ) or (due_date_obj.day >= now.day and due_date_obj.month >= now.month )) : 
        exp_name_file.write(name_exp[i])
        exp_name_file.write("\n") 
        exp_date_file.write(due[i])
        exp_date_file.write("\n")  

    exp_name_file.close()
    exp_date_file.close()

    name_exp.clear()
    due.clear()
    

def run_assignment():
  choice = 0
  while True:
    choice = input("1: add assignment , 2: due today, 3: all due , 4: clear old assignments, z:exit :")

    if choice == '1':
        get_data()
        save_data()

    elif choice == '2':
        today_submission()

    elif choice == '3':
        check_due_all()

    elif choice == '4':
        clear_old_assignments()
        print("Old Assignments Deleted!")
    
    elif choice == 'z':
        break;

    else:
        print("Invalid choice:")

#run_assignment()
