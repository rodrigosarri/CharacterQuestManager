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
        def getCurrentStrength(self):
            return self.charStats["strength"]["current"]

        @property
        def getCurrentFitness(self):
            return self.charStats["fitness"]["current"]

        @property
        def getCurrentCharisma(self):
            return self.charStats["charisma"]["current"]

        @property
        def getCurrentCharm(self):
            return self.charStats["charm"]["current"]

        @property
        def getCurrentKnowledge(self):
            return self.charStats["knowledge"]["current"]

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
        def getMaxStrength(self):
            return self.charStats["strength"]["max"]

        @property
        def getMaxFitness(self):
            return self.charStats["fitness"]["max"]

        @property
        def getMaxCharisma(self):
            return self.charStats["charisma"]["max"]

        @property
        def getMaxCharm(self):
            return self.charStats["charm"]["max"]

        @property
        def getMaxKnowledge(self):
            return self.charStats["knowledge"]["max"]

        @property
        def getTotalRelationship(self):
            current = float(self.charStats["relationship"]["current"])
            max = float(self.charStats["relationship"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getHeart(self):
            total = self.getTotalRelationship

            return defaultFolder + "images/heart/black_heart" + str(total) + ".png"

        @property
        def getTotalCorruption(self):
            current = float(self.charStats["corruption"]["current"])
            max = float(self.charStats["corruption"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getDevil(self):
            total = self.getTotalCorruption

            return defaultFolder + "images/devil/black_devil" + str(total) + ".png"

        @property
        def getTotalSluttiness(self):
            current = float(self.charStats["sluttiness"]["current"])
            max = float(self.charStats["sluttiness"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getPanties(self):
            total = self.getTotalSluttiness

            return defaultFolder + "images/panties/black_panties" + str(total) + ".png"

        @property
        def getTotalAwareness(self):
            current = float(self.charStats["awareness"]["current"])
            max = float(self.charStats["awareness"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getLight(self):
            total = self.getTotalAwareness

            return defaultFolder + "images/light/black_light" + str(total) + ".png"

        @property
        def getTotalStrength(self):
            current = float(self.charStats["strength"]["current"])
            max = float(self.charStats["strength"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getMuscle(self):
            total = self.getTotalStrength

            return defaultFolder + "images/muscle/muscle" + str(total) + ".png"

        @property
        def getTotalFitness(self):
            current = float(self.charStats["fitness"]["current"])
            max = float(self.charStats["fitness"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getRunner(self):
            total = self.getTotalFitness

            return defaultFolder + "images/fitness/fitness" + str(total) + ".png"

        @property
        def getTotalCharisma(self):
            current = float(self.charStats["charisma"]["current"])
            max = float(self.charStats["charisma"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getSpeaker(self):
            total = self.getTotalCharisma

            return defaultFolder + "images/speaker/speaker" + str(total) + ".png"

        @property
        def getTotalCharm(self):
            current = float(self.charStats["charm"]["current"])
            max = float(self.charStats["charm"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getCharming(self):
            total = self.getTotalCharm

            return defaultFolder + "images/charm/charm" + str(total) + ".png"

        @property
        def getTotalKnowledge(self):
            current = float(self.charStats["knowledge"]["current"])
            max = float(self.charStats["knowledge"]["max"])
            total = int(round(current/max * 100))
            return total

        @property
        def getBook(self):
            total = self.getTotalKnowledge

            return defaultFolder + "images/book/book" + str(total) + ".png"

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