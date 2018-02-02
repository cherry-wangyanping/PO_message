
from selenium.webdriver.support.wait import WebDriverWait
class Base(object):
    #初始化driver
    def __init__(self,driver):
        self.driver = driver
    #显示等待的方法定位元素并返回（二次封装）
    def find_element(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x : x.find_element(*loc))
    #定位一组元素
    def find_elements(self, loc, timeout=5, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))
    # 点击操作方法
    def click_element(self,loc):
        self.find_element(loc).click()
    #输入元素的方法
    def input_element(self,loc,text):
        self.find_element(loc).send_keys(text)






