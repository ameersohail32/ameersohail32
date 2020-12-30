#here are the commands to demonstrate how to access and perform operations on a main file
#run the MODULE of MAIN FILE and import mainfile as a library 

import code as x 
#importing the main file("code" is the name of the file I have used) as a library 

x.create("sohail",30)
#to create a key with key_name,value given and with no time-to-live property

x.create("src",70,1800) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)

x.read("sohail")
#it returns the value of the respective key in Jasonobject format 'key_name:value'

x.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR

x.create("sohail",40)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it

x.modify("sohail",45)
#it replaces the initial value of the respective key with new value 

x.delete("sohail")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
#upto tn
