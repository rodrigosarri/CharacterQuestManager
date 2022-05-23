init python:

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