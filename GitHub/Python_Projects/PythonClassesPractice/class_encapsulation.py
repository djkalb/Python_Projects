from msilib.schema import Class

class Private:
    def __init__(self, protected):
        self._protect = protected
        self.__secret = ""
    def getSecret(self):
        return self.__secret
    def setSecret(self, attr):
        self.__secret = attr
        return self.__secret
priv = Private("ummm")
print(priv._protect)
priv.setSecret("shhh")
print(priv.getSecret())