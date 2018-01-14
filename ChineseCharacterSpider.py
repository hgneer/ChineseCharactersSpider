import re
import os
import requests
from requests.exceptions import RequestException
from multiprocessing import Pool

def get_one_picture(picture_url):
    url = picture_url

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }

    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response
        else:
            print(response.status_code)
            return None
    except RequestException:
        print("请求出错,picture")
        return None

def get_one_character(character_url):
    url = character_url
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }

    try:
        response = requests.get(url,headers=headers)
        response.encoding = 'gbk'
        if response.status_code == 200:
            return response.text
        else:
            print(response.status_code)
            return None
    except RequestException:
        print("请求出错,character")
        return None

def get_one_page(number):
    url = "http://shufa.supfree.net/dity.asp?page=" + number.__str__()
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }

    try:
        response = requests.get(url,headers=headers)
        response.encoding = 'gbk'
        if response.status_code == 200:
            print(response.encoding)
            return response.text
        else:
            print(response.status_code)
            return None
    except RequestException:
        print("请求出错,page"+number.__str__())
        return None


def parse_one_page(html,number):
    pattern = re.compile('bblue.*?title.*?href="(.*?)".*?</a>',re.S);

    if isinstance(html,str):
        items = re.findall(pattern,html)
    else:
        return

    num_item = 0

    for item in items:
        num_item += 1
        item = "http://shufa.supfree.net/"+item
        print(item)
        html_item = get_one_character(item)
        parse_one_character(html_item,number,num_item)

def parse_one_character(html_item,number,num_item):
    pattern_character = re.compile('.*?target.*?img.*?alt.*?(.*?)</a>',re.S)

    if isinstance(html_item,str):
        items_character = re.findall(pattern_character,html_item)
    else:
        return

    if(os.path.isdir(os.curdir+'\\regular_script')):
        pass
    else:
        os.mkdir(os.curdir+'\\regular_script')

    if(os.path.isdir(os.curdir+'\\semi_cursive_script')):
        pass
    else:
        os.mkdir(os.curdir+'\\semi_cursive_script')

    if(os.path.isdir(os.curdir+'\\cursive_script')):
        pass
    else:
        os.mkdir(os.curdir+'\\cursive_script')

    if(os.path.isdir(os.curdir+'\\seal_script')):
        pass
    else:
        os.mkdir(os.curdir+'\\seal_script')

    num_regular_script_picture = 0
    num_semi_cursive_script_picture = 0
    num_cursive_script_picture = 0
    num_seal_script_picture = 0

    for item in items_character:
        if("楷书" in item):
            pattern_regular_script = re.compile('src="(.*?)"',re.S)
            if isinstance(item,str):
                items_regular_script = re.findall(pattern_regular_script,item)
            else:
                return
            for item_regular_script in items_regular_script:
                response = get_one_picture(item_regular_script)
                if (response != None):
                    if os.path.exists(os.curdir+'\\regular_script\\'+number.__str__()+'_'+num_item.__str__()+'_'+num_regular_script_picture.__str__()+'_'+'100000'+'.gif'):
                        pass
                    else:
                        with open(os.curdir+'\\regular_script\\'+number.__str__()+'_'+num_item.__str__()+'_'+num_regular_script_picture.__str__()+'_'+'100000'+'.gif','wb') as f:
                            num_regular_script_picture += 1
                            f.write(response.content)
                            f.close()
                else:
                    continue


        if("行书" in item):
            pattern_semi_cursive_script = re.compile('src="(.*?)"',re.S)
            if isinstance(item,str):
                items_semi_cursive_script = re.findall(pattern_semi_cursive_script,item)
            else:
                return
            for item_semi_cursive_script in items_semi_cursive_script:
                response = get_one_picture(item_semi_cursive_script)
                if (response != None):
                    if os.path.exists(os.curdir+'\\semi_cursive_script\\'+number.__str__()+'_'+num_item.__str__()+'_'+num_semi_cursive_script_picture.__str__()+'_'+'010000'+'.gif'):
                        pass
                    else:
                        with open(os.curdir+'\\semi_cursive_script\\'+number.__str__()+'_'+num_item.__str__()+'_'+num_semi_cursive_script_picture.__str__()+'_'+'010000'+'.gif','wb') as f:
                            num_semi_cursive_script_picture += 1
                            f.write(response.content)
                            f.close()
                else:
                    continue

        if("草书" in item):
            pattern_cursive_script = re.compile('src="(.*?)"',re.S)
            if isinstance(item,str):
                items_cursive_script = re.findall(pattern_cursive_script,item)
            else:
                return
            for item_cursive_script in items_cursive_script:
                response = get_one_picture(item_cursive_script)
                if (response != None):
                    if os.path.exists(os.curdir+'\\cursive_script\\'+number.__str__()+'_'+num_item.__str__()+'_'+num_cursive_script_picture.__str__()+'_'+'001000'+'.gif'):
                        pass
                    else:
                        with open(os.curdir+'\\cursive_script\\'+number.__str__()+'_'+num_item.__str__()+'_'+num_cursive_script_picture.__str__()+'_'+'001000'+'.gif','wb') as f:
                            num_cursive_script_picture += 1
                            f.write(response.content)
                            f.close()
                else:
                    continue


        if("篆书" in item):
            pattern_seal_script = re.compile('src="(.*?)"',re.S)
            if isinstance(item,str):
                items_seal_script = re.findall(pattern_seal_script,item)
            else:
                return
            for item_seal_script in items_seal_script:
                response = get_one_picture(item_seal_script)
                if (response != None):
                    if os.path.exists(os.curdir+'\\seal_script\\'+number.__str__()+'_'+num_item.__str__()+'_'+num_seal_script_picture.__str__()+'_'+'000100'+'.gif'):
                        pass
                    else:
                        with open(os.curdir+'\\seal_script\\'+number.__str__()+'_'+num_item.__str__()+'_'+num_seal_script_picture.__str__()+'_'+'000100'+'.gif','wb') as f:
                            num_seal_script_picture += 1
                            f.write(response.content)
                            f.close()
                else:
                    continue

def main(number):
    html = get_one_page(number)
    parse_one_page(html,number)


if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[number for number in  range(1,40)])

