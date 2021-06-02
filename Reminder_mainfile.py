
import event_reminder
import assignment_reminder
import sedentary_reminder
import medicine_reminder

from plyer import notification


choice = 0 

print("Hi this is reminder notification program enter your choice:")
print("For adding a specific reminder press: 1 \nFor setting a medicine reminder press: 2 \nAssignment Reminder press: 3\nTo exit the app press z \n")


while choice != 'z' :
    choice = input("\nEnter your choice: ")

    if choice == '1' :
        event_reminder.event_notification()
        event_reminder.snooze()

    elif choice == '2' :
        medicine_reminder.run_medicine()
       
    elif choice == '3' :
        assignment_reminder.run_assignment()

    elif choice == '4':
        sedentary_reminder.run_sedentary()
     
    elif choice == 'z':
        print("\nExiting the app: ")

    else:
        print("Invalid option !! enter again:")

