screen openButton():
    zorder 1
    textbutton "Menu" action menuButtonActions style "openButton"

image bgChar         = "[defaultFolder]images/bg.png"
image bgStats        = "[defaultFolder]images/bg_stats.png"
image bgQuest        = "[defaultFolder]images/bg_quest.png"
image noPhoto        = "[defaultFolder]images/no-photo.png"
image noPicPhoto     = "[defaultFolder]images/no-pic-photo_idle.png"
image doneIcon       = "[defaultFolder]images/icons/done.png"
image inprogressIcon = "[defaultFolder]images/icons/in_progress.png"
image underdevIcon   = "[defaultFolder]images/icons/under_dev.png"
image noQuests       = "[defaultFolder]images/no_quests.png"

screen showChars():
    frame style "mainFrame":
        add "[configPanel.getBg]"

        grid 2 1:
            textbutton "[configPanel.getTitleChacters]" action charTabButtonActions style "tabButton"
            textbutton "[configPanel.getTitleQuest]" action questTabButtonActions style "tabButton"

screen allChars():
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
                            imagebutton idle charButton.getProfilePic action [Show("char", type=charButton), charButtonActions] style "charButton"
                        else:
                            imagebutton idle "noPicPhoto" action [Show("char", type=charButton), charButtonActions] style "charButton"

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

screen allQuests():
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

screen quest(char = Null):
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
                            imagebutton idle charButton.getProfilePic action [Show("quest", char = charButton), questButtonActions] style "charButton"
                        else:
                            imagebutton idle "noPicPhoto" action [Show("quest", char = charButton), questButtonActions] style "charButton"

            vbox:
                hbox:
                    ypos 32
                    spacing 261
                    xoffset 32

                    if (mountQuest.getQuestObjectByChar(char.getCode)):
                        textbutton "All" action [Show("filterAllQuests", char = char), filterAllActions] style "filterTitle"
                        textbutton "Done" action [Show("filterDoneQuests", char = char), filterDoneActions] style "filterTitle"
                        textbutton "In progress" action [Show("filterInProgressQuests", char = char), filterInProgressActions] style "filterTitle"
                        textbutton "Under dev." action [Show("filterUnderDevQuests", char = char), filterUnderDevActions] style "filterTitle"

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

                            if (mountQuest.getQuestObjectByChar(char.getCode)):
                                for quests in mountQuest.getQuestObjectByChar(char.getCode):
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

screen filterAllQuests(char = Null):
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
                            imagebutton idle charButton.getProfilePic action [Show("quest", char = charButton), questButtonActions] style "charButton"
                        else:
                            imagebutton idle "noPicPhoto" action [Show("quest", char = charButton), questButtonActions] style "charButton"

            vbox:
                hbox:
                    ypos 32
                    spacing 261
                    xoffset 32

                    if (mountQuest.getQuestObjectByChar(char.getCode)):
                        textbutton "All" action [Show("filterAllQuests", char = char), filterAllActions] style "filterTitle"
                        textbutton "Done" action [Show("filterDoneQuests", char = char), filterDoneActions] style "filterTitle"
                        textbutton "In progress" action [Show("filterInProgressQuests", char = char), filterInProgressActions] style "filterTitle"
                        textbutton "Under dev." action [Show("filterUnderDevQuests", char = char), filterUnderDevActions] style "filterTitle"

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

                            if (mountQuest.getQuestObjectByChar(char.getCode)):
                                for quests in mountQuest.getQuestObjectByChar(char.getCode):
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

screen filterInProgressQuests(char = Null):
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

                            if (mountQuest.getFilterInProgressQuests(char.getCode)):
                                for quests in mountQuest.getFilterInProgressQuests(char.getCode):
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

screen filterUnderDevQuests(char = Null):
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
                                                    text "Under dev." style "titleIconInprogress"
                            else:
                                frame style "questFrame":
                                    text "This character doesn't have any quests yet" style "questTitle"
                                    add "noQuests" ypos 0.5

                        #vbar value YScrollValue("questList")