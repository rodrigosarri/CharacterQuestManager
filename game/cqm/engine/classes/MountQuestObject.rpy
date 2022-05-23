init python:
    import unicodedata

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