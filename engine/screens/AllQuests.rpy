screen allQuests():
    vpgrid:
        xpos 170
        ypos 178
        xysize(177, 616)
        cols 1
        mousewheel True
        spacing 8

        for charButton in mountCharacter.getAllChars:
            if (charButton.getActive):
                if (charButton.getProfilePic):
                    imagebutton idle charButton.getProfilePic:
                        style "charButton"
                        action [Show("quest", char = charButton), questButtonActions]
                else:
                    imagebutton idle "noPicPhoto" action [Show("quest", char = charButton), questButtonActions] style "charButton"