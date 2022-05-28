screen allChars():
    hbox:
        area(170, 177, 180, 588)

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
                            imagebutton idle charButton.getProfilePic action [Show("char", type=charButton), charButtonActions] style "charButton"
                        else:
                            imagebutton idle "noPicPhoto" action [Show("char", type=charButton), charButtonActions] style "charButton"
