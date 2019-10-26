#!/usr/bin/env python
# coding: utf-8

# This first cell does some necessary imports

# In[37]:


from selenium import webdriver
from xvfbwrapper import Xvfb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
import time
import sys
# These next commands allow us to run headlessly (without an actual browser window opening)

# In[5]:


# display = Xvfb()
# display.start()


# In[39]:


options = webdriver.ChromeOptions()
options.add_argument('window-size=800x841')
options.add_argument('headless')

# now Firefox will run in a virtual display. 
# you will not see the browser.
driver = webdriver.Chrome("/Users/rishabhkrishnan/iCloud Drive (Archive)/Desktop/Berkeley/Freshman/CalHacks/unnamedhack/Mac/chromedriver",chrome_options=options)
def get_phrases(text):
    driver.get('http://claudette.eui.eu/demo/#')
    textBox=driver.find_element_by_id("document_text")
    textBox.clear()
# For files
#     with open("sample_document.txt",'r') as f:
#         for line in f:
#             line=line.strip()
#             arr=line.split("\t")
#             for elem in arr:
#                 textBox.send_keys(elem)
#                 textBox.send_keys(Keys.TAB)
#             textBox.send_keys(Keys.RETURN)
    f=text.split("\n")
    for line in f:
        line=line.strip()
        arr=line.split("\t")
        for elem in arr:
            textBox.send_keys(elem)
            textBox.send_keys(Keys.TAB)
        textBox.send_keys(Keys.RETURN)
    driver.find_element_by_class_name("bluebutton").click()
    time.sleep(2)
    wait=WebDriverWait(driver,500).until(cond.presence_of_element_located((By.CLASS_NAME,"footer")))
    print(driver.find_element_by_class_name("footer").get_attribute('innerHTML'),file=sys.stderr)
    
    print("Woke up",file=sys.stderr)
    if len(driver.find_elements_by_class_name("dots"))>0:
        phrases=driver.find_elements_by_xpath("//div[@name='results_div']/b")
        if len(phrases)==0:
            return ["No suspect phrases"]
        else:
            return [x.text for x in phrases]
    else:
        return ["Language is not english"]
    
        
    #driver.quit()


# In[ ]:





# In[ ]:





# In[ ]:




