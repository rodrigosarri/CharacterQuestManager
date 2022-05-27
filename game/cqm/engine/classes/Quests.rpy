init python:
    import unicodedata

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

            currentQuestStatus = ["new", "done", "inProgress", "underDev", "close"]

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