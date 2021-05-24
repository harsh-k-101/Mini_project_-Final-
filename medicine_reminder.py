
import time
import copy
from plyer import notification

def notify_me(medicine_name):
   #if __name__ == "__main__" :
      notification.notify(
         title = " Medicine Reminder ! ",
         message = " Take " + medicine_name + " medicine ! ",
         app_icon = "medicine.ico",
         timeout = 10
      )

def run_medicine():

    medicine_name = input("Enter the name of medicine: ")
    number_of_dosage = int(input("Enter the number of dosage: "))
 
    dose_count = copy.deepcopy(number_of_dosage)

    choice = 0
        
    notifytime = input("Enter time to notify:")
    
    while True:
      current_time=time.strftime("%H:%M:%S")

      if current_time==notifytime:
        notify_me(medicine_name)
        dose_count = dose_count - 1 
            
        choice = input("If you have fever take " + medicine_name + " and your dose if no press 'n': ")

        if dose_count == 0:
            print("Your doses for today are finished")
            break;

        if choice == 'n':
            break;

print("Go to doctor for check up !")

