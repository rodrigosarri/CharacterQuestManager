screen showChars():
    frame style "mainFrame":
        add "[configPanel.getBg]"

        grid 2 1:
            if (configPanel.getTabStyle == "text"):
                textbutton "[configPanel.getTitleChacters]" action charTabButtonActions style "tabButton"
                textbutton "[configPanel.getTitleQuest]" action questTabButtonActions style "tabButton"
            elif (configPanel.getTabStyle == "icon"):
                imagebutton idle Transform("charIcon", align = (0.5, 0.5)) action charTabButtonActions style "tabButtonIcon"
                imagebutton idle Transform("questIcon", align = (0.5, 0.5)) action questTabButtonActions style "tabButtonIcon"