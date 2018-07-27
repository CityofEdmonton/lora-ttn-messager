from lora import lora_proc
import time 

n = lora_proc('testing')
for i in range(30):
   print('Time: '+str(i)) 
   time.sleep(1)
n = lora_proc('this is working')
