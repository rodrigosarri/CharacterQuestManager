screen quest(char = Null):
    frame:
        xpos 372
        ypos 230
        style "defaultFrame"

        hbox:
            spacing mountQuest.getSpacingStatus

            if (mountQuest.getQuestObjectByChar(char.getCode)):
                textbutton "All" action [Show("filterAllQuests", char = char), filterAllActions] style "filterTitle"

                if ("new" in mountQuest.getQuestStatus):
                    textbutton mountQuest.getQuestTitle("new") action [Show("filterNewQuests", char = char), filterNewActions] style "filterTitle"

                if ("done" in mountQuest.getQuestStatus):
                    textbutton mountQuest.getQuestTitle("done") action [Show("filterDoneQuests", char = char), filterDoneActions] style "filterTitle"

                if ("inProgress" in mountQuest.getQuestStatus):
                    textbutton mountQuest.getQuestTitle("inProgress") action [Show("filterInProgressQuests", char = char), filterInProgressActions] style "filterTitle"

                if ("underDev" in mountQuest.getQuestStatus):
                    textbutton mountQuest.getQuestTitle("underDev") action [Show("filterUnderDevQuests", char = char), filterUnderDevActions] style "filterTitle"

                if ("close" in mountQuest.getQuestStatus):
                    textbutton mountQuest.getQuestTitle("close") action [Show("filterCloseQuests", char = char), filterCloseActions] style "filterTitle"
            else:
                text "This character doesn't have any quests yet" style "noQuestTitle"
                add "noQuests" ypos 0.5 xpos 0 xanchor 1.0 yanchor 0.0