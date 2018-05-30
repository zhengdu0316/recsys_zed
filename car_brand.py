#encoding gbk
import  sys
import requests
from bs4 import BeautifulSoup
from car_brand_entry import BranchCar
reload(sys)
sys.setdefaultencoding('utf-8')
car_type_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']
#car_type_list = ['A']
sub_url='https://www.autohome.com.cn/grade/carhtml/{URL_TYPE}.html'
result_brand_file_dir='/Users/zhengdu/src/pycharm_workspace/python_workspace/brand.data'
result_brand_file_dir_sql='/Users/zhengdu/src/pycharm_workspace/python_workspace/brand_sql.data'

f = open(result_brand_file_dir,'w')

f_sql = open(result_brand_file_dir_sql,'w')

def car_info(index_type, sub_url):
    rec = requests.get(sub_url, 'html.paster')
    rec.encoding = 'gbk'
    soup = BeautifulSoup(rec.text)
    for list_dl in soup.select('dl'):
        if list_dl.has_key('id'):
            brand_id = list_dl['id']
        picture = 'https:' + list_dl.select('dt')[0].select('a')[0].select('img')[0]['src']
        brand_name = list_dl.select('dt')[0].select('div')[0].select('a')[0].text
        BranchCar(brand_name, brand_id, index_type, picture).print_format_str()
        f_sql.write("insert into car_brand(id,name,initial,logo) VALUES('"+brand_id+"','" + brand_name + "','" + index_type + "','" + picture + "');")
        f_sql.write('\n')
        f.writelines(str(BranchCar(brand_name,brand_id, index_type, picture).get_format_str()))
        f.write('\n')
'''
for list_dt in soup.select('dt'):
        picture = 'https:'+list_dt.select('a')[0].select('img')[0]['src']
        brand_name =list_dt.select('div')[0].select('a')[0].text
            #print(list_li.select('h4')[0].select('a')[0].text)
            #print(list_li.select('h4')[0].select('a')[0]['href'])
        
        car_brand_entry.BranchCar.branch_initial=index_type
        car_brand_entry.BranchCar.branch_name=brand_name
        car_brand_entry.BranchCar.logo = picture
        print('\t\t\t'.join([brand_name, picture]))
        
        BranchCar(brand_name,index_type,picture).print_format_str()
        f_sql.write("insert into car_brand(name,initial,logo) VALUES('"+brand_name+"','"+index_type+"','"+picture+"');")
        f_sql.write('\n')
        f.writelines(str(BranchCar(brand_name,index_type,picture).get_format_str()))
        f.write('\n')
'''

            #print(list_li)
        #print(list_ul.select('li'))
        #print(list_ul)
        #for li_list in list_ul.select('li')
        #class="interval01-list-cars-infor"
        #tab-content-item current

        #interval01-list-cars


if __name__ == "__main__":
    for index_type in car_type_list:
        car_info(index_type, sub_url.replace('{URL_TYPE}',index_type))
