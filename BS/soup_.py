################################################################################
# Parsing HTML using Beautiful Soup
################################################################################
# This pogram abuses the style of text to extract either red or green parts.

from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd


# At first, open the page below in a browser of your choice.
# Second, look how the code is constructed - view source in a browser.

# We download the code as before:
url = 'https://www.shopclues.com/branded-deals.html'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

# And we can display it in python:
print(bs)
#
# Beautiful Soup 'find_all' method allows to create list of tags by class in Smartphones category:

product_name = bs.find_all('span', {'class': 'prod_name'})
for name in product_name:
    print(name.get_text())

product_price = bs.find_all('span', {'class': 'p_price'})
for name in product_price:
    print(name.get_text())

product_discount = bs.find_all('span', {'class': 'prd_discount'})
for name in product_discount:
    print(name.get_text())


from bs4 import BeautifulSoup as bs
import requests
import os
# product images
prod_img = 'https://www.shopclues.com/branded-deals.html'
r = requests.get(prod_img)
img = bs(r.text, 'html.parser')

images = img.find_all('img')

print(images)

# Game Consoles category

url1 = 'https://www.shopclues.com/computer-games-gaming-consoles.html'
html1 = re.urlopen(url1)
bs1 = BS(html1.read(), 'html.parser')

# To display it in Python

print(bs1)


console_name = bs.find_all('span', {'class': 'prod_name'})
for name in console_name:
    print(name.get_text())

console_price = bs.find_all('span', {'class': 'p_price'})
for name in console_price:
    print(name.get_text())

console_discount = bs.find_all('span', {'class': 'prd_discount'})
for name in console_discount:
    print(name.get_text())

# Game consoles images
from bs4 import BeautifulSoup as bs
import requests
import os

console_img = 'https://www.shopclues.com/computer-games-gaming-consoles.html'
r1 = requests.get(console_img)
cons_img = bs(r.text, 'html.parser')

cons_images = cons_img.find_all('img')

print(cons_images)


# Laptops category

url2 = 'https://www.shopclues.com/laptops.html'
html2 = re.urlopen(url2)
bs = BS(html2.read(), 'html.parser')

laptop_name = bs.find_all('span', {'class': 'prod_name'})
for name in laptop_name:
    print(name.get_text())

laptop_price = bs.find_all('span', {'class': 'p_price'})
for name in laptop_price:
    print(name.get_text())

laptop_discount = bs.find_all('span', {'class': 'prd_discount'})
for name in laptop_discount:
    print(name.get_text())


# Laptop images
laptop_img = 'https://www.shopclues.com/computer-games-gaming-consoles.html'
r2 = requests.get(laptop_img_img)
laptop_img = bs(r.text, 'html.parser')

laptop_images = laptop_img.find_all('img')

print(laptop_images)

laptop_images.to_csv('laptop_image')
# Instead of displaying it one by one we might use list comprehension to put
# them into new list and pandas data frame:
# name_list = [name.get_text() for name in product_name]
# # bold_list = [bold.get_text() for bold in bs_bold]
# # The data can be put into data frame, later into .csv file.
# d = pd.DataFrame(name_list + bold_list)
# print(d)
# print(title)
# print(bs_footer)


