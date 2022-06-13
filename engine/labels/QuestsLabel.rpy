label questsLabel:
    # Don't touch
    # Character 'n' Quest Manager

    $ mountQuest = Quests()

    # Here is your playground ↓

    # Change status quests, default: new, done, inProgress, underDev, close

    # $ mountQuest.setStatusQuest([
    #    "new",
    #    "done",
    #    "inProgress",
    #    "underDev",
    #    "close",
    # ])

    # Change status quests title

    # $ mountQuest.setQuestTitle("all", "Every")
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
            "current": 0, # Initial quest progress
            "max": 120     # Total points for completing progress
        },
        "A Place with No Name" # Place where the quest is taking place
    )

    $ mountQuest.getQuestObjectByChar("Emma")[0].addProgress(72) # Increasing the character's progress by 72 in the first quest [0]
    $ mountQuest.getQuestObjectByChar("Emma")[0].subProgress(24) # Decreasing the character's progress by 24 in the first quest [0]

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"),
        "Second quest finished",
        "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout..",
        "done",
        "",
        {
            "current": 4,
            "max": 5
        },
    )

    $ mountQuest.getQuestObjectByChar("Emma")[1].addProgress() # Increasing the character's progress by 1 in the second quest [1]

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"),
        "Third quest",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old",
        "new",
        "",
        {},
        "At Work"
    )

    $ mountQuest.getQuestObjectByChar("Emma")[2].setProgress({ # Adding progress to a quest that started without in the third quest [2]
        "current": 1, # If the current value is not informed, the current will be zero
        "max": 10     # If the maximum value is not informed, the maximum value is 100
    })

    $ mountQuest.addQuest(
        mountCharacter.getCharByName("Emma"),
        "Quest you missed by choosing another path",
        "as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text",
        "close",
    )

    $ mountQuest.getQuestObjectByChar("Emma")[3].setHint("These things happen =(")

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