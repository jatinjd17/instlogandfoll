import time, os
import random
import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from pymongo import MongoClient


options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('--disable-popup-blocking')
#bot = uc.Chrome(options=options)
# ua = UserAgent()
# userAgent = ua.random
# print(userAgent)
# options.add_argument('--window-size=1920,1080')
#options.add_argument("--start-maximized")
#options.add_argument("--disable-blink-features=AutomationControlled")


# Exclude the collection of enable-automation switches
#options.add_experimental_option("excludeSwitches", ["enable-automation"])

# Turn-off userAutomationExtension
#options.add_experimental_option("useAutomationExtension", False)
# options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36')
# options.add_argument(f'user-agent=Chrome/113.0.0.0')
#options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')
# # options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--log-level=3")
# options.add_argument(r"--user-data-dir=C:\Users\jatin\AppData\Local\Google\Chrome\User Data") 
# options.add_argument(r"--user-data-dir=C:\Users\student_00_fc1ec9f2e\AppData\Local\Google\Chrome\User Data") 
	
#e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# options.add_argument('profile-directory=Default')
# options.add_argument('--window-size=1920,1080')
#options.add_argument("--headless")
time.sleep(2)
client = MongoClient(host="mongodb+srv://jatin:jatin123@cluster0.1zrdh.mongodb.net/outlookmail?retryWrites=true&w=majority",connect=False)

def RunScript():
    collection5 = client.get_database("outlookmail").get_collection("instacreatedemails")
    collection6 = client.get_database("outlookmail").get_collection('instacreatedemailsafterlogin')

    

  
    # totallines = len(lines)
    totallines = 6
    count = 0



    # print((names.get_first_name(gender='male')+'_'+names.get_last_name()).lower()+str(random.randrange(7598,100000))+'@outlook.com')

    try:
        while count < totallines:

            try:
                a = collection5.find_one_and_delete({})
                emaill = a['email']
                print(a['email'])   

                #############NEW##################
                #bot = webdriver.Chrome(chrome_options=options)
		bot = uc.Chrome(options=options)

                bot.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                ################################

                print(lines[count])

                time.sleep(5)
                

                bot.get('https://www.instagram.com/')
                time.sleep(3)
            
                # time.sleep(4)

                WebDriverWait(bot,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(emaill)

                WebDriverWait(bot,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))).send_keys('Jatin@123')

                WebDriverWait(bot,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]'))).click()

                try:
                    WebDriverWait(bot,6).until(EC.presence_of_element_located((By.XPATH, '//p[contains(text(),"There was a problem logging you in to Instagram. Please try again soon.")]')))

                    WebDriverWait(bot,1).until(EC.presence_of_element_located((By.XPATH, '//p[contains(text(),"There was a problem with logging you in to Instagram. Please try again soon.")]')))


                    print('Limit DOne!!!!!!!! Breaking loop')

                    break
                except:
                    pass


                WebDriverWait(bot,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="New post"]')))
                # bot.find_element(By.XPATH, '//*[@id="MemberName"]').send_keys(email)

                bot.get('https://www.instagram.com/codex_jd/')


                print('likeing!!!!!!!!')


                WebDriverWait(bot,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1i64zmx.x1n2onr6.x1plvlek.xryxfnj.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > button._acan._acap._acas._aj1-'))).click()

                print('Liked!!!!!!!!')


                time.sleep(6)

                # WebDriverWait(bot,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Settings"]')))

                
                count = count + 1

                data = {'email': emaill, 'follow': 'true'}

                collection6.insert_one(data)
                ######NEW#####
                bot.quit()
                ##############
            except Exception as e:
                data = {'email': emaill, 'follow': 'false'}

                collection6.insert_one(data)
                ##########NEW#########
                count = count + 1
                bot.quit()
                continue
            #######################
               


        print('Doneee!!!!!!!!!!!!!!!!')
        # time.sleep(1)

        


         
        time.sleep(50000)
        bot.quit()
    except Exception as e:
        print(e)
        time.sleep(10000)



if __name__ == "__main__":
    RunScript()
