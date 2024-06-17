from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
#driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
#         chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

sleep_time = 20
driver_list = []
driver_numb = 10
count = 0
while ( count < driver_numb):
   #driver_list.append( webdriver.Chrome(service=chrome_service, options=chrome_options) )
    driver_list.append( webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()) , options=chrome_options ) )
    count = count + 1

net_link_file = open("link.txt")
wsd_link_file = open(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())+".txt" , "w")

line = net_link_file.readline().strip('\n')

while line:
    count = 0
    num = 0
    output_line = []
    while ( count < driver_numb):
        if line:
            output_line.append(line)
            driver_list[count].get(line)
            num = num + 1
        line = net_link_file.readline().strip('\n')
        count = count + 1
    sleep(sleep_time)

    count1 = 0
    while ( count1 < num):
        element = WebDriverWait(driver_list[count1], 10).until(EC.presence_of_element_located((By.XPATH, "//button[iconpark-icon/@name='rectangle-terminal']/..")))
        element_content = element.get_attribute("innerHTML")
        lines = element_content.split('\n')
        output = output_line[count1]+"\n"+driver_list[count1].title+"\n"+lines[1][139:-2]+"\n\n"
        wsd_link_file.write(output)
        print(output)
        count1 = count1 + 1

net_link_file.close()
wsd_link_file.close()
