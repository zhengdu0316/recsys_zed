import  sys
import requests
from bs4 import BeautifulSoup

#car_type_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
car_type_list = ['A']
sub_url='https://www.autohome.com.cn/grade/carhtml/{URL_TYPE}.html'

def car_info(sub_url):
    rec = requests.get(sub_url, 'html.paster')
    rec.encoding = 'gbk'
    soup = BeautifulSoup(rec.text)
    for list_ul in soup.select('.rank-list-ul'):
        for list_li in list_ul.select('li'):
            if len(list_li.select('h4'))>0:
                brand_name=list_li.select('h4')[0].select('a')[0].text
                brand_detail_url=list_li.select('h4')[0].select('a')[0]['href']
            #print(list_li.select('h4')[0].select('a')[0].text)
            #print(list_li.select('h4')[0].select('a')[0]['href'])
                print('\t'.join([brand_name, brand_detail_url]))
            #print(list_li)
        #print(list_ul.select('li'))
        #print(list_ul)
        #for li_list in list_ul.select('li')


if __name__ == "__main__":
    for index_type in car_type_list:
        car_info(sub_url.replace('{URL_TYPE}',index_type))
