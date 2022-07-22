import pywhatkit as send
import datetime

current = datetime.datetime.now()
HR  = current.strftime('%H') 
Min = current.strftime('%M')
TimeHR  = int(HR)
TimeMin = int(Min)
TimeMin +=2
number = input("Enter the number with your country code:")
 

f = open("YourMessage.txt", "rt") 
result = f.read()

try:

   send.sendwhatmsg(number, result, TimeHR, TimeMin, tab_close=True)
   print("\n\n","Finished!","\n\n")
 
   
except:
  print("Unexpected Error: Terminated")

