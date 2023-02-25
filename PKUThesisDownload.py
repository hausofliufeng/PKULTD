import os
import re
import time
import datetime
import requests
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# option = webdriver.ChromeOptions()
# option.add_argument('--user-data-dir=/Users/liufeng/Library/Application Support/Google/Chrome') # 设置成自己的数据目录
# option.add_argument(" --profile-directory=Default")

# driver = webdriver.Chrome("./chromedriver",options=option)

driver = webdriver.Chrome("./chromedriver")
time.sleep(30)

#论文链接
thsis_url="https://drm.lib.pku.edu.cn/pdfindex.jsp?fid=d349749648fb6cffc255fd00f09eac56"
driver.get(thsis_url)
driver.refresh()
time.sleep(2)
# lookbut = driver.find_element_by_link_text('查看全文')
# lookbut.click()
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# time.sleep(2)
# #获取总页数
tpage=driver.find_element_by_css_selector('span#totalPages.toolbar-page-num')
total_pages=int(re.sub("\D","",tpage.get_attribute("innerText")))
print('本论文总页数为：%d 页'%(total_pages))
total_pages=int(total_pages)
#下载论文
os.makedirs('./thsis_image/', exist_ok=True)
i=0
find_page=False
while i<total_pages:
    div_name='div#loadingBg%d.loadingbg > img'%(i)
    try:
        pics = driver.find_element_by_css_selector(div_name)
        find_page=True
        img_url=pics.get_attribute('src')
    except:
        find_page=False
    if find_page:
        print('找到第%d页...'%(i+1))
        #print(img_url)
        i=i+1
        urlretrieve(img_url, './thsis_image/img%d.jpg'%(i))
    else:
        btnext=driver.find_element_by_css_selector('a#btnnext.toobar-btn.toobar-btn-next')
        btnext.click()
        time.sleep(0.5)
print('文章下载完成！')