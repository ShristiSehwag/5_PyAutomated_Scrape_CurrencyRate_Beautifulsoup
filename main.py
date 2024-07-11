from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# login , click, scrape


def get_driver():

  #set options for easier browsing
  options = webdriver.ChromeOptions()
  options.add_argument('disaable-infobars')
  options.add_argument('start-maximized ')
  options.add_argument('disable-dev-shm-usage')
  options.add_argument('no-sandbox') #gain more privilage
  options.add_experimental_option('excludeSwitches', ['enable-automation'])
  options.add_argument('disable-blink-features=AutomationControlled')

  driver = webdriver.Chrome(options)
  driver.get('https://automated.pythonanywhere.com/login/')

  return driver 

def clean_text(text):
  """Extract only the temperature from text"""
  # gives list of text, convert to float
  output = float(text.split(": ")[1])
  return output


def main():
  driver = get_driver()
  
  ## LOGIN - enter text
  driver.find_element(by='id',value ='id_username').send_keys("automated")
  
  time.sleep(2) #delay task
  
  driver.find_element(by='id',value ='id_password').send_keys("automatedautomated" + Keys.RETURN) # CLICK submit (with return(acts like enter key))
  # print(driver.current_url) #print new web page url
  time.sleep(2)

  
  #Go to home
  driver.find_element(by='xpath',value ='/html/body/nav/div/a').click()
  time.sleep(2)
  

  text = driver.find_element(by='xpath',value ='/html/body/div[1]/div/h1[2]')
  return clean_text(text.text)

  
  
print(main())

