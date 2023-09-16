import logging
import random
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
from selenium.common.exceptions import NoSuchElementException 

#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
#driver = webdriver.Chrome()#options=options
#driver.get("https://epayment-test.orange.int/login/")
log_url = "https://epayment-test.orange.int/login"
home_url = "https://epayment-test.orange.int/partenaire?page=1"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#@pytest.fixture(scope="function")
#def setup():
#    driver = webdriver.Chrome()
#    yield driver
#    #driver.quit()

class Login_deconnexion:
    def login(self,driver, username, password, stay_connected):
        driver.maximize_window()
        driver.find_element(By.XPATH, "//input[@id='inputUsername']").clear()
        driver.find_element(By.XPATH, "//input[@id='inputPassword']").clear()
        time.sleep(1)
        driver.find_element(By.XPATH, "//input[@id='inputUsername']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@id='inputPassword']").send_keys(password)
        if stay_connected:
            driver.find_element(By.XPATH,"//div[@class='inline-flex items-center']").click()
        driver.find_element(By.XPATH, "//button[normalize-space()='SE CONNECTER']").click()
        time.sleep(1)
        cur_url = driver.current_url
        return cur_url

    def logout(self,driver):
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@data-test-id='logout']").click()
        cur_url = driver.current_url
        return cur_url
    
