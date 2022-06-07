label panelLabel:
    # Don't touch
    # Character 'n' Quest Manager

    $ configPanel = Panel()

    # Here is your playground ↓

    # Change color of background

    # $ configPanel.setColor("anakiwa")
    # $ configPanel.setColor("caribbean_green")
    # $ configPanel.setColor("electric_violet")
    # $ configPanel.setColor("guardsman_red")
    # $ configPanel.setColor("limeade")
    # $ configPanel.setColor("lipstick")
    # $ configPanel.setColor("pacific_blue")
    # $ configPanel.setColor("rio_grande")
    # $ configPanel.setColor("science_blue")
    # $ configPanel.setColor("tenn")

    # Change title of tabs (Characters, Quest Log)

    # $ configPanel.setTitleCharacters("Char")
    # $ configPanel.setTitleQuest("Mission")

    # Don't touch
    # Character 'n' Quest Manager  ↓

    $ cqmAction = [
        ToggleScreen("showChars"),
        Hide("allChars"),
        Hide("allQuests"),
        Hide("char"),
        Hide("quest"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
    ]

    $ charTabButtonActions = [
        Show("allChars"),
        Hide("allQuests"),
        Hide("char"),
        Hide("quest"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
    ]

    $ questTabButtonActions = [
        Show("allQuests"),
        Hide("allChars"),
        Hide("char"),
        Hide("quest"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
    ]

    $ charButtonActions = [
        Hide("allQuests"),
        Hide("quest"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
    ]

    $ questButtonActions = [
        Hide("allChars"),
        Hide("char"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
    ]

    $ filterAllActions = [
        Hide("filterDoneQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
        Hide("char"),
    ]

    $ filterDoneActions = [
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
        Hide("char")
    ]

    $ filterInProgressActions = [
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterUnderDevQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
        Hide("char")
    ]

    $ filterUnderDevActions = [
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterCloseQuests"),
        Hide("filterNewQuests"),
        Hide("char")
    ]

    $ filterNewActions = [
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterCloseQuests"),
        Hide("char")
    ]

    $ filterCloseActions = [
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterNewQuests"),
        Hide("filterUnderDevQuests"),
        Hide("char")
    ]

    return