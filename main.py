from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import json
import os

class Main():
    def ReadConfig(self):
        with open('config.json','r') as f:
            return json.load(f)
    def __init__(self):
        config = self.ReadConfig()
        self.targeturl = config['targeturl']
        self.elementxpath = config['elementxpath']
        self.newvalue = config['newvalue']
        chrome_options = Options()  
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])
        chrome_options.add_argument('--log-level=3')

        self.driver = webdriver.Chrome(service_log_path=os.devnull,options=chrome_options)
        
    def Find(self):
        value_elem = None
    
        while value_elem == None:
            try:
                value_elem = self.driver.find_element_by_xpath(self.elementxpath)
            except:
                pass
        return value_elem

    def Change(self):
        value_elem = self.Find()
        while True:
            try:
                self.driver.execute_script("arguments[0].innerText = '{0}';".format(self.newvalue), value_elem)
            except:
                self.Change()
            
    def Start(self):
        self.driver.get(self.targeturl)
        self.Change()

if __name__ == '__main__':
    main = Main()
    main.Start()