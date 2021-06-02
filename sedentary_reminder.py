import time
from plyer import notification

def notify_me():
    #if __name__ == "__main__" :
       notification.notify(
          title = " Sedentary Reminder ! ",
          message = " Make sure to drink water and stay hydrated ! ",
          timeout = 15,
          app_icon = "hydrate.ico"
       )



def run_sedentary():
 interval = float(input("Enter time interval: "))
 interval = interval*60

 choice = 0


 while True :
     time.sleep(interval)    
     notify_me()
     choice = input("continue sedentary reminder? press 'y' to continue 'n' to stop: ")

     if choice == 'n' :
        break;

 print("Sedentry reminder stopped !")
 