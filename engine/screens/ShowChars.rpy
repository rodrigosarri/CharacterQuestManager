screen showChars():
    frame style "mainFrame":
        add configPanel.getBg xpos 175 ypos 88

        grid 4 1:
            textbutton configPanel.getTitleCharacters action charTabButtonActions style "tabButton1"
            textbutton configPanel.getTitleQuest action questTabButtonActions style "tabButton2"
            textbutton "Inventory" style "tabButton3"
            textbutton "Gallery" style "tabButton4"