#爬取京东页面图片  未成功
'''
import re
import urllib.request
import urllib.error

def craw(url,page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0]
    pat2 = '<img width="220" height="220" data-img="1" src="//(.+?\.jpg">'
    imagelist=re.compile(pat2).findall(result1)
    x = 1
    for imageurl in imagelist:
        imagename = str(page)+str(x)+".jpg"#页数+顺序号+.jpg
        imageurl = "http://"+ imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                x += 1
            if hasattr(e,"reason"):
                x += 1
    x += 1
for i in range(1,10):
    url = "http://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)
'''


'''
#获取csdn博客的所有链接
import re
import urllib.request
def getlink(url):
    #模拟浏览器
    headers = ('User-Agent','User-Agent: Mozilla/5.0\
     (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
      Chrome/65.0.3325.181 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener构建为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    #根据需求构建好链接表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    #去除重复链接
    link = list(set(link))
    return link
url = "https://blog.csdn.net/ChaseRaod/article/list/2"
linklist = getlink(url)
#通过for循环分别遍历输出获取到的链接地址到屏幕上
for link in linklist:
    print(link[0])
'''

#爬取内涵段子  未成功
'''
import urllib.request
import re
def getcontent(url,page):
    #模拟成浏览器
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    userpat = 'target="_blank" onclick="(.*?)">'
    contentpat = '<div class="content">(.*?) </div>'
    userlist = re.compile(userpat,re.S).findall(data)
    contentlist = re.compile(contentpat,re.S).findall(data)
    x = 1
    for content in contentlist:
        content = content.replace('\n',"")
        # 用字符串作为变量名，先将对应字符串付给一个变量
        name = "content"+str(x)
        #通过exec函数实现用字符串作为变量名并赋值
        exec(name+'=content')
        x += 1
    y = 1
    #通过for循环遍历用户，并输出该用户对应的内容
    for user in userlist:
        name = 'content'+str(y)
        print("用户"+str(page)+str(y)+"是："+user)
        print('内容是：')
        exec("print('+name+')")
        print("\n")
        y+=1
#分别获取各页的段子，通过for循环可以获取多页
for i in range(1,30):
    url="http://www.qiushibaike.com/8hr/page"+str(i)
    getcontent(url,i)
'''


'''
import re
import urllib.request
import random
def getlink(url):
    #模拟浏览器
    headers = ('User-Agent','User-Agent: Mozilla/5.0\
     (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
      Chrome/65.0.3325.181 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #将opener构建为全局
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    #根据需求构建好链接表达式
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    #去除重复链接
    link = list(set(link))
    return link
url = "https://blog.csdn.net/ChaseRaod/article/list/2"
linklist = getlink(url)
for link1 in linklist:
    addr = link1[0]
    req = urllib.request.Request(addr)
    data = urllib.request.urlopen(req).read()
    print(len(data))
'''

