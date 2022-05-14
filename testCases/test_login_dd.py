import time

import pytest
from selenium import webdriver

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutilis


class Test_002_DDT_login:
    baseurl = ReadConfig.getApplicationURL()
    path = "/home/arcgate/PycharmProjects/POMProjectforecommerce/TestData/Logindata.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("**********Test_002_DDT_Login*************")
        self.logger.info("************Verifying Login Test*********")
        self.driver = setup
        self.driver.get(self.baseurl)

        self.lp = Login(self.driver)
        self.rows = XLutilis.getRowCount(self.path, 'Sheet1')
        print("Number of rows i a excel", self.rows)

        list_status = []  # Empty list variable

        for r in range(2, self.rows + 1):
            self.user = XLutilis.readData(self.path, 'Sheet1', r, 1)
            self.password = XLutilis.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLutilis.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.login_user()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            # DDT crucial things to notice and work

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("***Passed")
                    self.lp.logout_user();
                    list_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("***Failed")
                    self.lp.logout_user();
                    list_status.append("fail")

            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("***failed")
                    list_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("***passed")
                    list_status.append("pass")

        if "fail" not in list_status:
            self.logger.info("******Login DDT test passed******")
            self.driver.close()
            assert True
        else:
            self.logger.info("*************8Login DDT test failed*******")
            self.driver.close()
            assert False

        self.logger.info("***********End of login DDT*********")
        self.logger.info("**********Test_DD2_Login Completed******")
