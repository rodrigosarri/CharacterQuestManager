screen allChars():
    vpgrid:
        xpos 170
        ypos 178
        xysize(177, 616)
        cols 1
        mousewheel True
        spacing 8
        transpose True

        for charButton in mountCharacter.getAllChars:
            if (charButton.getActive):
                if (charButton.getProfilePic):
                    imagebutton idle charButton.getProfilePic:
                        style "charButton"
                        action [Show("char", type = charButton), charButtonActions]
                else:
                    imagebutton idle "noPicPhoto":
                        style "charButton"
                        action [Show("char", type = charButton), charButtonActions]