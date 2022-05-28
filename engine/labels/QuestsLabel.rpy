label questsLabel:
    # Don't touch
    # Character 'n' Quest Manager

    $ mountQuest = Quests()

    # Here is your playground ↓

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