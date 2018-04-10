
'''
import re
res = re.search(r'you','I love you')
res2 = re.search(r'lo.','I love. you')#匹配除换行符之外的任何字符
res3 = re.search(r'\.','I love. you')#匹配点
res4 = re.search(r'\d\d\d','I love. 123 you')
res5 = re.search(r'[aeiouAEIOU]','I love 123 you')
res6 = re.search(r'[a-z]','I love. 123 you')
res7 = re.search(r'[1-9]','I love. 123 you')
res8 = re.search(r'ab{3}c','abbbc')
res9 = re.search(r'ab{3,10}c','abbbbbc')
res10 = re.search(r'[01]\d\d|2[0-4]\d|25[0-5]','188')#在0-255中匹配188
res11 = re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.)'
                  r'{3}[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5]',
                  '192.168.1.1')#{0,1}表示可有可无，重复0次或一次
print(res)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)
print(res8)
print(res9)
print(res10)
print(res11)


import urllib.request

file = urllib.request.urlretrieve('http://edu.51cto.com',filename='1.html')
urllib.request.urlcleanup()


import urllib.request
ret = urllib.request.quote('http://www.sina.com.cn')
print(ret)
ret1 = urllib.request.unquote('http%3A//www.sina.com.cn')
print(ret1)
'''

'''

while True:
    import urllib.request
    url = 'https://blog.csdn.net/chaseraod/article/details/79780111'
    headers = ('User-Agent','Mozilla/5.0\
     (Windows NT 10.0; WOW64) AppleWebKit/537.36\
      (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read()
    fhandle = open('1.html','wb')
    fhandle.write(data)
    fhandle.close()
'''

'''
import urllib.request
import time
import random
while True:
    try:
        list1 = ['https://blog.csdn.net/chaseraod/article/details/79719571',
                 'https://blog.csdn.net/chaseraod/article/details/79660484',
                 'https://blog.csdn.net/chaseraod/article/details/79673645',
                 'https://blog.csdn.net/chaseraod/article/details/79717393',
                 'https://blog.csdn.net/chaseraod/article/details/79647523',
                 'https://blog.csdn.net/chaseraod/article/details/79338215',
                 'https://blog.csdn.net/chaseraod/article/details/79342897']
        req = urllib.request.Request(random.choice(list1))
        req.add_header('User-Agent','Mozilla/5.0\
         (Windows NT 10.0; WOW64) AppleWebKit/537.36\
          (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
        data = urllib.request.urlopen(req).read()
        print(len(data))
    except Exception as e:
        print('出现异常--->'+str(e))
'''


'''

import urllib.request
keywd = 'ChaseRoad'
url = "http://www.baidu.com/s?wd="+keywd
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhandle = open('hh.html','wb')
fhandle.write(data)
fhandle.close()
'''

'''
import urllib.request
url = "http://www.baidu.com/s?wd="
keywd = '刘宇琳'
keycode = urllib.request.quote(keywd)
req = urllib.request.Request(url+keycode)
data = urllib.request.urlopen(req).read()
fhandle = open('2.html','wb')
fhandle.write(data)
fhandle.close()
'''

'''
def use_proxy(proxy_addr,url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http':proxy_addr})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr = '203.174.11.13:3128'
data = use_proxy(proxy_addr,'http://www.baidu.com')
print(len(data))
'''

#开启Debuglog
'''
import urllib.request
httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
daat = urllib.request.urlopen('http://edu.51cto.com')
'''

'''
import urllib.request
import urllib.error
try:
    html = urllib.request.urlopen("http://blog.csdn.net")
    print(html)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print(e.reason)
'''
''''
#改进整合版
import urllib.request
import urllib.error
try:
    url = "http://zsxx.sust.edu.cn"
    headers = ('User-Agent', 'Mozilla/5.0\
        (Windows NT 10.0; WOW64) AppleWebKit/537.36\
         (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    req = urllib.request.Request(url)
    data = urllib.request.urlopen(req).read()
    f = open('sust.html', 'wb')
    f.write(data)
    f.close()
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)
'''

#正则表达式
'''
#（1）普通字符作为原子
import re
pattern = "yue"
string = 'http://yum.iqianyue.com'
result = re.search(pattern,string)
print(result)
'''
'''
#（2）非打印字符作为原子
import re
pattern = '\n'
string = 'http://yum.iqianyue.com
http://baidu.com'
result = re.search(pattern,string)
print(result)
'''

