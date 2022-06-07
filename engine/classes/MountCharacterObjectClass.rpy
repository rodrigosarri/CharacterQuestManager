init python:
    import unicodedata

    class MountCharacterObject(object):

        def __init__(self, charName, charDesc, charProfilePic, charImage, charStats, isShow):
            self.charName = charName
            self.charDesc = charDesc
            self.charProfilePic = charProfilePic
            self.charImage = charImage
            self.charStats = charStats

            if (not charStats):
                self.setAllStats(charStats)

            self.isShow = isShow

            self.configStats = {
                "relationship": {
                    "style": "statsRelationship"
                },
                "corruption": {
                    "style": "statsCorruption"
                },
                "sluttiness": {
                    "style": "statsSluttiness"
                },
                "awareness": {
                    "style": "statsAwareness"
                },
                "strength": {
                    "style": "statsStrength"
                },
                "fitness": {
                    "style": "statsFitness"
                },
                "charisma": {
                    "style": "statsCharisma"
                },
                "charm": {
                    "style": "statsCharm"
                },
                "knowledge": {
                    "style": "statsKnowledge"
                },
                "respect": {
                    "style": "statsRespect"
                },
                "libido": {
                    "style": "statsLibido"
                },
                "submission": {
                    "style": "statsSubmission"
                },
            }

        def checkStatsList(self, stat):
            if (stat not in self.configStats):
                return False

            return True

        def checkStatsChar(self, stat):
            if (stat not in self.charStats):
                return False

            return True

        def setImage(self, charImage):
            self.charImage = charImage

        def setStats(self, stats, num = 0):
            if (stats in self.charStats):
                num = int(num)

                if (num <= self.charStats[stats]["max"]):
                    self.charStats[stats]["current"] = num
                else:
                    self.charStats[stats]["current"] = self.charStats[stats]["max"]

        def addStats(self, stats, num = 1):
            if (stats in self.charStats):
                current = self.charStats[stats]["current"]
                num = int(num)

                if ((current + num) <= self.charStats[stats]["max"]):
                    self.charStats[stats]["current"] += num
                else:
                    self.charStats[stats]["current"] = self.charStats[stats]["max"]


        def subStats(self, stats, num = 1):
            if (stats in self.charStats):
                current = self.charStats[stats]["current"]
                num = int(num)

                if ((current - num) >= 0):
                    self.charStats[stats]["current"] -= num
                else:
                    self.charStats[stats]["current"] = 0


        def setAllStats(self, stats):
            for stat in stats:
                if (self.checkStatsList(stat)):
                    self.charStats[stat] = {
                        "current": 0,
                        "max": 100
                    }

                    if ("current" in stats[stat]):
                        self.charStats[stat]["current"] = stats[stat]["current"]

                    if ("max" in stats[stat]):
                        self.charStats[stat]["max"] = stats[stat]["max"]

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
        def getTotalStats(self):
            return len(self.charStats)

        @property
        def getCurrentByStats(self, stats):
            return self.charStats[stats]["current"]

        @property
        def getMaxByStats(self, stats):
            return self.charStats[stats]["max"]

        def getTotalByStats(self, stat):
            current = float(self.charStats[stat]["current"])
            max = float(self.charStats[stat]["max"])
            total = int(round(current/max * 100))
            return total

        def getIconByStats(self, stat):
            total = self.getTotalByStats(stat)

            return defaultFolder + "images/character_stats/" + stat + "/" + str(total) + ".png"

        def getInfoByStats(self, stat):
            return str(self.charStats[stat]["current"]) + "/" + str(self.charStats[stat]["max"])

        @property
        def getAllStatsChar(self):
            statsChar = {}

            for stats in self.charStats:
                if (stats in self.configStats):
                    statsChar[stats] = self.configStats[stats]
                    statsChar[stats]["icon"] = self.getIconByStats(stats)
                    statsChar[stats]["info"] = self.getInfoByStats(stats)

            return statsChar