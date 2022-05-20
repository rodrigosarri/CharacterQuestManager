init python:
    import unicodedata

    class Panel(object):
        colors = [
            "default",
            "anakiwa",
            "caribbean_green",
            "electric_violet",
            "guardsman_red",
            "limeade",
            "lipstick",
            "pacific_blue",
            "rio_grande",
            "science_blue",
            "tenn"
        ]

        currentColor = "default"
        titleChacters = "Characters"
        titleQuest = "Quest Log"

        def setColor(self, color):
            if (color in self.colors):
                self.currentColor = color

        def setTitleChacters(self, title):
            self.titleChacters = title

        def setTitleQuest(self, title):
            self.titleQuest = title

        @property
        def getColor(self):
            return self.currentColor

        @property
        def getBg(self):
            return "cqm/assets/images/bg/" + self.getColor + "/bg_idle.png"

        @property
        def getTitleChacters(self):
            return self.titleChacters

        @property
        def getTitleQuest(self):
            return self.titleQuest

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

    class Quests(object):
        def __init__(self, allQuests = {}, charCode = ""):
            self.allQuests = allQuests
            self.charCode = ""

        def stripAccents(self, text):
            text = unicodedata.normalize("NFD", text)
            text = text.encode("ascii", "ignore")
            text = text.decode("utf-8")
            text = text.replace(" ", "")
            text = text.lower()
            return str(text)

        def addQuest(self, char, questTitle, questDesc, questStatus, questHint = "", questProgress = {}, questPlace = ""):
            if (char.getCode):
                self.charCode = char.getCode

            currentQuestStatus = ["new", "done", "inProgress", "underDev"]

            if (questStatus in currentQuestStatus):

                if (self.charCode not in self.allQuests):
                    self.allQuests[self.charCode] = []

                self.allQuests[self.charCode].append(MountQuestObject(
                    questTitle,
                    questDesc,
                    questStatus,
                    questHint,
                    questProgress,
                    questPlace
                ))

        def getAllQuestObject(self):
            return self.allQuests

        def getQuestObjectByChar(self, charCode):
            charCode = self.stripAccents(charCode)

            if (charCode in self.allQuests):
                return self.allQuests[charCode]

            return False

        def getFilterDoneQuests(self, charCode):
            charCode = self.stripAccents(charCode)
            filter = []

            if (charCode in self.allQuests):
                for quest in self.allQuests[charCode]:
                    if (quest.getStatus == "done"):
                        filter.append(quest)

                return filter

            return False

        def getFilterInProgressQuests(self, charCode):
            charCode = self.stripAccents(charCode)
            filter = []

            if (charCode in self.allQuests):
                for quest in self.allQuests[charCode]:
                    if (quest.getStatus == "inProgress"):
                        filter.append(quest)

                return filter

            return False

        def getFilterUnderDevQuests(self, charCode):
            charCode = self.stripAccents(charCode)
            filter = []

            if (charCode in self.allQuests):
                for quest in self.allQuests[charCode]:
                    if (quest.getStatus == "underDev"):
                        filter.append(quest)

                return filter

            return False

    class MountQuestObject(object):

        def __init__(self, questTitle, questDesc, questStatus, questHint, questProgress, questPlace):
            self.questTitle = questTitle
            self.questDesc = questDesc
            self.questStatus = questStatus
            self.questHint = questHint
            self.questProgress = questProgress
            self.questPlace = questPlace

        def setTitle(self, questTitle):
            self.questTitle = questTitle

        def setDesc(self, questDesc):
            self.questDesc = questDesc

        def setHint(self, questHint):
            self.questHint = questHint

        def setProgress(self, questProgress):
            self.questProgress = questProgress

        def setPlace(self, questPlace):
            self.questPlace = questPlace

        def addProgress(self, progress = 1):
            current = self.questProgress["current"]

            if ((current + progress) <= self.questProgress["max"]):
                self.questProgress["current"] += progress
            else:
                self.questProgress["current"] = self.questProgress["max"]

        def subProgress(self, progress = 1):
            current = self.questProgress["current"]

            if ((current - progress) >= 0):
                self.questProgress["current"] -= progress
            else:
                self.questProgress["current"] = 0

        @property
        def getTitle(self):
            return self.questTitle

        @property
        def getDesc(self):
            return self.questDesc

        @property
        def getStatus(self):
            return self.questStatus

        @property
        def getHint(self):
            return self.questHint

        @property
        def getProgress(self):
            return self.questProgress

        @property
        def getCurrentProgress(self):
            return self.questProgress["current"]

        @property
        def getMaxProgress(self):
            return self.questProgress["max"]

        @property
        def getPlace(self):
            return self.questPlace