import  sys
import requests
from bs4 import BeautifulSoup

def __init__(sub_url):
    rec = requests.get(sub_url,'html.paster')
    rec.encoding='utf-8'
    BeautifulSoup(rec.text)

def get_car_info():
    print()
