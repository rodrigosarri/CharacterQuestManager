screen char(type = Null):

    default charImage = type.getImage

    if (type != Null):
        frame:
            xysize(250, 802)
            pos(365, 190)
            style "defaultFrame"

            if (charImage):
                add Transform(charImage, align = (0.0, 0.5)):
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

                if not type.getHideName['hideName']:
                    text type.getName:
                        style "charTitle"
                else:
                    text type.getHideName['hiddenNameText']:
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

                                            imagebutton idle Transform(type.getAllStatsChar[stats]["icon"], align = (0.5, 0.5)):
                                            # add type.getAllStatsChar[stats]["icon"]:
                                                xalign .5
                                                action Return(1)
                                                hovered [SetScreenVariable("charImage", type.getImageByStat(stats))]
                                                unhovered [SetScreenVariable("charImage", type.getImage)]
                                                # SetVariable / SetScreenVariable

                                            text type.getAllStatsChar[stats]["info"]:
                                                style type.getAllStatsChar[stats]["style"]
