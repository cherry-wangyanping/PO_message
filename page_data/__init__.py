from selenium.webdriver.common.by import By
#新建联系人按钮
create_user_button = (By.ID,"com.android.contacts:id/create_contact_button")
#保存本地按钮
save_local_button = (By.ID,"com.android.contacts:id/left_button")
#姓名栏
name_button = (By.XPATH,"//*[contains(@text,'姓名')]")
#电话栏
telephone_button =(By.XPATH,"//*[contains(@text,'电话')]")
#返回键
back_button =(By.XPATH,"//*[contains(@content-desc,'向上导航')]")
#手机返回键
#添加新联系人键
new_user_create_button=(By.ID,"com.android.contacts:id/floating_action_button")








