screen allQuests():
    hbox:
        area(170, 180, 176, 588)

        vpgrid:
            cols 1
            rows mountCharacter.getRows
            mousewheel True
            # scrollbars "vertical"
            # vscrollbar_yoffset 29

            vbox:
                spacing 16

                for charButton in mountCharacter.getAllChars:
                    if charButton.getActive:
                        if charButton.getProfilePic:
                            imagebutton idle charButton.getProfilePic action [Show("quest", char = charButton), questButtonActions] style "charButton"
                        else:
                            imagebutton idle "noPicPhoto" action [Show("quest", char = charButton), questButtonActions] style "charButton"