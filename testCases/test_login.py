import pytest
from selenium import webdriver

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()

    logger = LogGen.loggen()

    def test_homepage(self, setup):
        self.logger.info("**************Test_001_login*******")
        self.logger.info("**************Verifying Homepage title**********")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login!":
            assert True
            self.driver.close
            self.logger.info("***********HomePage Test Passed********************")

        else:
            self.driver.save_screenshots(filename="\home\arcgate\PycharmProjects\POMProjectforecommerce\ScreenShots\failtestcase.png")
            self.driver.close
            self.logger.info("***********HomePage Test Failed********************")

            assert False

    def test_login(self, setup):
        self.logger.info("************Verifying Login Test*********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.login_user()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close
            self.logger.info("***********Login Test Passed********************")

        else:
            self.driver.get_screenshot_as_file("test_login.png")
            self.driver.close
            self.logger.info("***********Login Test Failed********************")

            assert False
