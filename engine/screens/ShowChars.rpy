screen showChars():
    frame style "mainFrame":
        add "[configPanel.getBg]" xpos 175 ypos 88

        grid 4 1:
            if (configPanel.getTabStyle == "text"):
                textbutton "[configPanel.getTitleChacters]" action charTabButtonActions style "tabButton1"
                textbutton "[configPanel.getTitleQuest]" action questTabButtonActions style "tabButton2"
                textbutton "Inventory" style "tabButton3"
                textbutton "Gallery" style "tabButton4"
            elif (configPanel.getTabStyle == "icon"):
                imagebutton idle Transform("charIcon", align = (0.5, 0.5)) action charTabButtonActions style "tabButtonIcon"
                imagebutton idle Transform("questIcon", align = (0.5, 0.5)) action questTabButtonActions style "tabButtonIcon"