class Commandes:
    #def __init__(self, driver):
    #    self.driver = driver
    
    def click_success(self,driver):
        driver.find_element(By.XPATH,"//button[@data-test-id='commandes']").click()
        success1 = int(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > h5:nth-child(2)"))
        ).text)        
        driver.find_element(By.XPATH,"//body/div/div/div[1]/div[1]/div[2]/div[3]").click()
        time.sleep(2)
        success2 = int(driver.find_element(By.CSS_SELECTOR,"div[class='relative flex flex-col bg-clip-border rounded-xl text-gray-700 shadow-md cursor-pointer active bg-green-100 bg-opacity-10'] h5[class='block antialiased tracking-normal font-sans text-xl font-semibold leading-snug text-blue-gray-900']").text)
        failed =   int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > h5:nth-child(2)").text)
        Replay =   int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > h5:nth-child(2)").text)
        Ambigu =   int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(6) > div:nth-child(2) > h5:nth-child(2)").text)
        assert success1==success2 and failed==0 and Replay==0  and Ambigu==0 
    
    def click_failed(self,driver):
        driver.find_element(By.XPATH,"//button[@data-test-id='commandes']").click()
        failed1 =int(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > h5:nth-child(2)"))
        ).text)
        driver.find_element(By.XPATH,"//body/div/div/div[1]/div[1]/div[2]/div[4]").click()
        time.sleep(1)
        success = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > h5:nth-child(2)").text)
        failed2 = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > h5:nth-child(2)").text)
        Replay =  int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > h5:nth-child(2)").text)
        Ambigu =  int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(6) > div:nth-child(2) > h5:nth-child(2)").text)
        assert failed1==failed2 and success==0 and Replay==0  and Ambigu==0 
    
    def click_replay(self,driver):
        driver.find_element(By.XPATH,"//button[@data-test-id='commandes']").click()
        replay1 =int(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > h5:nth-child(2)"))
        ).text)
        driver.find_element(By.XPATH,"//body/div/div/div[1]/div[1]/div[2]/div[5]").click()
        time.sleep(1)
        success = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > h5:nth-child(2)").text)
        failed =  int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > h5:nth-child(2)").text)
        replay2 = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > h5:nth-child(2)").text)
        Ambigu =  int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(6) > div:nth-child(2) > h5:nth-child(2)").text)
        assert replay1==replay2 and success==0 and failed==0  and Ambigu==0 
        
    def click_ambigu(self,driver):
        driver.find_element(By.XPATH,"//button[@data-test-id='commandes']").click()
        ambigu1 =int(WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2) > h5:nth-child(2)"))
        ).text)
        time.sleep(1)
        driver.find_element(By.XPATH,"//body/div/div/div[1]/div[1]/div[2]/div[6]").click()
        time.sleep(1)
        success = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > h5:nth-child(2)").text)
        failed = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(4) > div:nth-child(2) > h5:nth-child(2)").text)
        Replay = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > h5:nth-child(2)").text)
        ambigu2 = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(6) > div:nth-child(2) > h5:nth-child(2)").text)
        assert ambigu1==ambigu2 and success==0 and Replay==0  and failed==0             
    
    def click_last_button(self,driver):
        div_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='my-5 text-center']"))
        )
        last_button = WebDriverWait(div_element, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='my-5 text-center']//button[last()]"))
        )
        last_button.click()
    
    def calculate_total(self, montants, statuses):
        total = 0
        for amount, status in zip(montants, statuses):
            if status.text == "Success":
                y = amount.text.replace(',','.').replace(' ','')
                total += float(y)
        return total
    
    def process_slide(self,driver,page_number):
        montants = WebDriverWait(driver, 11).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='root']/div/div[1]/div/div[3]/div/div[2]/table/tbody/tr/td[11]/p"))
        )
        status = WebDriverWait(driver, 11).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@id='root']/div/div[1]/div/div[3]/div/div[2]/table/tbody/tr/td[14]/p"))
        )
        total = 0      
        total = self.calculate_total(montants, status)
        print(f"Total for page {page_number}: {total}")
        montants=[]
        status=[]
        #self.click_last_button()   
        return total
    
    def verifier_mnts(self,driver):  
        driver.find_element(By.XPATH,"//button[@data-test-id='commandes']").click()
        time.sleep(2) 
        amounts=driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > h5:nth-child(2)").text
        total_amounts = float(amounts.replace(',','.').replace(' ',''))                 
        TOT = 0
        page_number = 1
        total=0
        try:
            while True:
                total = self.process_slide(driver,page_number)
                TOT += total
                page_number += 1
                self.click_last_button(driver)
        except :
            print("hello")  
        TOT=round(TOT,2)     
        print("Final Total:", TOT)  
        assert total_amounts==TOT ,"les totaux des montants ne sont pas égaux"


    def verify_nbrcom(self,driver):
        driver.find_element(By.XPATH,"//button[@data-test-id='commandes']").click()
        time.sleep(2)
        total_cmd = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > h5:nth-child(2)").text)
        success = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > h5:nth-child(2)").text)
        failed = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > h5:nth-child(2)").text)
        Replay = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > h5:nth-child(2)").text)
        Ambigu = int(driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > div:nth-child(2) > h5:nth-child(2)").text)
        total2 = success + failed + Replay + Ambigu
        print(f" {str(total_cmd)} egal à {str(total2)}")
        assert total_cmd == total2, "les totaux des commandes ne sont pas égaux"
        
    def telecharger_liste_rapport(self,driver):
        driver.find_element(By.XPATH,"//button[@data-test-id='réconciliation']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//tbody//tr//td[5]//button").click()
        popup_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        popup_element.find_element( By.XPATH, "//button[normalize-space()='Oui, JE CONFIRME']" ).click()      
        time.sleep(1)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'swal2-html-container')))
            popup_element = driver.find_element(By.ID, 'swal2-html-container')
            popup_text = popup_element.text
            return popup_text
        except Exception as e:
            print(f"An error occurred: {str(e)}")       
            
    def telecharger_liste_cmd(self,driver):
        driver.find_element(By.XPATH,"//button[@data-test-id='commandes']").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//button[@data-test-id='export-orders']").click()
        popup_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        popup_element.find_element( By.XPATH, "//button[normalize-space()='Oui, JE CONFIRME']" ).click()      
        time.sleep(1)
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'swal2-html-container')))
            popup_element = driver.find_element(By.ID, 'swal2-html-container')
            popup_text = popup_element.text
            return popup_text
        except Exception as e:
            print(f"An error occurred: {str(e)}")          
        
        
