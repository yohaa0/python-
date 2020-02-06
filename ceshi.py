import requests
import json
import time
import hashlib
import xlwt

# 获取as和cp参数的函数
def get_as_cp_args():
    zz ={}
    now = round(time.time())
    print (now)  # 获取计算机时间
    e = hex(int(now)).upper()[2:]  # hex()转换一个整数对象为十六进制的字符串表示
    print (e)
    i = hashlib.md5(str(int(now)).encode("utf8")).hexdigest().upper() # hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    if len(e)!=8:
        zz = {'as': "479BB4B7254C150",
            'cp': "7E0AC8874BB0985"}
        return zz
    n=i[:5]
    a=i[-5:]
    r = ""
    s = ""
    for i in range(5):
        s = s+n[i]+e[i]
    for j in range(5):
        r = r+e[j+3]+a[j]
    zz = {
            'as': "A1" + s + e[-3:],
            'cp': e[0:3] + r + "E1"
        }
    print (zz)
    return zz

#获取解析json后的数据
def get_html_data(target_url):
    # 这里你换成你自己的请求头。直接复制代码，会报错！！！
    headers = {"referer": "https://www.toutiao.com/",
               "accept": "text/javascript, text/html, application/xml, text/xml, */*",
               "content-type": "application/x-www-form-urlencoded",
               "cookie": "tt_webid=6774555886024279565; s_v_web_id=76cec5f9a5c4ee50215b678a6f53dea5; WEATHER24279565; csrftoken=bb8c835711d848db5dc5445604d0a9e9; __tasessionId=gphokc0el1577327623076",
               "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    response = requests.get(target_url, headers=headers)
    res_data = json.loads(response.text)
    return res_data

# 解析数据，提取相关的字段
def get_parse_data(max_behot_time, base_url, start_url,):
    # 存放所有的今日头条新闻数据
    excel_data = []
    
    # 循环次数,相当于于刷新新闻的次数，正常情况下刷新一次会出现10条新闻，但也存在少于10条的情况；所以最后的结果并不一定是10的倍数
    for i in range(3):
        # 获取as和cp参数的函数
        as_cp_args = get_as_cp_args()  
        # 拼接请求路径地址
        targetUrl = start_url + max_behot_time + '&max_behot_time_tmp=' + max_behot_time + '&tadrequire=true&as=' + as_cp_args['as'] + '&cp=' + as_cp_args['cp']
        res_data = get_html_data(targetUrl)
        time.sleep(1)
        toutiao_data = res_data['data']
        for i in range(len(toutiao_data)):
            toutiao = []
            toutiao_title = toutiao_data[i]['title']                            # 头条新闻标题
            toutiao_source_url = toutiao_data[i]['source_url']                  # 头条新闻链接
            if "https" not in toutiao_source_url:
                toutiao_source_url = base_url + toutiao_source_url
            toutiao_source = toutiao_data[i]['source']                          # 头条发布新闻的来源
            toutiao_media_url = base_url + toutiao_data[i]['media_url']         # 头条发布新闻链接
            toutiao.append(toutiao_title)
            toutiao.append(toutiao_source_url)
            toutiao.append(toutiao_source)
            toutiao.append(toutiao_media_url)
            excel_data.append(toutiao)
            print(toutiao)
    # 获取下一个链接的max_behot_time参数的值
    max_behot_time = str(res_data['next']['max_behot_time'])

    return excel_data

# 数据保存到Excel 表格中中
def save_data(excel_data):
    header = ["新闻标题", "新闻链接", "头条号", "头条号链接"]
    excel_data.insert(0, header)

    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)
    for i in range(len(excel_data)):
        for j in range(len(excel_data[i])):
            worksheet.write(i, j, excel_data[i][j])
    workbook.save(r"今日头条热点新闻.xls")
    print("今日头条新闻保存完毕！！")


if __name__ == '__main__':
    # 链接参数
    max_behot_time = '0'
    # 基础地址
    base_url = 'https://www.toutiao.com'
    # 请求的前半部分地址
    start_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time='
    toutiao_data = get_parse_data(max_behot_time, base_url, start_url)
    save_data(toutiao_data)
