# Email
# Password
# //button[@class='button-1 login-button']
# //a[@href='/logout']

class Login:
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@class='button-1 login-button']"
    link_logout_xpath = "//a[@href='/logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def login_user(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def logout_user(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()
