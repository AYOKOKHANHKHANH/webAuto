from configparser import ConfigParser
import config.appConfig as appConfig


class Info:
    user_name: str = ''
    pwd: str = ''
    pin: str = ''
    name_contact: str = ''
    name_group: str = ''
    phone_contact : str = ''

    def __init__(self, user_name: str, pwd: str, pin: str, name_contact:str, name_group: str, phone_contact: str):
        self.user_name = user_name
        self.pwd = pwd
        self.pin = pin
        self.name_contact = name_contact
        self.name_group = name_group
        self.phone_contact = phone_contact


class EnvConfig:
    __instance__ = None
    INFO_LOGIN_SECTION_KEY: str = 'INFO'

    def __init__(self):
        if EnvConfig.__instance__ is None:
            try:
                config: ConfigParser = ConfigParser()
                config.read(appConfig.ENV_FILE_PATH, encoding='utf-8')

                user_name = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'UserName')
                pwd = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'Password')
                pin = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'PIN')
                name_contact = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'Name_Contact')
                name_group = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'Name_Group')
                phone_contact = config.get(EnvConfig.INFO_LOGIN_SECTION_KEY, 'Phone_Contact')

                self.info = Info(user_name=user_name, pwd=pwd, pin=pin, name_contact=name_contact, name_group=name_group, phone_contact=phone_contact)


                EnvConfig.__instance__ = self
            except Exception as ex:
                print("Load evn.ini error", ex)
        else:
            raise Exception("You cannot create another EnvConfig class")

    @staticmethod
    def getInstance():
        """ Static method to fetch the current instance.
        """
        if not EnvConfig.__instance__:
            EnvConfig()
        return EnvConfig.__instance__