'''
#（3）通用字符作为原子
import re
pattern = '\w\dpython\w'
string = 'abcdfphp345python_py'
result = re.search(pattern,string)
print(result)
'''

'''
#（4）原子表
import re
pattern1 = '\w\dpython[xyz]\w'
pattern2 = '\w\dpython[^xyz]\w'
pattern3 = '\w\dpython[xyz]\W'
string = 'abcdfphp345pythony_py'
resutlt1 = re.search(pattern1,string)
resutlt2 = re.search(pattern2,string)
resutlt3 = re.search(pattern3,string)
print(resutlt1)
print(resutlt2)
print(resutlt3)
'''

'''
#元字符
#（1）任意匹配元字符
import re
pattern = ".python..."
string = 'abcdfphp345pythony_py'
result = re.search(pattern,string)
print(result)
'''

'''
#（2）边界限制元字符
import re
pattern1 = '^abd'
pattern2 = '^abc'
pattern3 = 'py$'
pattern4 = 'ay$'
string = 'abcdfphp345pythony_py'
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
result3 = re.search(pattern3,string)
result4 = re.search(pattern4,string)
print(result1)
print(result2)
print(result3)
print(result4)
'''
#（3）限定符
'''
import re
pattern1 = 'py.n'
pattern2 = 'cd{2}'
pattern3 = 'cd{3}'
pattern4 = 'cd{2,}'
string = 'abcdddfphp34pythony_py'
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
result3 = re.search(pattern3,string)
result4 = re.search(pattern4,string)
print(result1)
print(result2)
print(result3)
print(result4)
'''

'''
#（4）模式选择符
import re
pattern = 'python|php'
string = 'abcdphp345pythony_py'
result = re.search(pattern,string)
print(result)
'''

'''
#（5）模式单元符
import re
pattern1 = '(cd){1,}'
pattern2 = 'cd{1,}'
string = 'abcdcdcdfphp34pythony_py'
result = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result)
print(result2)
'''

'''
#模式修正
import re
pattern1 = 'python'
pattern2 = 'python'
string = 'abcdfphp345Pythonp_py'
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string,re.I)
print(result1)
print(result2)
'''

'''
#贪婪模式与懒惰模式
import re
pattern1 = 'p.*y'#贪婪模式
pattern2 = 'p.*?y'#懒惰模式
string = 'abcdfphp345pythonp_py'
result1 = re.search(pattern1,string)
result2 = re.search(pattern2,string)
print(result1)
print(result2)
'''

'''
#re.match函数
#从源字符串的起始位置匹配一个模式
import re
string = 'apythonhellomypythonhispythonourpythonend'
pattern = '.python'
result = re.match(pattern,string)
result1 = re.match(pattern,string).span()#直接返回匹配的位置
print(result)
print(result1)
'''

'''
#re.search函数
import re
string = 'hellomypythonhispythonourpythonend'
pattern = '.python'
result = re.match(pattern,string)
result2 = re.search(pattern,string)
print(result)
print(result2)
'''

'''
#全局匹配函数
#（1）使用re.compile()对正则表达式进行预编译
#（2）编译后，使用findall()根据正则表达式从源字符串中将匹配的结果全部找出
import re
string = 'hellomypythonhispythonourpythonend'
pattern = re.compile('.python.')
result = pattern.findall(string)
print(result)
'''

'''
#整合
import re
string = 'hellomypythonhispythonourpythonend'
pattern = '.python.'
result = re.compile(pattern).findall(string)
print(result)
'''

'''
#re.sub函数
#根据正则表达式来实现替换某些字符串的功能
#re.sub(pattern,rep,string,max)
import re
string = 'hellomypythonhispythonourpythonend'
pattern = 'python.'
result = re.sub(pattern,'php',string)#全部替换
result2 = re.sub(pattern,'php',string,2)#最多替换两次
print(result)
print(result2)
'''

'''
#匹配.com或.cn后缀的url网址
import re
pattern = '[a-zA-Z]+://[^\s]*[.com|.cn]'
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern,string)
print(result)
'''

'''
#匹配电话号码
import re
pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
string = '021-672826365385382265236'
result = re.search(pattern,string)
print(result)
'''

#匹配电子邮件地址
import re
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
string = "<a href='http://www.baidu.com'>百度首页\
</a?<br><a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件地址</a>"
result = re.search(pattern,string)
print(result)









