# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # Don't touch
    # Character 'n' Quest Manager

    $ configPanel = Panel()
    #$ configPanel.setColor("anakiwa")
    #$ configPanel.setColor("caribbean_green")
    #$ configPanel.setColor("electric_violet")
    #$ configPanel.setColor("guardsman_red")
    #$ configPanel.setColor("limeade")
    #$ configPanel.setColor("lipstick")
    #$ configPanel.setColor("pacific_blue")
    #$ configPanel.setColor("rio_grande")
    #$ configPanel.setColor("science_blue")
    #$ configPanel.setColor("tenn")

    $ defaultFolder = "cqm/assets/"

    $ menuButtonActions = [
        ToggleScreen("showChars"),
        Hide("allChars"),
        Hide("allQuests"),
        Hide("char"),
        Hide("quest"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests")
    ]

    $ charTabButtonActions = [
        Show("allChars"),
        Hide("allQuests"),
        Hide("char"),
        Hide("quest"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests")
    ]

    $ questTabButtonActions = [
        Show("allQuests"),
        Hide("allChars"),
        Hide("char"),
        Hide("quest"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests")
    ]

    $ charButtonActions = [
        Hide("allQuests"),
        Hide("quest"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests")
    ]

    $ questButtonActions = [
        Hide("allChars"),
        Hide("char"),
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests")
    ]

    $ filterAllActions = [
        Hide("filterDoneQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("char")
    ]

    $ filterDoneActions = [
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("filterUnderDevQuests"),
        Hide("char")
    ]

    $ filterInProgressActions = [
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterUnderDevQuests"),
        Hide("char")
    ]

    $ filterUnderDevActions = [
        Hide("filterDoneQuests"),
        Hide("filterAllQuests"),
        Hide("filterInProgressQuests"),
        Hide("char")
    ]

    $ mountCharacter = Characters()
    $ mountQuest = Quests()


    # Here is your playground ↓

    # Example of how to assemble a character
    $ mountCharacter.addChar(
        "Michelle", # Name of you character
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum", # Description of you character (max: 570 characters)
        "cqm/assets/images/chars/michelle_pic_idle.png", # Profile picture of the character that will be on the button
        "cqm/assets/images/chars/michelle.png", # Image that will be next to the character description
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

    $ mountCharacter.getAllChars[0].addRelationship(30) # Increasing the character's relationship
    $ mountCharacter.getCharByName("Michelle").addCorruption(15) # You can also increase it using the char name as a parameter instead of the number
    $ mountCharacter.getCharByName("michelle").addSluttiness(25) # The name can be capitalized or lowercase, it doesn't matter

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

    $ mountQuest.getQuestObjectByChar("Michelle")[0].setTitle("New Title Quest")
    $ mountQuest.getQuestObjectByChar("Michelle")[0].addProgress()

    $ mountCharacter.addChar(
        "Lisa",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "cqm/assets/images/chars/lisa_pic_idle.png",
        "cqm/assets/images/chars/lisa.png",
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
        False
    )

    $ mountCharacter.getAllChars[1].addRelationship(15)
    $ mountCharacter.getAllChars[1].setActive()

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy
    show screen openButton

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
