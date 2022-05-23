init python:

    class Characters(object):

        def __init__(self, chars = []):
            self.chars = chars

        def addChar(self, charName, charDesc, charProfilePic, charImage, charStats, isShow):
            self.charName = charName
            self.charDesc = charDesc
            self.charProfilePic = charProfilePic
            self.charImage = charImage
            self.charStats = charStats
            self.isShow = isShow

            self.saveChar()

        def saveChar(self):
            self.chars.append(MountCharacterObject(
                self.charName,
                self.charDesc,
                self.charProfilePic,
                self.charImage,
                self.charStats,
                self.isShow
            ))

        @property
        def getAllChars(self):
            return self.chars

        def getCharByName(self, name):
            for char in self.chars:
                if (char.getName == name or char.getCode == name):
                    return char