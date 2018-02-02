from base_data.base_data import Base
import page_data

class Page_data(Base):

    def __init__(self,driver):
        Base.__init__(self,driver)
        self.driver = driver
    def create_user(self):
        #新建联系人
        self.click_element(page_data.new_user_create_button)
        #保存到本地
        self.click_element(page_data.save_local_button)

    def name_input(self,text):
        #输入姓名
        self.input_element(page_data.name_button,text)
    def telephone_input(self,text):
        self.input_element(page_data.telephone_button,text)
    def back(self):
        self.click_element(page_data.back_button)
    def new_user_create(self):
        self.click_element(page_data.new_user_create_button)




