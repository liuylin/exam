'''
import urllib.request
response = urllib.request.urlopen("http://www.baidu.com")
html = response.read()
html = html.decode("utf-8")
print(html)
'''

'''
import urllib.request
response = urllib.request.urlopen('http://placekitten.com/500/600')
cat_img = response.read()

with open('cat.jpg','wb')as f:
    f.write(cat_img)

print(response.geturl()) #获取链接地址
print(response.info())
'''

#爬取有道翻译
'''
import json
import urllib.request
import urllib.parse
import time

while True:
    content = input("请输入需要翻译的内容：（输入'q'退出程序）\n")
    if content == 'q':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    #head = {}
    #head['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"

    data = {}
    data['i'] =  content
    data['from'] = 'AUTO'
    data['to'] =  'AUTO'
    data['smartresult'] = 'dict'
    data['client']= 'fanyideskweb'
    data['salt'] = '1522810548560'
    data['sign']  = '1c3052fed220e88ca910ac44dedd91ea'
    data['doctype'] = 'json'
    data['version']  = '2.1'
    data['keyfrom']  = 'fanyi.web'
    data['action']  = 'FY_BY_REALTIME'
    data['typoResult']  = 'false'

    data = urllib.parse.urlencode(data).encode('utf-8')

    #req = urllib.request.Request(url,data,head)
    req = urllib.request.Request(url,data)
    req.add_header('User-Agent',"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')

    #print(html)
    target = json.loads(html)
    print('翻译结果 %s' % (target['translateResult'][0][0]['tgt']))
    time.sleep(2)
'''

#使用代理
import urllib.request

url = "http://www.whatismyip.com.tw"
proxy_support = urllib.request.ProxyHandler({'http':'58.240.53.196:8080'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)











