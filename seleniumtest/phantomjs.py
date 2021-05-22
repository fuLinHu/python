# #引入selenium
# from selenium import webdriver
#
# # 使用webkit无界面浏览器
# # 如果路径为 exe 启动程序的路径，那么该路径需要加一个 r
# driver =webdriver.PhantomJS(executable_path=r'E:/phantomjs-2.1.1-windows/bin/phantomjs.exe')
# # 获取指定网页的数据  start_urls
# driver.get('http://www.shtdsc.com/2016/tdjy/dkjs/')
#
#
# print(driver.find_element_by_tag_name("html").text)
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
#https://www.baidu.com/
#driver.get('https://www.baidu.com/')
#driver.get('http://www.shtdsc.com/2016/tdjy/dkjs/')
driver.get('http://yewu.ghzrzyw.beijing.gov.cn/gwxxfb/tdsc/tdzpgxm.html')
#//div[@id='tdcrjgTablePageDiv']/div/a[@class='layui-laypage-next']

sleep(2) #等待页面加载
print(driver.find_element_by_xpath("//div[@id='tdcrjgTablePageDiv']/div/a[@class='layui-laypage-next']").text)
# print(driver.find_element_by_tag_name("html").text)