class Partner:
    def recherche_pre_partner(self,driver):
        recherche=driver.find_element(By.XPATH,"//button[normalize-space()='RECHERCHE']")
        recherche.click()
        rech_list=driver.find_element(By.XPATH,"//button[@data-test-id='advaced-criteria']")
        rech_list.click()
        time.sleep(1)
        prepaye=driver.find_element(By.XPATH,"//input[@id='type-prepaid']")
        prepaye.click()
        appliquer=driver.find_element(By.XPATH,"//button[normalize-space()='APPLIQUER']")
        appliquer.click()
        #count_prep=len(driver.find_element(By.XPATH,"//tbody/tr"))
        time.sleep(2)
        elements=driver.find_elements(By.XPATH,"//tbody/tr/td[4]/p[1]")
        for elem in elements:
            assert elem.text == "Prépayé"
        cancel=driver.find_element(By.XPATH,"//button[@data-test-id='cancel-close-filters']")    
        cancel.click()
        
    def recherche_post_partner(self,driver):
        recherche=driver.find_element(By.XPATH,"//button[normalize-space()='RECHERCHE']")
        recherche.click()
        rech_list=driver.find_element(By.XPATH,"//button[@data-test-id='advaced-criteria']")
        rech_list.click()    
        time.sleep(1)
        pospaye=driver.find_element(By.XPATH,"//input[@id='type-postpaid']")
        pospaye.click() 
        appliquer=driver.find_element(By.XPATH,"//button[normalize-space()='APPLIQUER']") 
        appliquer.click() 
        time.sleep(2)
        elements=driver.find_elements(By.XPATH,"//tbody/tr/td[4]/p[1]")
        for elem in elements:
            assert elem.text == "Postpayé"
        cancel=driver.find_element(By.XPATH,"//button[@data-test-id='cancel-close-filters']")    
        cancel.click()             
        
    def descativer_partner(self,driver):
        wait=WebDriverWait(driver,10)
        desactiver=wait.until(EC.presence_of_element_located((By.XPATH,"//label[@for='switch-12']")))
        desactiver.click()
        try:
            popup_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@aria-labelledby='swal2-title']"))
            )
            confirm_button = popup_element.find_element(By.XPATH, "//button[normalize-space()='Oui, JE CONFIRME']")
            confirm_button.click()

        except TimeoutException:
            print("Popup or element was not visible within the specified time.")    
        time.sleep(1)    
        count_prep2=len(driver.find_elements(By.XPATH,"//tbody/tr"))
        return count_prep2
             
        
    def activer_partner(self,driver):
        wait=WebDriverWait(driver,10)
        recherche=driver.find_element(By.XPATH,"//button[normalize-space()='RECHERCHE']")
        recherche.click()
        rech_list=driver.find_element(By.XPATH,"//button[@data-test-id='advaced-criteria']")
        rech_list.click()         
        desact=driver.find_element(By.XPATH,"//button[2]//div[1]")
        desact.click()    
        appliquer=driver.find_element(By.XPATH,"//button[normalize-space()='APPLIQUER']")
        appliquer.click()
        activer=wait.until(EC.presence_of_element_located((By.XPATH,"//label[@for='switch-12']")))
        activer.click()
        try:
            popup_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
            # Locate and click the element inside the popup
            confirm_button = popup_element.find_element(By.XPATH, "//button[normalize-space()='Oui, JE CONFIRME']")
            confirm_button.click()
        except TimeoutException:
            print("Popup or element was not visible within the specified time.")    
        time.sleep(3)        
        cancel=driver.find_element(By.XPATH,"//button[@data-test-id='cancel-close-filters']")    
        cancel.click()   
        time.sleep(2)       
        count_prep2=len(driver.find_elements(By.XPATH,"//tbody/tr"))
        return count_prep2          
                  
         
    def ajouter_sous_partenaire(self,driver):
        edit=driver.find_element(By.XPATH,"//tbody/tr[3]/td[7]/div[1]/button[2]")
        edit.click()
        len1=len(driver.find_elements(By.XPATH,"//div[contains(@class,'mb-6')]/div")) 
        time.sleep(1)
        add_ss_partner=driver.find_element(By.XPATH,"//button[normalize-space()='AJOUTER UN SOUS PARTENAIRE']")
        add_ss_partner.click()  
        time.sleep(2) 
        driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(12) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys(f"demoO{random.randint(1,100)}")
        driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(12) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)").send_keys(f"demoo{random.randint(1,100)}")
        driver.find_element(By.XPATH,"//input[@id='gab-rc-cc']").click()
        driver.find_element(By.XPATH,"//input[@id='gab-inv-cash']").click()
        driver.find_element(By.XPATH,"//li[contains(@data-value,'mob')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='mob-rc-cc']").click()
        driver.find_element(By.XPATH,"//input[@id='mob-inv-cc']").click()
        driver.find_element(By.XPATH,"//li[@data-value='agn']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='agn-rc-cash']").click()
        driver.find_element(By.XPATH,"//input[@id='agn-inv-cash']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[normalize-space()='AJOUTER']").click()
        confirm_button = driver.find_element(By.XPATH, "//button[normalize-space()='Oui, JE CONFIRME']")
        confirm_button.click()
        time.sleep(4)
        len2=len(driver.find_elements(By.XPATH,"//div[contains(@class,'mb-6')]/div")) 
        time.sleep(4)        
        retour_liste=driver.find_element(By.XPATH,"//button[normalize-space()='Retour à la liste des partenaires']")
        retour_liste.click()
        time.sleep(4)
        assert len1<len2
                        
         
    def editer_info(self,driver):
        try:       
           val=driver.find_element(By.XPATH,"//a[normalize-space()='demo55']").text
        except:       
           val=driver.find_element(By.XPATH,"//a[normalize-space()='demo5']").text
        edit=driver.find_element(By.XPATH,"//tbody/tr[4]/td[7]/div[1]/button[2]")
        edit.click() 
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@name='name']").clear()
        time.sleep(2)
        return_value=""
        a=random.randint(1,50)
        if val=="demo55":
           driver.find_element(By.XPATH,"//input[@name='name']").send_keys(f"demo5{a}")
           return_value=f"demo5{a}"
        else :
           driver.find_element(By.XPATH,"//input[@name='name']").send_keys(f"demo55{a}")  
           return_value=f"demo55{a}"
        driver.find_element(By.XPATH,"//button[normalize-space()='APPLIQUER LES CHANGEMENTS']").click()
        time.sleep(2)
        try:
            popup_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
            # Locate and click the element inside the popup
            confirm_button = popup_element.find_element(By.XPATH, "//button[normalize-space()='Oui, JE CONFIRME']")
            confirm_button.click()
        except TimeoutException:
            print("Popup or element was not visible within the specified time.")        
        time.sleep(2)
        return return_value
        #if val=="demoo5":
        #    time.sleep(4)
        #    driver.find_element(By.XPATH,"//button[normalize-space()='Retour à la liste des partenaires']").click()
        #    return "demo5"
        #else :
        #    time.sleep(4)
        #    driver.find_element(By.XPATH,"//button[normalize-space()='Retour à la liste des partenaires']").click()
        #    return "demoo5"
               
                
    def ajouter_partner(self,driver):
        #partner_button = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > button:nth-child(1)")
        partner_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div/div/div/div[1]/div[2]/button[1]")
        partner_button.click()  
        a=random.randint(6,500)
        val=f"demo{a}"
        val2=f"dem{a}"
        val3=f"demo{a}@gmail.com"
        val4=f"demo{random.randint(1,500)}"
        val5=f"demo{a}@"
        val6=f"demo0{a}"
        val7=f"demo{random.randint(1,1000)}"
        driver.find_element(By.XPATH,"//input[@name='name']").send_keys(val)
        driver.find_element(By.XPATH,"//input[@name='code']").send_keys(val2)
        driver.find_element(By.XPATH,"//input[@name='email']").send_keys(val3)
        driver.find_element(By.XPATH,"//input[@name='login']").send_keys(val4)
        driver.find_element(By.XPATH,"//input[@name='password']").send_keys(val5)
        driver.find_element(By.XPATH,"//input[@name='dealerRate']").clear()
        driver.find_element(By.XPATH,"//input[@name='dealerRate']").send_keys("0.5")
        driver.find_element(By.XPATH,"//input[@name='sapCode']").send_keys(val6)
        driver.find_element(By.XPATH,"//input[@name='subPartners[0].code']").send_keys(val7)
        driver.find_element(By.XPATH,"//input[@id='gab-rc-cc']").click()
        driver.find_element(By.XPATH,"//input[@id='gab-inv-cc']").click()
        driver.find_element(By.XPATH,"//input[@id='gab-inv-acc']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[normalize-space()='AJOUTER']").click()
        try:
            popup_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']"))
            )
    
            # Locate and click the element inside the popup
            confirm_button = popup_element.find_element(
                By.XPATH, "//button[normalize-space()='Oui, JE CONFIRME']"
            )
            confirm_button.click()

        except TimeoutException:
            print("Popup or element was not visible within the specified time.")
        time.sleep(1)      
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'swal2-html-container')))
            popup_element = driver.find_element(By.ID, 'swal2-html-container')
            popup_text = popup_element.text
            return popup_text
        except Exception as e:
            print(f"An error occurred: {str(e)}")     
        #time.sleep(2)
        #driver.find_element(By.XPATH,"/html/body/div[9]/div/div[6]/button[3]").click()
        
    def telecharger_liste_part(self,driver):
        driver.find_element(By.XPATH,"//button[@data-test-id='export-button']").click()
        popup_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='dialog']")))
        popup_element.find_element( By.XPATH, "//button[normalize-space()='Oui, JE CONFIRME']" ).click()
        time.sleep(1)      
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'swal2-html-container')))
            popup_element = driver.find_element(By.ID, 'swal2-html-container')
            popup_text = popup_element.text
            return popup_text
        except Exception as e:
            print(f"An error occurred: {str(e)}")  
          

