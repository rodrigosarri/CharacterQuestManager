screen allQuests():
    frame:
        xysize(177, 616)
        xpos 180
        ypos 230
        style "defaultFrame"

        area(0, 0, 177, 616)
        vpgrid:
            xysize(177, 616)
            cols 1
            mousewheel True

            for charButton in mountCharacter.getAllChars:
                if (charButton.getActive):
                    if (charButton.getProfilePic):
                        imagebutton idle Transform(charButton.getProfilePic, align = (0.5, 0.5)):
                            style "charButton"
                            action [Show("quest", char = charButton), questButtonActions]
                    else:
                        imagebutton idle Transform("noPicPhoto", align = (0.5, 0.5)):
                            style "charButton"
                            action [Show("quest", char = charButton), questButtonActions]