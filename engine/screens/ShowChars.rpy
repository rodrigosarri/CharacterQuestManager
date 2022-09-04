screen showChars():

    if renpy.get_screen("showChars"):
        $ renpy.block_rollback()
    else:
        $ renpy.can_rollback()

    frame style "mainFrame":
        add configPanel.getBg xpos 175 ypos 88

        grid 2 1:
            textbutton configPanel.getTitleCharacters action charTabButtonActions style "tabButton1"
            textbutton configPanel.getTitleQuest action questTabButtonActions style "tabButton2"
            # textbutton "Inventory" style "tabButton3"
            # textbutton "Gallery" style "tabButton4"