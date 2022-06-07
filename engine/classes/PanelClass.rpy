init python:

    class Panel(object):

        def __init__(self,
            currentColor  = "default",
            titleChacters = "Characters",
            titleQuest = "Quest Log",
        ):
            if (self.checkColorList(currentColor)):
                self.currentColor = currentColor
            else:
                self.currentColor = "default"

            self.titleChacters = titleChacters
            self.titleQuest = titleQuest

        def checkColorList(self, color):
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

            if (color not in colors):
                return False

            return True

        def setColor(self, color):
            if (self.checkColorList(color)):
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
            return defaultFolder + "images/bg/" + self.getColor + "/bg_idle.png"

        @property
        def getTitleChacters(self):
            return self.titleChacters

        @property
        def getTitleQuest(self):
            return self.titleQuest
