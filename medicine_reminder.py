
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
        
    while True:
      notifytime = input("Enter time to notify:")

      while True:
        current_time=time.strftime("%H:%M:%S")

        if current_time==notifytime:

          notify_me(medicine_name)  

          choice = input("If you have fever take " + medicine_name + " and your dose if no press 'n': ")
          break;

      if choice == 'n':
        break;

#run_medicine()
