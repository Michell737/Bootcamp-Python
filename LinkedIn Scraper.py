#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
from parsel import Selector
from time import sleep
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

opts = Options()

driver = webdriver.Chrome(options=opts)

#function to ensure all key data fields have a value
def validate_field(field):
    #if field is present pass if field:
    if field:
        pass
    #if field is not present print text else:
    else:
        field = 'No results'
    return field

#driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

#Locate email form by_class_name
username = driver.find_element(By.ID,'session_key')

#send_keys() to simulate key strokes
username.send_keys('michelltenaortega@gmail.com')

#sleep for 0.5 seconds
sleep(0.5)

#Locate password form by_class_name
password = driver.find_element(By.ID,'session_password')

#send_keys() to simulate key strokes
password.send_keys('M-t10037')
sleep(0.5)

#Locate submit button by_xpath
sign_in_button = driver.find_element(By.XPATH,'//*[@type="submit"]')

#.click() to mimic button click
sign_in_button.click()
sleep(15)


Jobdata = []
lnks = []
for x in range(0,3,1):
    driver.get(f'https://www.google.com/search?q=site:linkedin.com/in/+AND+%22Python+Developer%22+AND+%22Delhi%22&rlz=1C1CHZO_enIN1023&ei=jPaIY-mEGM6cseMPyZaNmAo&start=10')
    try:
        time.sleep(random.uniform(2.5, 4.9))
        linkedin_urls = [my_elem.get_attribute("href") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='yuRUbf']/a[@href]")))]
        time.sleep(5)
        lnks.append(linkedin_urls)
    except TimeoutException:
        pass

for x in lnks:
    print("Link: ",x)
    for i in x:
        #get the profile URL
        driver.get(i)
        time.sleep(random.uniform(2.5, 4.9))
        print('entre')
        #assigning the source code for the web page to varible sel
        sel = Selector(text=driver.page_source)
        
        #xpath to extract the text from the class containing the name
        name = sel.xpath('//*[starts-with(@class, "text-heading-xlarge inline t-24 v-align-middle break-words")]/text()').extract_first()
        
        #if name exists
        if name:
            #.strip() will remove the new line /n and white spaces
            name = name.strip()
            
        #xpath to extract the text from the class containing the job title
        job_title = sel.xpath('//*[starts-with(@class, "text-body-medium break-words")]/text()').extract_first()
        
        if job_title:
            job_title = job_title.strip()
        
        try:
            #xpath to extract the text from the class xontsining the college
            company = driver.find_element(By.XPATH,'//ul[@class="pv-text-details__right-panel"]').text
        
        except:
            company = 'None'
            
        if company:
            company = company.strip()
            
        #xpath to extract the text from the class containing the location
        location = sel.xpath('//*[starts-with(@class, "text-body-small inline t-black--light break-words")]/text()').extract_first()
        
        if location:
            location = location.strip()
            
        #Validatig if the fields exist on the profile
        name = validate_field(name)
        job_title = validate_field(job_title)
        company = validate_field(company)
        college = validate_field(college)
        location = validate_field(location)
        linkedin_url = validate_field(linkedin_url)
        
        #printing the output
        print('\n')
        print('Name: ' + name)
        print('Job Title: ' + job_title)
        print('Company: ' + company)
        print('Location: ' + location)
        print('URL: ' + linkedin_url)
        print('\n')
        
        data = {
                'Name' : name,
                'Job Title' : job_title,
                'Company' : company,
                'Location' : location,
                'URL' : linkedin_url
                    }
        Jobdata.append(data)
        
    df = pd.DataFrame(Jobdata)
    df.to_excel('Jobdata_linkedin.xlsx')
    # Terminates the application
    driver.quit()



# In[12]:


print(Jobdata)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




