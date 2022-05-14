import configparser

config = configparser.RawConfigParser()
config.read("/home/arcgate/PycharmProjects/POMProjectforecommerce/Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getUseremail():
        user_name = config.get('common info', 'username')
        return user_name

    @staticmethod
    def getUserpassword():
        user_pass = config.get('common info', 'password')
        return user_pass
