screen filterNewQuests(char = Null):
    frame:
        xysize(1344, 680)
        xpos 380
        ypos 310
        style "defaultFrame"

        area(0, 0, 1344, 680)
        viewport id "questList":
            draggable True
            mousewheel True

            hbox:
                box_wrap True

                if (mountQuest.getFilterNewQuests(char.getCode)):
                    for quests in mountQuest.getFilterNewQuests(char.getCode):
                        frame style "questFrame":
                            add "bgQuest"

                            frame:
                                xysize(145, 145)
                                xpos 0
                                ypos 5
                                style "defaultFrame"

                                add Transform(mountQuest.getQuestIcon(quests.getStatus), align = (0.5, 0.5))
                                text mountQuest.getQuestTitle(quests.getStatus) xalign 0.5 yalign 1.0 style mountQuest.getQuestStyle(quests.getStatus)

                            frame:
                                xysize(1145, 115)
                                xpos 155
                                ypos 10
                                style "defaultFrame"

                                vbox:
                                    spacing 8
                                    text quests.getTitle  style "questTitle"
                                    text quests.getDesc style "questDesc"

                            frame:
                                xysize(610, 30)
                                xpos 155
                                yanchor 1.0
                                ypos 1.0
                                style "defaultFrame"

                                if (quests.getHint):
                                    text quests.getHint style "questHint"

                            frame:
                                xysize(265, 30)
                                xpos 805
                                yanchor 1.0
                                ypos 1.0
                                style "defaultFrame"

                                if (quests.getProgress):
                                    hbox:
                                        text "Progress: " style "questProgress"
                                        add quests.getProgressBar

                            frame:
                                xysize(265, 30)
                                yanchor 1.0
                                ypos 1.0
                                xanchor 1.0
                                xpos 1.0
                                style "defaultFrame"

                                if (quests.getPlace):
                                    hbox:
                                        text "Place: " style "questPlace"
                                        text "{u}[quests.getPlace]{/u}" style "questPlace"

                else:
                    text "No quests with this status were found" style "noQuestTitle"
                    add "noQuests" ypos 0.5 xpos 0 xanchor 1.0 yanchor 0.0

        #vbar value YScrollValue("questList")