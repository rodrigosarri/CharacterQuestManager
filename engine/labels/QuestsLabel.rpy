label questsLabel:
    # Don't touch
    # Character 'n' Quest Manager

    $ mountQuest = Quests()

    # Here is your playground ↓

    # Change status quests, default: new, done, inProgress, underDev, close

    #$ mountQuest.setStatusQuest([
    #    "new",
    #    "done",
    #    "inProgress",
    #    "underDev",
    #    "close"
    #])

    # Change status quests title

    # $ mountQuest.setQuestTitle("new", "Start")
    # $ mountQuest.setQuestTitle("done", "Finish")
    # $ mountQuest.setQuestTitle("inProgress", "Progressing")
    # $ mountQuest.setQuestTitle("underDev", "Keep calm")
    # $ mountQuest.setQuestTitle("close", "Lost")

    # Example of how to build a quest

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"), # Add which character this quest is
        "This is your first quest", # Quest Title
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a", # Quest description (max: 225 characters)
        "inProgress", # Quest status
        "Tip to help complete this quest.",  # Hint or warning for this quest
        {
            "current": 48,
            "max": 120
        },
        "A Place with No Name" # Place where the mission is taking place
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"),
        "Second quest finished",
        "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout..",
        "done",
        "",
        {
            "current": 5,
            "max": 5
        },
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"),
        "Third quest",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old",
        "new",
        "",
        {},
        "At Work"
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"),
        "Quest you missed by choosing another path",
        "as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text",
        "close",
        "These things happen =("
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"),
        "title quest5",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old",
        "inProgress",
    )

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"),
        "title quest6",
        "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour",
        "underDev",
        "You have already reached maximum progress on this quest. Wait for update =)"
    )

    return