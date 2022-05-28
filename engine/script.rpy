label cqm:
    define defaultFolder = "CharacterQuestManager/assets/"

    # Don't touch
    # Character 'n' Quest Manager

    $ configPanel = Panel()
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

    # default images
    image bgChar         = "[defaultFolder]images/bg.png"
    image bgStats        = "[defaultFolder]images/bg_stats.png"
    image bgQuest        = "[defaultFolder]images/bg_quest.png"
    image noPhoto        = "[defaultFolder]images/no-photo.png"
    image noPicPhoto     = "[defaultFolder]images/no-pic-photo_idle.png"
    image newIcon        = "[defaultFolder]images/icons/new.png"
    image doneIcon       = "[defaultFolder]images/icons/done.png"
    image inprogressIcon = "[defaultFolder]images/icons/in_progress.png"
    image underdevIcon   = "[defaultFolder]images/icons/under_dev.png"
    image closeIcon      = "[defaultFolder]images/icons/close.png"
    image noQuests       = "[defaultFolder]images/no_quests.png"

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
        Hide("char")
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

    $ mountCharacter = Characters()
    $ mountQuest = Quests()

    # Here is your playground ↓

    # Example of how to assemble a character
    $ mountCharacter.addChar(
        "Michelle", # Name of you character
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum", # Description of you character (max: 570 characters)
        "CharacterQuestManager/assets/images/chars/michelle_pic_idle.png", # Profile picture of the character that will be on the button
        "", # Image that will be next to the character description
        {
            "relationship": {
                "current": 0,
                "max": 60
            },
            "corruption": {
                "current": 0,
                "max": 50
            },
            "sluttiness": {
                "current": 0,
                "max": 30
            },
            "awareness": {
                "current": 0,
                "max": 40
            }
        },
        True # Character is active
    )

    $ mountCharacter.getCharByName("Michelle").addRelationship(30) # Increasing the character's relationship
    $ mountCharacter.getCharByName("Michelle").addCorruption(15) # You can also increase it using the char name as a parameter instead of the number
    $ mountCharacter.getCharByName("Michelle").addSluttiness(25) # The name can be capitalized or lowercase, it doesn't matter

    # Example of how to build a quest
    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Michelle"), # Add which character this quest is
        "Raise the relationship level with your wife", # Quest Title
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a",
        "inProgress", # Quest description (max: 225 characters)
        "test hint", # Hint or warning for this quest, not required, you can send: ""
        {
            "current": 0,
            "max": 120
        },
        "At Home" # Place where the mission is taking place, no thanks, you can send: ""
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Michelle"),
        "new test quest",
        "whatever.",
        "done",
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Michelle"),
        "title quest3",
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
        "new",
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Michelle"),
        "title quest4",
        "as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text",
        "close",
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Michelle"),
        "title quest5",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old",
        "inProgress",
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Michelle"),
        "title quest6",
        "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour",
        "underDev",
    )

    $ mountCharacter.addChar(
        "Lisa",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "CharacterQuestManager/assets/images/chars/lisa_pic_idle.png",
        "",
        {
            "relationship": {
                "current": 0,
                "max": 60
            },
            "corruption": {
                "current": 0,
                "max": 50
            },
            "sluttiness": {
                "current": 0,
                "max": 30
            },
            "awareness": {
                "current": 0,
                "max": 40
            }
        },
        True
    )

    $ mountCharacter.getCharByName("Lisa").addRelationship(15)

    $ mountCharacter.addChar(
        "Nina",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "CharacterQuestManager/assets/images/chars/nina_pic_idle.png",
        "",
        {
            "relationship": {
                "current": 0,
                "max": 60
            },
            "corruption": {
                "current": 0,
                "max": 50
            },
            "sluttiness": {
                "current": 0,
                "max": 30
            },
            "awareness": {
                "current": 0,
                "max": 40
            }
        },
        True
    )

    $ mountCharacter.addChar(
        "Jenny",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "CharacterQuestManager/assets/images/chars/jenny_pic_idle.png",
        "",
        {
            "relationship": {
                "current": 0,
                "max": 60
            },
            "corruption": {
                "current": 0,
                "max": 50
            },
            "sluttiness": {
                "current": 0,
                "max": 30
            },
            "awareness": {
                "current": 0,
                "max": 40
            }
        },
        True
    )

    $ mountCharacter.addChar(
        "Jill",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "CharacterQuestManager/assets/images/chars/jill_pic_idle.png",
        "",
        {
            "relationship": {
                "current": 0,
                "max": 60
            },
            "corruption": {
                "current": 0,
                "max": 50
            },
            "sluttiness": {
                "current": 0,
                "max": 30
            },
            "awareness": {
                "current": 0,
                "max": 40
            }
        },
        True
    )

    return