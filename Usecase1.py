import pyttsx3
import os

pyttsx3.speak("welcome to my virtual world ")
pyttsx3.speak("I am here to help to open applications just type your query")
print("\t------------------------------------------------")

while True:
   print(" \t chat with me with your requirements: " , end ='')
   p = input()
       
   if (("open" in p) or ("run" in p)) and (("launch" in p) or ("chrome" in p) or ("google" in p)):
     os.system("chrome")

   elif (("open" in p) or ("run" in p) or ("launch" in p)) and (("notepad" in p) or ("editor" in p)):
     os.system("notepad")

   elif (("open" in p) or ("run" in p) or ("launch" in p)) and (("paint" in p) or ("mspaint" in p)):
     os.system("mspaint")

   elif (("open" in p) or ("run" in p)) and (("media player" in p) or ("video player" in p)):
     os.system("wmplayer")

   elif (("open" in p) or ("run" in p)) and (("firefox" in p) or ("mozila firefox" in p)):
     os.system("firefox")

   elif(("open" in p) or ("run" in p)) and (("internetexplorer" in p) or ("explorer" in p)):
     os.system("iexplore")

   elif("exit" in p) or ("close" in p) or ("quit" in p):
     break

   else:
     print("dont support")

print("\n \t THANK YOU...! :)")
pyttsx3.speak("THANK YOU I hope you had a fun interacting with me")

       