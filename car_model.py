#encoding=gbk
import  sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
import json
from car_model_entry import model_entry



#car_type_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
car_type_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z']
sub_url='https://www.autohome.com.cn/grade/carhtml/{URL_TYPE}.html'

# 停售车型访问链接
drop_model_url='https://www.autohome.com.cn/ashx/series_allspec.ashx?s={BRAND_ID}&y={DROP_ID}'

result_model_dir='/Users/zhengdu/src/pycharm_workspace/python_workspace/model.data'
result_model_dir_sql='/Users/zhengdu/src/pycharm_workspace/python_workspace/model_sql.data'

car_model_detail_dir = '/Users/zhengdu/src/pycharm_workspace/python_workspace/model_detail.data'
car_model_detail_dir_sql='/Users/zhengdu/src/pycharm_workspace/python_workspace/model_detail_sql.data'
cat_all_model_url='https://car.autohome.com.cn/duibi/ashx/specComparehandler.ashx?type=1&seriesid=#{MODEL_ID}'
fd = open(result_model_dir,'w')
d_fd = open(car_model_detail_dir,'w')
model_detail_sql=open(car_model_detail_dir_sql,'w')


model_sql_fd = open(result_model_dir_sql,'w')

car_model_dict={}
car_branch_id_dict={}
branch_id_dict={}
model_id_dict={}
def car_model(sub_url):
    rec = requests.get(sub_url, 'html.paster')
    rec.encoding = 'gbk'
    soup = BeautifulSoup(rec.text)
    #print(soup.select('dl'))
    for ss in soup.select('dl'):
        if ss.has_key('id'):
            brand_id = ss['id']
        if len(ss.select('dt')) > 0:
            if len(ss.select('dt')[0].select('div')) > 0:
                if len(ss.select('dt')[0].select('div')[0].select('a')) > 0:
                    brand_name=ss.select('dt')[0].select('div')[0].select('a')[0].text
                    print('=========='+ss.select('dt')[0].select('div')[0].select('a')[0].text) # brand


        #print(ss.select('ul.rank-list-ul'))
            #print(ss.select('dt')[0])
        for i in range(len(ss.select('div.h3-tit'))):
            print("+++++"+ss.select('div.h3-tit')[i].text)  # 生产厂商
            prodution_firm=ss.select('div.h3-tit')[i].text
            li_list = ss.select('ul.rank-list-ul')[i].select('li')
            for sub_li in li_list:
                if sub_li.has_key('id'):
                    model_id= sub_li['id'][1:]
                    print(sub_li['id'])
                #if len(sub_li.select('id')) >0:
                    #print(sub_li['id'])
                if len(sub_li.select('h4')) > 0:
                    if len(sub_li.select('h4')[0].select('a')) >0:
                        print(sub_li.select('h4')[0].select('a')[0].text)
                        car_model=sub_li.select('h4')[0].select('a')[0].text
                        fd.write(model_entry(brand_name,brand_id,prodution_firm,car_model,model_id).get_format_data())
                        fd.write('\n')
                        model_sql_fd.write("INSERT INTO car_model(id,brand_id,name, full_name,production_firm,feature) VALUES ('"+model_id+"','"+brand_id+"','"+car_model+"', '"+car_model+"','"+prodution_firm+"','"+brand_name+"');")
                        model_sql_fd.write('\n')
                #for h3_tit in ss.select('div.h3-tit'):
            #print(h3_tit.text) # 生产厂商
        '''
        for list_ul in ss.select('ul.rank-list-ul'):
            for li in list_ul.select('li'):
                if len(li.select('id')) >0:
                    print(li['id'])
                if len(li.select('h4')) > 0:
                    if len(li.select('h4')[0].select('a')) >0:
                        print(li.select('h4')[0].select('a')[0].text)
        '''



def car_model_info(sub_url):
    rec = requests.get(sub_url, 'html.paster')
    rec.encoding = 'gbk'
    soup = BeautifulSoup(rec.text)
    for list_ul in soup.select('.rank-list-ul'):
        for list_li in list_ul.select('li'):
            #branch_id = str(list_li['id'])[1:]#车系ID
            #print(list_li['id'])
            #branch_id = list_li['id']

            if len(list_li.select('h4'))>0:
                model_name = list_li.select('h4')[0].select('a')[0].text # 车型
                model_name_url = 'https:'+list_li.select('h4')[0].select('a')[0]['href'] # 详情访问
                if car_model_dict.has_key(model_name):
                    continue
                else:
                    car_model_dict[model_name] = model_name_url
                    #branch_id_dict[model_name] = list_li['id']
                    model_id_dict[model_name] = list_li['id']
                print('\t'.join([model_name, model_name_url]))

# 访问车型详细信息
#

def interval01_list_cars(ss):
    return ss.select('div.interval01-list-cars-infor')[0].select('p')[0].select('a')[0].text

