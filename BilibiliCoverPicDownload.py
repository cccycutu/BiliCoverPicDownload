import requests
import random
import string
import os


def bilibili_download(space_id):
    url = f'https://api.bilibili.com/x/space/arc/search?mid={space_id}&pn=1&ps=50&index=1&jsonp=jsonp'
    myheaders = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87'
                          '.0.4280.88 Safari/537.36'}
    file_path = './pic/'
    res = requests.get(url=url, headers=myheaders)
    count = res.json()['data']['page']['count']

    if 0 < count <= 50:
        max = 1
    elif count <= 100:
        max = 2
    elif count <= 150:
        max = 3
    elif count <= 200:
        max = 4
    elif count <= 250:
        max = 5
    elif count <= 300:
        max = 6
    elif count <= 350:
        max = 7
    elif count <= 400:
        max = 8
    elif count <= 450:
        max = 9
    else:
        max = 10

    for i in range(1, max+1):  # range包前不包后，（1，1）什么都没有，（1，2）才是1，所以需要+1。
        myurl = f'https://api.bilibili.com/x/space/arc/search?mid={space_id}&pn={i}&ps=50&index=1&jsonp=jsonp'
        res = requests.get(url=myurl, headers=myheaders)
        pic_urls = []
        for url in res.json()['data']['list']['vlist']:
            pic_url = url['pic']
            pic_urls.append(pic_url)
        if not os.path.exists(file_path):
            os.mkdir(file_path)
        print(f'---------------------封面一共有{count}张----------------')
        print(f'------------------当前正在下载第{i}/{max}页------------------')
        for num in range(0, len(pic_urls)):
            print(f'正在下载第{50*(i-1)+num+1}张图片')
            filename = ''.join(random.sample(string.ascii_letters + string.digits, 16))  # 数字 加 随机文件名
            open(f'{file_path}{str(50*(i-1)+num+1)+"_"+filename}.jpg', 'wb').write(requests.get(pic_urls[num]).content)


if __name__ == '__main__':
    # space_id
    bilibili_download(454228982)
