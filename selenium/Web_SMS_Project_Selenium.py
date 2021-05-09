from selenium import webdriver
import time
import pandas as pd
gecko_path = 'C:\\Users\\yenis\\Desktop\\Web_SMS\\project WEB_SCPY\\geckodriver.exe'

url = 'https://www.shopclues.com/'
options = webdriver.firefox.options.Options()
options.headless = False

driver = webdriver.Firefox(options = options, executable_path = gecko_path)

driver.get(url)

dil = pd.DataFrame({"Brand":[], "Price":[], "Discount":[]})

shows=driver.find_elements_by_xpath("//div//a[@class='Smartphones & Tablets']")

links=[link.get_attribute('href') for link in shows]
print(links)
for link in links:
    print(link)
    print("###################")
    driver.get(link)
    time.sleep(1)


    try:

        brand = driver.find_element_by_xpath("//div//li//a[@class='Brand']", 'https://www.shopclues.com/').text
        print(brand)
    except:

        print("Not Found")

    try:

        price = driver.find_element_by_xpath("//div//li//a[@class='Price']", 'https://www.shopclues.com/').text
        print(price)
    except:
        print("Not Found")

    try:

        discount = driver.find_element_by_xpath("//div//li//a[@class='Discount']", 'https://www.shopclues.com/').text
        print(discount)
    except:
        print("Not Found")


        shop = {"Brand": brand, "Price": price, "Discount":discount}

        dil=d.append(shop, ignore_index = True)

dil.to_csv('SSS.csv')

start = time.time()
print("Running time: ",time.time() - start)
