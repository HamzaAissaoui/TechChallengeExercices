import os

class Settings:
    @classmethod
    def get_setting(cls, name, defaultValue):
        val = os.environ.get(name)
        if val is None:
            val = defaultValue
        return val

    @classmethod
    def getHost(cls):
        return cls.get_setting("Host", "localhost")

    @classmethod
    def getDatabase(cls):
        return cls.get_setting("Database", "postgres")


    @classmethod
    def getUser(cls):
        return cls.get_setting("User", "postgres")


    @classmethod
    def getPort(cls):
        return cls.get_setting("Port", "5432")

    @classmethod
    def getPassword(cls):
        return cls.get_setting("Password", "Yobi2021")
        