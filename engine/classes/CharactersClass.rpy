init python:

    class Characters(object):

        def __init__(self):
            self.chars = []
            self.charStatusTitle = {
                "relationship": "Relationship",
                "corruption": "Corruption",
                "sluttiness": "Sluttiness",
                "awareness": "Awareness",
                "strength": "Strength",
                "fitness": "Fitness",
                "charisma": "Charisma",
                "charm": "Charm",
                "knowledge": "Knowledge",
                "respect": "Respect",
                "libido": "Libido",
                "submission": "Submission"
            }

        def addChar(self, charName, charDesc, charProfilePic, charImage, charStats = {}, isShow = True):
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

        def checkStats(self, stat):
            stats = [
                "relationship",
                "corruption",
                "sluttiness",
                "awareness",
                "strength",
                "fitness",
                "charisma",
                "charm",
                "knowledge",
                "respect",
                "libido",
                "submission"
            ]

            if (stat not in stats):
                return False

            return True

        def setStatusTitle(self, status, title):
            if (self.checkStats(status)):
                self.charStatusTitle[status] = title

        @property
        def getAllChars(self):
            return self.chars

        def getCharByName(self, name):
            for char in self.chars:
                if (char.getName == name or char.getCode == name):
                    return char

        @property
        def getRows(self):
            return len(self.chars) * 0.206

        def getStatusTitle(self, status):
            if (self.checkStats(status)):
                return self.charStatusTitle[status]