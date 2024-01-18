import time

from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup

# 创建Edge浏览器选项
def get_csdn_message(message):
    edge_options = EdgeOptions()
    # 使用edge的驱动，设置报头
    edge_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"')
    # 使用字典根据输入转化为网页字符串
    dict={
        '服务器':'server',
        'python':'python',
        'java':'java',
        '前端':'web',
        '后端':'back-end',
    }
    str1=dict[message]
    # 拼接url
    url='https://www.csdn.net/nav/'+str1
    # 启动Edge浏览器
    browser = Edge(executable_path="E:\python\pythonProject6\edgedriver_win64/msedgedriver.exe",options=edge_options)
    browser.get(url)
    # 获取网页的HTML内容
    html = browser.page_source

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 可以使用BeautifulSoup对象来提取和处理网页中的信息
    links1 = soup.find_all('div', class_='content')
    links2 = [tag.find_all('a',target='_blank',class_='blog') for tag in links1]
    titles = soup.find_all('span', class_="blog-text")

    link_set=[]
    title_set=[]
    # 将href中链接保存到linkset列表中
    for link in links2:
        for l in link:
            link_set.append(l.get('href'))
    # 将title保存到titleset列表中
    for title in titles:
        content = title.text
        title_set.append(content)
    link_list=list(link_set)
    title_list=list(title_set)
    
    # 创建txt将两个列表中对应元素写入
    with open('csdn.txt',"a",encoding='utf-8') as f:
        for i in range(0,len(link_list)):
            str1=link_list[i]+' '+title_list[i]+'\n'
            f.write(str1)
        f.close()

if __name__=="__main__":
    print("输入csdn要爬取的内容：服务器，前端，java，python，后端。输入只可是这些")
    message=input("输入：")
    get_csdn_message(message)
    time.sleep(10)



