screen char(type = Null):
    frame style "mainFrame":
        add "[configPanel.getBg]"

        grid 2 1:
            textbutton "[configPanel.getTitleChacters]" action charTabButtonActions style "tabButton"
            textbutton "[configPanel.getTitleQuest]" action questTabButtonActions style "tabButton"

        if type != Null:
            hbox:
                ypos 78

                vbox:
                    spacing 16
                    for charButton in mountCharacter.getAllChars:
                        if charButton.getActive:
                            if charButton.getProfilePic:
                                imagebutton idle charButton.getProfilePic action  [Show("char", type=charButton), charButtonActions] style "charButton"
                            else:
                                imagebutton idle "noPicPhoto" action  [Show("char", type=charButton), charButtonActions] style "charButton"

                hbox:
                    vbox:
                        if type.getImage:
                            add "[type.getImage]" pos((64, 64))
                        else:
                            add "noPhoto" pos((64, 64))

                    vbox:
                        text "[type.getName]" pos((96, 64)) style "charTitle"
                        text "[type.getDesc]" pos((96, 80)) style "charDesc"

                        add "bgStats" pos((96, 116))
                        hbox:
                            spacing 100
                            xpos 136
                            ypos -80

                            vbox:
                                spacing 8
                                text "Relationship" style "statsTitle"
                                add "[type.getHeart]" xalign .5
                                text "[type.getCurrentRelationship]/[type.getMaxRelationship]" xalign .5 style "statsRelationship"
                            vbox:
                                spacing 8
                                text "Corruption" style "statsTitle"
                                add "[type.getDevil]" xalign .5
                                text "[type.getCurrentCorruption]/[type.getMaxCorruption]" xalign .5 style "statsCorruption"
                            vbox:
                                spacing 8
                                text "Sluttiness" style "statsTitle"
                                add "[type.getPanties]"  xalign .5
                                text "[type.getCurrentSluttiness]/[type.getMaxSluttiness]" xalign .5 style "statsSluttiness"
                            vbox:
                                spacing 8
                                text "Awareness" style "statsTitle"
                                add "[type.getLight]"  xalign .5
                                text "[type.getCurrentAwareness]/[type.getMaxAwareness]" xalign .5 style "statsAwareness"