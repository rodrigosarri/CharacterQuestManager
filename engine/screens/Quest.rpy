screen quest(char = Null):
    default selectedFilter = "all"

    frame:
        xpos 372
        ypos 230
        style "defaultFrame"

        hbox:
            spacing mountQuest.getSpacingStatus

            if (mountQuest.getQuestObjectByChar(char.getCode)):
                for quests in mountQuest.getQuestStatus:
                    textbutton mountQuest.getQuestTitle(quests):
                        action [Show("filterQuests", char = char, filter = quests), SetScreenVariable("selectedFilter", quests)]
                        selected selectedFilter == quests
                        style "filterTitle"

            else:
                text "This character doesn't have any quests yet" style "noQuestTitle"
                add "noQuests" ypos 0.5 xpos 0 xanchor 1.0 yanchor 0.0