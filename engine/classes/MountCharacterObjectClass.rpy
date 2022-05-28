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
                self.setStats(charStats)

            self.isShow = isShow

        def checkStatsList(self, stat):
            stats = [
                "relationship",
                "corruption",
                "sluttiness",
                "awareness",
                "strength",
                "fitness",
                "charisma",
                "knowledge",
                "respect",
                "libido",
                "submission"
            ]

            if (stat not in stats):
                return False

            return True

        def checkStatsChar(self, stat):
            if (stat not in self.charStats):
                return False

            return True

        def setRelationship(self, num = 0):
            if ("relationship" in self.charStats):
                num = int(num)

                if (num <= self.charStats["relationship"]["max"]):
                    self.charStats["relationship"]["current"] = num
                else:
                    self.charStats["relationship"]["current"] = self.charStats["relationship"]["max"]

        def setCorruption(self, num = 0):
            if ("corruption" in self.charStats):
                num = int(num)

                if (num <= self.charStats["corruption"]["max"]):
                    self.charStats["corruption"]["current"] = num
                else:
                    self.charStats["corruption"]["current"] = self.charStats["corruption"]["max"]

        def setSluttiness(self, num = 0):
            if ("sluttiness" in self.charStats):
                num = int(num)

                if (num <= self.charStats["sluttiness"]["max"]):
                    self.charStats["sluttiness"]["current"] = num
                else:
                    self.charStats["sluttiness"]["current"] = self.charStats["sluttiness"]["max"]

        def setAwareness(self, num = 0):
            if ("awareness" in self.charStats):
                num = int(num)

                if (num <= self.charStats["awareness"]["max"]):
                    self.charStats["awareness"]["current"] = num
                else:
                    self.charStats["awareness"]["current"] = self.charStats["awareness"]["max"]

        def setStrength(self, num = 0):
            if ("strength" in self.charStats):
                num = int(num)

                if (num <= self.charStats["strength"]["max"]):
                    self.charStats["strength"]["current"] = num
                else:
                    self.charStats["strength"]["current"] = self.charStats["strength"]["max"]

        def setFitness(self, num = 0):
            if ("fitness" in self.charStats):
                num = int(num)

                if (num <= self.charStats["fitness"]["max"]):
                    self.charStats["fitness"]["current"] = num
                else:
                    self.charStats["fitness"]["current"] = self.charStats["fitness"]["max"]

        def setCharisma(self, num = 0):
            if ("charisma" in self.charStats):
                num = int(num)

                if (num <= self.charStats["fitness"]["max"]):
                    self.charStats["charisma"]["current"] = num
                else:
                    self.charStats["charisma"]["current"] = self.charStats["charisma"]["max"]

        def addRelationship(self, num = 1):
            if ("relationship" in self.charStats):
                current = self.charStats["relationship"]["current"]
                num = int(num)

                if ((current + num) <= self.charStats["relationship"]["max"]):
                    self.charStats["relationship"]["current"] += num
                else:
                    self.charStats["relationship"]["current"] = self.charStats["relationship"]["max"]

        def addCorruption(self, num = 1):
            if ("corruption" in self.charStats):
                current = self.charStats["corruption"]["current"]
                num = int(num)

                if ((current + num) <= self.charStats["corruption"]["max"]):
                    self.charStats["corruption"]["current"] += num
                else:
                    self.charStats["corruption"]["current"] = self.charStats["corruption"]["max"]

        def addSluttiness(self, num = 1):
            if ("sluttiness" in self.charStats):
                current = self.charStats["sluttiness"]["current"]
                num = int(num)

                if ((current + num) <= self.charStats["sluttiness"]["max"]):
                    self.charStats["sluttiness"]["current"] += num
                else:
                    self.charStats["sluttiness"]["current"] = self.charStats["sluttiness"]["max"]

        def addAwareness(self, num = 1):
            if ("awareness" in self.charStats):
                current = self.charStats["awareness"]["current"]
                num = int(num)

                if ((current + num) <= self.charStats["awareness"]["max"]):
                    self.charStats["awareness"]["current"] += num
                else:
                    self.charStats["awareness"]["current"] = self.charStats["awareness"]["max"]

        def addStrength(self, num = 1):
            if ("strength" in self.charStats):
                current = self.charStats["strength"]["current"]
                num = int(num)

                if ((current + num) <= self.charStats["strength"]["max"]):
                    self.charStats["strength"]["current"] += num
                else:
                    self.charStats["strength"]["current"] = self.charStats["strength"]["max"]

        def addFitness(self, num = 1):
            if ("fitness" in self.charStats):
                current = self.charStats["fitness"]["current"]
                num = int(num)

                if ((current + num) <= self.charStats["fitness"]["max"]):
                    self.charStats["fitness"]["current"] += num
                else:
                    self.charStats["fitness"]["current"] = self.charStats["fitness"]["max"]

        def addCharisma(self, num = 1):
            if ("charisma" in self.charStats):
                current = self.charStats["charisma"]["current"]
                num = int(num)

                if ((current + num) <= self.charStats["fitness"]["max"]):
                    self.charStats["charisma"]["current"] += num
                else:
                    self.charStats["charisma"]["current"] = self.charStats["charisma"]["max"]

        def subRelationship(self, num = 1):
            if ("relationship" in self.charStats):
                current = self.charStats["relationship"]["current"]
                num = int(num)

                if ((current - num) >= 0):
                    self.charStats["relationship"]["current"] -= num
                else:
                    self.charStats["relationship"]["current"] = 0

        def subCorruption(self, num = 1):
            if ("corruption" in self.charStats):
                current = self.charStats["corruption"]["current"]
                num = int(num)

                if ((current - num) >= 0):
                    self.charStats["corruption"]["current"] -= num
                else:
                    self.charStats["corruption"]["current"] = 0

        def subSluttiness(self, num = 1):
            if ("sluttiness" in self.charStats):
                current = self.charStats["sluttiness"]["current"]
                num = int(num)

                if ((current - num) >= 0):
                    self.charStats["sluttiness"]["current"] -= num
                else:
                    self.charStats["sluttiness"]["current"] = 0

        def subAwareness(self, num = 1):
            if ("awareness" in self.charStats):
                current = self.charStats["awareness"]["current"]
                num = int(num)

                if ((current - num) >= 0):
                    self.charStats["awareness"]["current"] -= num
                else:
                    self.charStats["awareness"]["current"] = 0

        def subStrength(self, num = 1):
            if ("strength" in self.charStats):
                current = self.charStats["strength"]["current"]
                num = int(num)

                if ((current - num) >= 0):
                    self.charStats["strength"]["current"] -= num
                else:
                    self.charStats["strength"]["current"] = 0

        def subFitness(self, num = 1):
            if ("fitness" in self.charStats):
                current = self.charStats["fitness"]["current"]
                num = int(num)

                if ((current - num) >= 0):
                    self.charStats["fitness"]["current"] -= num
                else:
                    self.charStats["fitness"]["current"] = 0

        def subCharisma(self, num = 1):
            if ("charisma" in self.charStats):
                current = self.charStats["charisma"]["current"]
                num = int(num)

                if ((current - num) >= 0):
                    self.charStats["charisma"]["current"] -= num
                else:
                    self.charStats["charisma"]["current"] = 0

        def setStats(self, stats):
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