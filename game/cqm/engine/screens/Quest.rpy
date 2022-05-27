screen quest(char = Null):
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