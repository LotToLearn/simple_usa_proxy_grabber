import proxyscrape
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

req_proxy = RequestProxy()  # you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list()  # this will create proxy list
USA = [proxy for proxy in proxies if proxy.country == 'United States']



# ============================== proxyscrape START ============================== #
open("proxies.txt", "w").close()
collector = proxyscrape.create_collector('default', 'http')  # Create a collector for http resources
proxy = collector.get_proxies({'country': 'united states'})


for x in range(len(proxy)):
    portBefore = (str(proxy[x]).split("port='",1)[-1])
    portAfter = (str(portBefore).split("', code=")[0])
    ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(proxy[x]))
    ip = str(ip)
    rS1B = str((ip.split("['",1)[1]))
    rS2B = str((rS1B.split("']")[0]))
    ipAndPort = (rS2B + ":" + portAfter)
    with open("proxies.txt", "a") as myfile:
        myfile.write(ipAndPort + "\n")
        myfile.close()
        
# ============================== proxyscrape END ============================== #


# ============================== RequestProxy START ============================== #
badFree = " | FreeProxy"
badPrem = " | PremProxy"

for x in USA:
    with open("proxies.txt", "a") as file:
        file.write(str(x) + "\n")
        file.close()
 
# == TAKING OUT FreeProxy from line == #
with open("proxies.txt", "r") as file:
    badFreeData = file.read()
badFreeData = badFreeData.replace(badFree, "")
with open("proxies.txt", "w") as file:
    file.write(badFreeData)
# ==================================== #

# == TAKING OUT PremProxy from line == #
with open("proxies.txt", "r") as file:
    badPremData = file.read()
    badPremData = badPremData.replace(badPrem, "")
with open("proxies.txt", "w") as file:
    file.write(badPremData)
# ==================================== #

# ============================== RequestProxy END ============================== #

# ============================== PROXYSCAPE EXTENDED START ============================== #

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
url = ("https://api.proxyscrape.com/?request=share&proxytype=http&timeout=10000&country=all&ssl=all&anonymity=all")
driver.get(url)
time.sleep(5)
contents = driver.find_element_by_id('proxyshare').get_attribute('value')
with open("proxies.txt", "a") as file:
    print(contents)
    file.write(str(contents) + "\n")
    file.close()

driver.quit()

# ============================== RequestProxy END ============================== #

    
    