def car_model_detail(car_model_key , car_model_value):
    rec = requests.get(car_model_value, 'html.paster')
    rec.encoding = 'gbk'
    soup = BeautifulSoup(rec.text)
    car_model_drop_urls(car_model_key,soup)
    for tab_content_list  in soup.select('.tab-content'):
        if len(tab_content_list.select('.interval01-list')) > 0:
            for interval01_list in soup.select('.interval01-list'):
                if len(interval01_list.select('li')) >0 :
                    for li_list in interval01_list.select('li'):
                        model_detail_name = li_list.select('div.interval01-list-cars')[0].select('div.interval01-list-cars-infor')[0].select('p')[0].select('a')[0].text #车型
                        print(li_list.select('div.interval01-list-cars'))
                        print(model_detail_name)
                        guidancel = li_list.select('div.interval01-list-guidance')[0].select('div')[0].text
                        print(guidancel)
                '''
                for list_cars in interval01_list.select('.interval01-list-cars'):
                    if len(list_cars.select('.interval01-list-cars-infor')) > 0:
                        if len(list_cars.select('.interval01-list-cars-infor')[0].select('p')) > 0 :
                            if len(list_cars.select('.interval01-list-cars-infor')[0].select('p')[0].select('a')) :
                                d_fd.write('\t'.join([car_model_key, \
                                                 list_cars.select('.interval01-list-cars-infor')[0].select('p')[0].select('a')[
                                                     0].text]))
                                d_fd.write('\n')
                                print('\t'.join([car_model_key, \
                                                 list_cars.select('.interval01-list-cars-infor')[0].select('p')[0].select('a')[
                                                     0].text]))
                '''
drop_list=[]
drop_model_dict={}
def car_model_drop_urls(car_model_key,soup):
    if len(soup.select('div.dropdown.cartype-sale-list.fn-hide'))>0:
        for drop_li in soup.select('div.dropdown.cartype-sale-list.fn-hide')[0].select('li'):
            #print(drop_li.select('a')[0]['data'])
            #drop_list.append(drop_li.select('a')[0]['data'])
            branch_id = branch_id_dict[car_model_key][1:]
            yesrs = drop_li.select('a')[0].contents
            drop_li.select('a')[0]['data']
            drop_model_dict[car_model_key+"_"+drop_li.select('a')[0]['data']] = drop_model_url.replace('{BRAND_ID}', branch_id).replace('{DROP_ID}', drop_li.select('a')[0]['data'])




def car_drop_views(car_modek_key,car_drop_value):
    r = requests.get(car_drop_value)
    json_response = r.text
    dict_json = json.loads(json_response)
    drop_list = dict_json['Spec']
    for ss in drop_list:
        print '\t'.join([car_modek_key,ss['Name']])
    #print(dict_json)


def car_all_model(car_model,model_id,car_drop_value):
    r = requests.get(car_drop_value)
    json_response = r.text
    dict_json = json.loads(json_response)
    ll = dict_json['List']
    for li in ll:
        index = str(li['I'])
        name = str(li['N'])
        #print('\t'.join([index,name]))
        sub_all_list = li['List']
        for sub in sub_all_list:
            sub_i = str(sub['I'])
            sub_n = str(sub['N'])
            sub_p = str(sub['P'])
            d_fd.write('\t'.join([car_model,index,name,sub_i, sub_n, sub_p]))
            d_fd.write('\n')
            model_detail_sql.write("insert into car_detail(id,model_id,name,price,size_type,feature) VALUES('"+sub_i+"','"+model_id+"','"+sub_n+"','"+sub_p+"','"+index+"','"+car_model+"');")
            model_detail_sql.write('\n')
            print('\t'.join([sub_i,model_id,sub_n,sub_p,index,car_model]))

if __name__ == "__main__":
    #car_all_model('https://car.autohome.com.cn/duibi/ashx/specComparehandler.ashx?type=1&seriesid=3170')

    for index_type in car_type_list:
        car_model(sub_url.replace('{URL_TYPE}', index_type))
        #car_model_info(sub_url.replace('{URL_TYPE}',index_type))


    '''
    for model_name,model_id in model_id_dict.items():
        #ss= 'https: // car.autohome.com.cn / duibi / ashx / specComparehandler.ashx?type = 1 & seriesid ='+brand_id[1:]
        car_all_model(model_name,model_id[1:],'https://car.autohome.com.cn/duibi/ashx/specComparehandler.ashx?type=1&seriesid='+model_id[1:])

   
    print('====================================')
    for car_model_key, car_model_value in car_model_dict.items():
        car_model_detail(car_model_key,car_model_value)
        print("----------------------z")
       
    for car_modek_key,car_drop_value in drop_model_dict.items():
        car_drop_views(car_modek_key,car_drop_value)
        '''
