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
        Hide("filterQuests"),
    ]

    $ charTabButtonActions = [
        Show("allChars"),
        Hide("allQuests"),
        Hide("char"),
        Hide("quest"),
        Hide("filterQuests"),
    ]

    $ questTabButtonActions = [
        Show("allQuests"),
        Hide("allChars"),
        Hide("char"),
        Hide("quest"),
        Hide("filterQuests"),
    ]

    $ charButtonActions = [
        Hide("allQuests"),
        Hide("quest"),
        Hide("filterQuests"),
    ]

    $ questButtonActions = [
        Hide("allChars"),
        Hide("char"),
    ]

    return