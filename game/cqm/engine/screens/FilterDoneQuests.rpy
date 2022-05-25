screen filterDoneQuests(char = Null):
    frame style "mainFrame":
        add "[configPanel.getBg]"

        grid 2 1:
            textbutton "[configPanel.getTitleChacters]" action charTabButtonActions style "tabButton"
            textbutton "[configPanel.getTitleQuest]" action questTabButtonActions style "tabButton"

        hbox:
            ypos 78

            vbox:
                spacing 16
                for charButton in mountCharacter.getAllChars:
                    if charButton.getActive:
                        if charButton.getProfilePic:
                            imagebutton idle charButton.getProfilePic action [Show("quest", char=charButton), questButtonActions] style "charButton"
                        else:
                            imagebutton idle "noPicPhoto" action [Show("quest", char=charButton), questButtonActions] style "charButton"

            vbox:
                hbox:
                    ypos 32
                    spacing 261
                    xoffset 32

                    if (mountQuest.getQuestObjectByChar(char.getCode)):
                        textbutton "All" action [Show("filterAllQuests", char = char), filterAllActions] style "filterTitle"
                        textbutton "Done" action [Show("filterDoneQuests", char = char), filterDoneActions]  style "filterTitle"
                        textbutton "In progress" action [Show("filterInProgressQuests", char = char), filterInProgressActions]  style "filterTitle"
                        textbutton "Under dev." action [Show("filterUnderDevQuests", char = char), filterUnderDevActions]  style "filterTitle"

                hbox:
                    yoffset 64
                    xoffset 32

                    area(1, 0, 1342, 600)
                    viewport id "questList":
                        draggable True
                        mousewheel True

                        hbox:
                            spacing 24
                            box_wrap True

                            if (mountQuest.getFilterDoneQuests(char.getCode)):
                                for quests in mountQuest.getFilterDoneQuests(char.getCode):
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
                                                    text "Under dev." style "titleIconInprogress"
                            else:
                                frame style "questFrame":
                                    text "This character doesn't have any quests yet" style "questTitle"
                                    add "noQuests" ypos 0.5

                        #vbar value YScrollValue("questList")