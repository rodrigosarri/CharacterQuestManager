screen char(type = Null):
    if type != Null:
        hbox:
            pos((0.5, 0.2))
            xanchor 0.5
            yanchor 0

            hbox:
                vbox:
                    if type.getImage:
                        add "[type.getImage]" pos((32, 64))
                    else:
                        add "noPhoto" pos((32, 64))

                vbox:
                    text "[type.getName]" pos((96, 64)) style "charTitle"
                    text "[type.getDesc]" pos((96, 80)) style "charDesc"

                    if (type.getTotalStats > 0):
                        add "bgStats" pos((96, 116))

                    hbox:
                        spacing 100
                        xpos 136
                        ypos -80

                        if (type.getTotalStats > 0):

                            if (type.checkStatsChar("strength")):
                                vbox:
                                    spacing 8
                                    text "Strength" style "statsTitle"
                                    add "[type.getMuscle]"  xalign .5
                                    text "[type.getCurrentStrength]/[type.getMaxStrength]" style "statsStrength"

                            if (type.checkStatsChar("fitness")):
                                vbox:
                                    spacing 8
                                    text "Fitness" style "statsTitle"
                                    add "[type.getRunner]"  xalign .5
                                    text "[type.getCurrentFitness]/[type.getMaxFitness]" style "statsFitness"

                            if (type.checkStatsChar("relationship")):
                                vbox:
                                    spacing 8
                                    text "Relationship" style "statsTitle"
                                    add "[type.getHeart]" xalign .5
                                    text "[type.getCurrentRelationship]/[type.getMaxRelationship]" style "statsRelationship"

                            if (type.checkStatsChar("charisma")):
                                vbox:
                                    spacing 8
                                    text "Charisma" style "statsTitle"
                                    add "[type.getSpeaker]" xalign .5
                                    text "[type.getCurrentCharisma]/[type.getMaxCharisma]" style "statsCharisma"

                            if (type.checkStatsChar("charm")):
                                vbox:
                                    spacing 8
                                    text "Charm" style "statsTitle"
                                    add "[type.getCharming]" xalign .5
                                    text "[type.getCurrentCharm]/[type.getMaxCharm]" style "statsCharm"

                            if (type.checkStatsChar("knowledge")):
                                vbox:
                                    spacing 8
                                    text "Knowledge" style "statsTitle"
                                    add "[type.getBook]" xalign .5
                                    text "[type.getCurrentKnowledge]/[type.getMaxKnowledge]" style "statsKnowledge"

                            if (type.checkStatsChar("corruption")):
                                vbox:
                                    spacing 8
                                    text "Corruption" style "statsTitle"
                                    add "[type.getDevil]" xalign .5
                                    text "[type.getCurrentCorruption]/[type.getMaxCorruption]" style "statsCorruption"

                            if (type.checkStatsChar("sluttiness")):
                                vbox:
                                    spacing 8
                                    text "Sluttiness" style "statsTitle"
                                    add "[type.getPanties]"  xalign .5
                                    text "[type.getCurrentSluttiness]/[type.getMaxSluttiness]" style "statsSluttiness"

                            if (type.checkStatsChar("awareness")):
                                vbox:
                                    spacing 8
                                    text "Awareness" style "statsTitle"
                                    add "[type.getLight]"  xalign .5
                                    text "[type.getCurrentAwareness]/[type.getMaxAwareness]" style "statsAwareness"