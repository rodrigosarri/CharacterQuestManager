screen filterUnderDevQuests(char = Null):
    vbox:
        pos((0.19, 0.2))
        xanchor 1
        yanchor 0

        hbox:
            spacing 118

            if (mountQuest.getQuestObjectByChar(char.getCode)):
                textbutton "All" action [Show("filterAllQuests", char = char), filterAllActions] style "filterTitle"
                textbutton "New" action [Show("filterNewQuests", char = char), filterNewActions] style "filterTitle"
                textbutton "Done" action [Show("filterDoneQuests", char = char), filterDoneActions] style "filterTitle"
                textbutton "In progress" action [Show("filterInProgressQuests", char = char), filterInProgressActions] style "filterTitle"
                textbutton "Under dev." action [Show("filterUnderDevQuests", char = char), filterUnderDevActions] style "filterTitle"
                textbutton "Close" action [Show("filterCloseQuests", char = char), filterCloseActions] style "filterTitle"
            else:
                vbox:
                    text "This character doesn't have any quests yet" style "noQuestTitle"
                    add "noQuests" ypos 0.5 xpos 0 xanchor 0.0

        hbox:
            yoffset 64

            area(1, 0, 1342, 600)
            viewport id "questList":
                draggable True
                mousewheel True

                hbox:
                    spacing 24
                    box_wrap True

                    if (mountQuest.getFilterUnderDevQuests(char.getCode)):
                        for quests in mountQuest.getFilterUnderDevQuests(char.getCode):
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