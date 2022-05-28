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