init python:
    import unicodedata

    class MountCharacterObject(object):

        def __init__(self, charName, charDesc, charProfilePic, charImage, charStats, isShow):
            self.charName = charName
            self.charDesc = charDesc
            self.charProfilePic = charProfilePic
            self.charImage = charImage
            self.charStats = charStats
            self.isShow = isShow

        def addRelationship(self, num = 1):
            current = self.charStats["relationship"]["current"]
            num = int(num)

            if ((current + num) <= self.charStats["relationship"]["max"]):
                self.charStats["relationship"]["current"] += num
            else:
                self.charStats["relationship"]["current"] = self.charStats["relationship"]["max"]

        def addCorruption(self, num = 1):
            current = self.charStats["corruption"]["current"]
            num = int(num)

            if ((current + num) <= self.charStats["corruption"]["max"]):
                self.charStats["corruption"]["current"] += num
            else:
                self.charStats["corruption"]["current"] = self.charStats["corruption"]["max"]

        def addSluttiness(self, num = 1):
            current = self.charStats["sluttiness"]["current"]
            num = int(num)

            if ((current + num) <= self.charStats["sluttiness"]["max"]):
                self.charStats["sluttiness"]["current"] += num
            else:
                self.charStats["sluttiness"]["current"] = self.charStats["sluttiness"]["max"]

        def addAwareness(self, num = 1):
            current = self.charStats["awareness"]["current"]
            num = int(num)

            if ((current + num) <= self.charStats["awareness"]["max"]):
                self.charStats["awareness"]["current"] += num
            else:
                self.charStats["awareness"]["current"] = self.charStats["awareness"]["max"]

        def subRelationship(self, num = 1):
            current = self.charStats["relationship"]["current"]
            num = int(num)

            if ((current - num) >= 0):
                self.charStats["relationship"]["current"] -= num
            else:
                self.charStats["relationship"]["current"] = 0

        def subCorruption(self, num = 1):
            current = self.charStats["corruption"]["current"]
            num = int(num)

            if ((current - num) >= 0):
                self.charStats["corruption"]["current"] -= num
            else:
                self.charStats["corruption"]["current"] = 0

        def subSluttiness(self, num = 1):
            current = self.charStats["sluttiness"]["current"]
            num = int(num)

            if ((current - num) >= 0):
                self.charStats["sluttiness"]["current"] -= num
            else:
                self.charStats["sluttiness"]["current"] = 0

        def subAwareness(self, num = 1):
            current = self.charStats["awareness"]["current"]
            num = int(num)

            if ((current - num) >= 0):
                self.charStats["awareness"]["current"] -= num
            else:
                self.charStats["awareness"]["current"] = 0

        def setStats(self, stats):
            if (stats["relationship"]):
                self.charStats["relationship"]["current"] = stats["relationship"]

            if (stats["corruption"]):
                self.charStats["corruption"]["current"] = stats["corruption"]

            if (stats["sluttiness"]):
                self.charStats["sluttiness"]["current"] = stats["sluttiness"]

            if (stats["awareness"]):
                self.charStats["awareness"]["current"] = stats["awareness"]

        def setActive(self):
            self.isShow = True

        def stripAccents(self, text):
            text = unicodedata.normalize("NFD", text)
            text = text.encode("ascii", "ignore")
            text = text.decode("utf-8")
            text = text.replace(" ", "")
            text = text.lower()
            return str(text)

        @property
        def getCode(self):
            return self.stripAccents(self.charName)

        @property
        def getName(self):
            return self.charName

        @property
        def getDesc(self):
            return self.charDesc

        @property
        def getProfilePic(self):
            return self.charProfilePic

        @property
        def getImage(self):
            return self.charImage

        @property
        def getActive(self):
            return self.isShow

        @property
        def getCurrentRelationship(self):
            return self.charStats["relationship"]["current"]

        @property
        def getCurrentCorruption(self):
            return self.charStats["corruption"]["current"]

        @property
        def getCurrentSluttiness(self):
            return self.charStats["sluttiness"]["current"]

        @property
        def getCurrentAwareness(self):
            return self.charStats["awareness"]["current"]

        @property
        def getMaxRelationship(self):
            return self.charStats["relationship"]["max"]

        @property
        def getMaxCorruption(self):
            return self.charStats["corruption"]["max"]

        @property
        def getMaxSluttiness(self):
            return self.charStats["sluttiness"]["max"]

        @property
        def getMaxAwareness(self):
            return self.charStats["awareness"]["max"]

        @property
        def getTotalRelationship(self):
            current = float(self.charStats["relationship"]["current"])
            max = float(self.charStats["relationship"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getHeart(self):
            total = self.getTotalRelationship

            return "cqm/assets/images/heart/black_heart" + str(total) + ".png"

        @property
        def getTotalCorruption(self):
            current = float(self.charStats["corruption"]["current"])
            max = float(self.charStats["corruption"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getDevil(self):
            total = self.getTotalCorruption

            return "cqm/assets/images/devil/black_devil" + str(total) + ".png"

        @property
        def getTotalSluttiness(self):
            current = float(self.charStats["sluttiness"]["current"])
            max = float(self.charStats["sluttiness"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getPanties(self):
            total = self.getTotalSluttiness

            return "cqm/assets/images/panties/black_panties" + str(total) + ".png"

        @property
        def getTotalAwareness(self):
            current = float(self.charStats["awareness"]["current"])
            max = float(self.charStats["awareness"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getLight(self):
            total = self.getTotalAwareness

            return "cqm/assets/images/light/black_light" + str(total) + ".png"