from selenium import webdriver
from ordered_set import OrderedSet
import time
import os
import csv

os.system("cls")


f=open("99acres.csv","w",encoding='utf-8')
csv_writer= csv.writer(f)
csv_writer.writerow(['Project', 'specification', 'area','Value'])

driver = webdriver.Chrome('D:/virtualenvs_muthu/selenium_twitter/chromedriver_win32/chromedriver.exe') 

os.system("cls")

scroll_list=OrderedSet()

for x in range(1,3):
   
    
                  
    driver.get(f"https://www.99acres.com/property-in-hadapsar-pune-ffid-page-{x}")       
    try:
        mutiple_properties=driver.find_elements_by_class_name('srpTuple__tupleDetails')
        time.sleep(2)
        
        for elem in (mutiple_properties):
            scroll_list.add(elem.text)
            
    except:
        continue   

    
    
    

temp=list(scroll_list)


my_actual_list=[]


for x in temp:
    
    xt=x.split("\n") 
      
    print(xt)
    
    try:
        if xt!=['']:
            
            my_actual_list=[xt[2],xt[1],xt[4],xt[3]]
        
    except:
        temp_i=temp.index(x)

        os.system("cls")
        print("previous:")
        print(temp[temp_i-1])
        print("error:")
        print(xt)
        
        

                
        
       
   
    print(my_actual_list)

    csv_writer.writerow(my_actual_list)
    my_actual_list.clear()



f.close()
        
