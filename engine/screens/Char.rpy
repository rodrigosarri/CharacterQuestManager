screen char(type = Null):
    if (type != Null):
        frame:
            xysize(250, 802)
            pos(365, 190)
            style "defaultFrame"

            if (type.getImage):
                add Transform(type.getImage, align = (0.0, 0.5)):
                    xpos 33
            else:
                add Transform("noPhoto", align = (0.0, 0.5)):
                    xpos 33

        frame:
            xysize(1135, 802)
            pos(615, 190)
            style "defaultFrame"

            vbox:
                ypos 140
                xpos 50
                spacing 30

                text type.getName:
                    style "charTitle"

                text type.getDesc:
                    style "charDesc"

                if (type.getTotalStats > 0):
                    frame:
                        style "statsFrame"
                        add "bgStats"

                        area(0, 0, 899, 228)
                        viewport id "statsList":
                            draggable True
                            mousewheel True
                            pos(32, 32)

                            hbox:
                                spacing 80

                                if (type.getTotalStats > 0):
                                    for stats in type.getAllStatsChar:
                                        vbox:
                                            spacing 8

                                            text mountCharacter.getStatusTitle(stats):
                                                style "statsTitle"

                                            add type.getAllStatsChar[stats]["icon"]:
                                                xalign .5

                                            text type.getAllStatsChar[stats]["info"]:
                                                style type.getAllStatsChar[stats]["style"]
