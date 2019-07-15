# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 22:16:24 2019

@author: Rodrigo
"""
import sys
time_unit=sys.argv[1]
time_val=int(sys.argv[2])

#start validation
if time_unit=="minutes":
    time_val=60*time_val
elif time_unit=="seconds":
    time_val=time_val



#create dummy data
import datetime
import hashlib
import random

source_language_list=['en','fr','pt','it','dk']
target_language_list=['en','fr','pt','it','dk']
client_list=['easyjet','booking']

time_s=datetime.datetime.utcnow()
time_end=datetime.datetime.utcnow()+datetime.timedelta(0,time_val)

print("The records are being generated:")
print("The records will be generated between: ")
print("      "+str(time_s))
print("      "+str(time_end))
if time_unit=="minutes":
    print("this will take: {} minutes".format(str(time_val/60)))
elif time_unit=="seconds":
    print("this will take: {} seconds".format(str(time_val)))
else:
    raise ValueError("Time unit is not recognizable:")
    raise ValueError("must be seconds or minutes")
    


#save dummy data for analysis
with open("dummy_data.txt","w") as file:
    while datetime.datetime.utcnow()<time_end:
        timestamp=str(datetime.datetime.utcnow().strftime ("%Y-%m-%d %H:%M:%S"))
        translation_id=hashlib.sha256((timestamp+str(random.randint(15,400))).encode()).hexdigest()
        
        source_language=random.choice(source_language_list)
        target_language=random.choice(target_language_list)
        while target_language==source_language:
            target_language=random.choice(target_language_list)
            
        client_name=random.choice(client_list)
        
        nr_words=random.randint(15,400)
        duration=random.randint(15,60)
        data='{"timestamp": "'+timestamp+'","translation_id": "'+translation_id+'","source_language": "'+ \
            source_language+'","target_language": "'+target_language+'","client_name": "'+client_name+'","event_name": "translation_delivered",'+\
            '"nr_words": '+ str(nr_words)+', "duration": '+str(duration)+'}\n'
        file.write(data)
    


    