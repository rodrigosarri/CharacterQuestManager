screen filterCloseQuests(char = Null):
    hbox:
        xpos 370
        ypos 305

        area(0, 0, 1342, 600)
        viewport id "questList":
            draggable True
            mousewheel True

            hbox:
                spacing 24
                box_wrap True

                if (mountQuest.getFilterCloseQuests(char.getCode)):
                    for quests in mountQuest.getFilterCloseQuests(char.getCode):
                        frame style "questFrame":
                            add "bgQuest"

                            hbox:
                                vbox:
                                    xoffset 8
                                    yoffset 8
                                    xminimum 1192

                                    text "[quests.getTitle]"  style "questTitle"
                                    text "[quests.getDesc]" style "questDesc"

                                    hbox:
                                        spacing 8

                                        if (quests.getHint):
                                            text "[quests.getHint]" style "questHint"

                                        if (quests.getProgress):
                                            text "Progress:" style "questProgress"
                                            text "[quests.getCurrentProgress]/[quests.getMaxProgress]" style "questProgress"

                                        if (quests.getPlace):
                                            text "Place:" style "questProgress"
                                            text "[quests.getPlace]" style "questProgress"

                                vbox:
                                    ypos 0.5

                                    if (quests.getStatus == "done"):
                                        add "doneIcon" xpos 0.35
                                        text "Done" style "titleIconDone"
                                    elif (quests.getStatus == "inProgress"):
                                        add "inprogressIcon" xpos 0.2
                                        text "In progress" style "titleIconInprogress"
                                    elif (quests.getStatus == "underDev"):
                                        add "underdevIcon" xpos 0.2
                                        text "Under dev." style "titleIconUnderDev"
                                    elif (quests.getStatus == "new"):
                                        add "newIcon" xpos 0.35
                                        text "New" style "titleIconNew"
                                    elif (quests.getStatus == "close"):
                                        add "closeIcon" xpos 0.35
                                        text "Close" style "titleIconClose"
                else:
                    text "This character doesn't have any quests yet" style "questTitle"
                    add "noQuests" ypos 0.5

        #vbar value YScrollValue("questList")