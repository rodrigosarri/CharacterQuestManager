init python:
    import unicodedata

    class Quests(object):
        def __init__(self):
            self.allQuests = {}
            self.charCode = ""
            self.questStatus = [
                "all",
                "new",
                "done",
                "inProgress",
                "underDev",
                "close"
            ]

            self.questsTitle = {
                "all": "All",
                "new": "New",
                "done": "Done",
                "inProgress": "In Progress",
                "underDev": "Under Dev",
                "close": "Close",
            }

        def stripAccents(self, text):
            text = unicodedata.normalize("NFD", text)
            text = text.encode("ascii", "ignore")
            text = text.decode("utf-8")
            text = text.replace(" ", "")
            text = text.lower()
            return str(text)

        def checkQuestStatus(self, status):
            currentStatus = [
                "all",
                "new",
                "done",
                "inProgress",
                "underDev",
                "close"
            ]

            return status in currentStatus

        def setStatusQuest(self, questStatus):
            self.questStatus = ["all"]

            for status in questStatus:
                if (self.checkQuestStatus(status)):
                    self.questStatus.append(status)

        def setQuestTitle(self, status, title):
            if (self.checkQuestStatus(status)):
                self.questsTitle[status] = title

        def addQuest(self, char, questTitle, questDesc, questStatus, questHint = "", questProgress = {}, questPlace = ""):
            if (char.getCode):
                self.charCode = char.getCode

            if (self.checkQuestStatus(questStatus)):

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

        def getFilterNewQuests(self, charCode):
            charCode = self.stripAccents(charCode)
            filter = []

            if (charCode in self.allQuests):
                for quest in self.allQuests[charCode]:
                    if (quest.getStatus == "new"):
                        filter.append(quest)

                return filter

            return False

        def getFilterCloseQuests(self, charCode):
            charCode = self.stripAccents(charCode)
            filter = []

            if (charCode in self.allQuests):
                for quest in self.allQuests[charCode]:
                    if (quest.getStatus == "close"):
                        filter.append(quest)

                return filter

            return False

        @property
        def getQuestStatus(self):
            return self.questStatus

        @property
        def getSpacingStatus(self):
            if (len(self.questStatus) == 5):
                return 119
            elif (len(self.questStatus) == 4):
                return 176
            elif (len(self.questStatus) == 3):
                return 300
            else:
                return 119

        def getQuestTitle(self, status):
            if (self.checkQuestStatus(status)):
                return self.questsTitle[status]

        def getQuestIcon(self, status):
            if (self.checkQuestStatus(status)):
                return defaultFolder + "images/icons/" + status + ".png"

        def getQuestStyle(self, status):
            if (self.checkQuestStatus(status)):
                return "titleIcon" + status.capitalize()