casevalues=[("gpay_user11", "Orange@2024", True)]

#@pytest.fixture
@pytest.mark.parametrize("username, password, stay_connected",casevalues) #verifier le login
def test_login(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    logger.info("connexion réussie")


@pytest.mark.parametrize("username, password, stay_connected",casevalues)  #verifier le login et logout
def test_log_logout(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url,'connexion echouée'
    cur_url=demo_log.logout(driver)
    assert cur_url==log_url ,'deconexion echouée'
    if stay_connected:
        driver.find_element(By.XPATH, "//input[@id='inputUsername']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@id='inputPassword']").send_keys(password)  
 
 
@pytest.mark.parametrize("username, password, stay_connected",casevalues) #verifier le nombre total des commandes affiche et le nombre total calcule 
def test_cmd_nbr(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url,'connexion echoué'
    commandes_page = Commandes()
    commandes_page.verify_nbrcom(driver) 
    
    
@pytest.mark.parametrize("username, password, stay_connected",casevalues) #verifier le montant total affiche et le total des montants calcule
def test_cmd_mnts(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url,'connexion echoué'
    commandes_page = Commandes()
    commandes_page.verifier_mnts(driver) 
    
            
@pytest.mark.parametrize("username, password, stay_connected",casevalues) #selectionner les commandes réussies
def test_cmd_succ(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url,'connexion echoué'
    commandes_page = Commandes()
    commandes_page.click_success(driver)  
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@class='align-middle select-none font-sans font-bold text-center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-blue-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30 flex items-center gap-1 self-end px-4 normal-case']").click()
          
@pytest.mark.parametrize("username, password, stay_connected",casevalues) #selectionner les commandes failed
def test_cmd_fail(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url,'connexion echoué'
    commandes_page = Commandes()
    commandes_page.click_failed(driver)
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@class='align-middle select-none font-sans font-bold text-center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-blue-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30 flex items-center gap-1 self-end px-4 normal-case']").click()         
        
@pytest.mark.parametrize("username, password, stay_connected",casevalues) #selectionner les commandes à rejouer
def test_cmd_repl(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url,'connexion echoué'
    commandes_page = Commandes()
    commandes_page.click_replay(driver)         
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@class='align-middle select-none font-sans font-bold text-center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-blue-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30 flex items-center gap-1 self-end px-4 normal-case']").click()    

@pytest.mark.parametrize("username, password, stay_connected",casevalues) #selectionner les commandes ambigues
def test_cmd_amb(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url,'connexion echoué'
    commandes_page = Commandes()
    commandes_page.click_ambigu(driver)         
    time.sleep(3)
    driver.find_element(By.XPATH,"//button[@class='align-middle select-none font-sans font-bold text-center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-blue-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30 flex items-center gap-1 self-end px-4 normal-case']").click()

@pytest.mark.parametrize("username, password, stay_connected",casevalues) #Ajouter un partenaire
def test_log_ajout_part(username, password, stay_connected, ):
    driver = webdriver.Chrome()
    text_ajout="Le partenaire a bien été ajouté avec succès"
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    driver.find_element(By.XPATH, "//input[@id='inputUsername']").clear()
    driver.find_element(By.XPATH, "//input[@id='inputPassword']").clear()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    if cur_url == home_url:
        assert True
        logger.info("connexion réussie")
        len1=len(driver.find_elements(By.XPATH,"//tbody/tr"))
        partner_page = Partner()
        text=partner_page.ajouter_partner(driver)
        #driver.find_element(By.XPATH,"//button[normalize-space()='RÉINITIALISER']").click()
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Retour à la liste des partenaires']")))
        element.click()
        #driver.find_element(By.XPATH,"//button[normalize-space()='Retour à la liste des partenaires']").click()
        time.sleep(3)
        len2=len(driver.find_elements(By.XPATH,"//tbody/tr"))
        if text==text_ajout:
           assert len2>len1
        #demo_log.logout(driver)
           
    elif cur_url == log_url:
        assert False
        #msg = driver.find_element(By.TAG_NAME, "p").text
        #logger.info("echec de connexion : "+msg)
    else:
        assert False, "Unexpected URL after login"


@pytest.mark.parametrize("username, password, stay_connected",casevalues)  # Editer les informations d'un partenaire
def test_editer_infopart(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url,'connexion echouée'
    demo_part = Partner()
    try: 
        if driver.find_element(By.XPATH,"//a[normalize-space()='demo5']").text == "demo5":
            nom="demo5"
    except :
        if driver.find_element(By.XPATH,"//a[normalize-space()='demo55']").text == "demo55":
           nom="demo55" 
    nom2=demo_part.editer_info(driver)
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[normalize-space()='Retour à la liste des partenaires']").click()
    time.sleep(4)
    assert nom!=nom2 ,"echec de modif"

@pytest.mark.parametrize("username, password, stay_connected",casevalues)  #desactiver partenaire
def test_desac_partner(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    logger.info("connexion réussie")
    count_prep=len(driver.find_elements(By.XPATH,"//tbody/tr"))    
    rech_part=Partner()
    count_prep2=rech_part.descativer_partner(driver)    
    assert count_prep2<count_prep,"erreur de desactivation"

@pytest.mark.parametrize("username, password, stay_connected",casevalues)  #activer partenaire
def test_activer_partner(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    count_prep=len(driver.find_elements(By.XPATH,"//tbody/tr"))    
    logger.info("connexion réussie")
    rech_part=Partner()
    count_prep2=rech_part.activer_partner(driver)    
    assert count_prep2>count_prep,"erreur de d'activation"
    

@pytest.mark.parametrize("username, password, stay_connected",casevalues)  # Recherche des partenaires prepayes
def test_rech_pre_partner(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    driver.find_element(By.XPATH, "//input[@id='inputUsername']").clear()
    driver.find_element(By.XPATH, "//input[@id='inputPassword']").clear()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    logger.info("connexion réussie")
    rech_part=Partner()
    rech_part.recherche_pre_partner(driver)
    
    
@pytest.mark.parametrize("username, password, stay_connected",casevalues)  # Recherche des partenaires postpayes
def test_rech_post_partner(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    driver.find_element(By.XPATH, "//input[@id='inputUsername']").clear()
    driver.find_element(By.XPATH, "//input[@id='inputPassword']").clear()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    logger.info("connexion réussie")
    rech_part=Partner()
    rech_part.recherche_post_partner(driver)
    
    
@pytest.mark.parametrize("username, password, stay_connected",casevalues)  #telecharger la liste des partenaires
def test_telech_partn(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    driver.find_element(By.XPATH, "//input[@id='inputUsername']").clear()
    driver.find_element(By.XPATH, "//input[@id='inputPassword']").clear()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    logger.info("connexion réussie")
    expected_msg="Le téléchargement du fichier a bien été effectué avec succès"
    rech_part=Partner()
    msg=rech_part.telecharger_liste_part(driver)
    assert msg==expected_msg


@pytest.mark.parametrize("username, password, stay_connected",casevalues)  #telecharger la liste des commandes
def test_telech_cmd(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    driver.find_element(By.XPATH, "//input[@id='inputUsername']").clear()
    driver.find_element(By.XPATH, "//input[@id='inputPassword']").clear()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    logger.info("connexion réussie")
    expected_msg="Le téléchargement du fichier a bien été effectué avec succès"
    rech_part=Commandes()
    msg=rech_part.telecharger_liste_cmd(driver)
    assert msg==expected_msg
    
    
@pytest.mark.parametrize("username, password, stay_connected",casevalues) #telecharger le rapport 
def test_telech_rapport(username, password, stay_connected): 
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    driver.find_element(By.XPATH, "//input[@id='inputUsername']").clear()
    driver.find_element(By.XPATH, "//input[@id='inputPassword']").clear()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    logger.info("connexion réussie")
    expected_msg="Le téléchargement du rapport a bien été effectué avec succès"
    rech_part=Commandes()
    msg=rech_part.telecharger_liste_rapport(driver)
    assert msg==expected_msg
    
 
@pytest.mark.parametrize("username, password, stay_connected",casevalues) #ajouter sous partenaire
def test_add_ss_partner(username, password, stay_connected):
    driver = webdriver.Chrome()
    driver.get("https://epayment-test.orange.int/login/")
    demo_log = Login_deconnexion()
    driver.find_element(By.XPATH, "//input[@id='inputUsername']").clear()
    driver.find_element(By.XPATH, "//input[@id='inputPassword']").clear()
    cur_url = demo_log.login(driver,username, password, stay_connected)
    assert cur_url == home_url
    logger.info("connexion réussie")
    add_ss_part=Partner()    
    add_ss_part.ajouter_sous_partenaire(driver)


if __name__ == "__main__":
    pytest.main()
  
  

  

