import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

homepage = requests.request(
    method='get',
    url='https://wx.qq.com/',
)

soup_homepage = BeautifulSoup(homepage.text, features='lxml')
img_QR = soup_homepage.find(name='img')
print(img_QR, '\n', type(img_QR))