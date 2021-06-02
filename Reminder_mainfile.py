
import event_reminder
import assignment_reminder
import sedentary_reminder
import medicine_reminder

from plyer import notification


choice = 0 

print("Hi this is reminder notification program enter your choice:")
print("----------------------------------------------")
print("---> For Specific Reminder           press: 1")
print("---> For setting a Medicine Reminder press: 2")
print("---> For Assignment Reminder         press: 3")
print("---> For Sedentry Reminder           press: 4")
print("To exit press: z\n")

while choice != 'z' :
    print("----------------------------------------------")
    choice = input("Enter your choice: ")
    print("----------------------------------------------")

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

