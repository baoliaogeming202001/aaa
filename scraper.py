from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

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

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 打开传到 tmp.link 的文件，此文件内按行写入下载界面链接
net_link_file = open("link.txt")
# 按当前时间新建文件，准备写入 界面链接 文件名 下载链接，此文件会推送到 github 本库根目录
wsd_link_file = open(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())+".txt" , "w")

line = net_link_file.readline()

while line:
    driver.get(line)
    sleep(10)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[iconpark-icon/@name='rectangle-terminal']/..")))
    element_content = element.get_attribute("innerHTML")

    lines = element_content.split('\n')
    wsd_link_file.write(line[:-1]+"\n"+driver.title+"\n"+lines[1][139:-2]+"\n\n")
    print(line[:-1]+"\n"+driver.title+"\n"+lines[1][139:-2]+"\n\n")
    line = net_link_file.readline()

net_link_file.close()
wsd_link_file.close()
