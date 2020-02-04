import csv
import time
from win10toast import ToastNotifier
l=[]
f=1
with open('birthday_db.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter =',')
    date = time.strftime("%d-%m-%y")
    date=date[:len(date)-2]
    for i in csv_reader:
        t=i[4]
        t = t[:len(t)-2]
        if t == date:
            l.append(i) 
            f=0
if(f==1):
    toaster = ToastNotifier()
    toaster.show_toast("No Birthdays Today!","Birthdays",threaded=True,icon_path='bday.ico',duration=5)
else:
    for i in l:
        toaster = ToastNotifier()
        toaster.show_toast("Birthday of " + i[1],"Birthdays",threaded=True,icon_path='bday.ico',duration=5)

    
       
