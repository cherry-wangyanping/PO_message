from page_data.page_data import Page_data
from appium import webdriver
import pytest
import time
import sys ,os
sys.path.append(os.getcwd())
class Test_case(object):
    def setup_class(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "5.1"
        # 设备号
        desired_caps["deviceName"] = "192.168.128.101:5555"
        # 包名
        desired_caps["appActivity"] = ".activities.PeopleActivity"
        # 启动名
        desired_caps["appPackage"] = "com.android.contacts"
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.test_obj = Page_data(self.driver)

        print("测试开始")

    def teardown_class(self):
        self.driver.quit()
        print("测试结束")
    def test_start(self):
        self.test_obj.create_user()
    @pytest.mark.parametrize("a,b",[("小","0123456789")])
    def test_001(self,a,b):
        self.test_obj.name_input(a)
        self.test_obj.telephone_input(b)
        self.test_obj.back()
        time.sleep(5)
        self.driver.keyevent(4)
        self.driver.get_screenshot_as_file("./screen/test_001.png")
    @pytest.mark.parametrize("a,b", [("大", "9876543210")])
    def test_002(self,a,b):
        self.test_obj.new_user_create()
        self.test_obj.name_input(a)
        self.test_obj.telephone_input(b)
        self.test_obj.back()
        self.driver.get_screenshot_as_file("./screen/test_002.png")






