screen allChars():
    frame style "mainFrame":
        add "[configPanel.getBg]"

        grid 2 1:
            textbutton "[configPanel.getTitleChacters]" action charTabButtonActions style "tabButton"
            textbutton "[configPanel.getTitleQuest]" action questTabButtonActions style "tabButton"

        hbox:
            ypos 78

            vbox:
                spacing 16
                for charButton in mountCharacter.getAllChars:
                    if charButton.getActive:
                        if charButton.getProfilePic:
                            imagebutton idle charButton.getProfilePic action [Show("char", type=charButton), charButtonActions] style "charButton"
                        else:
                            imagebutton idle "noPicPhoto" action [Show("char", type=charButton), charButtonActions] style "charButton"