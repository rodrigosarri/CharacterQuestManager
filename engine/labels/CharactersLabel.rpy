label charactersLabel:
    # Don't touch
    # Character 'n' Quest Manager

    $ mountCharacter = Characters()

    # Here is your playground ↓

    # Example of how to assemble a character
    $ mountCharacter.addChar(
        "Michelle", # Name of you character
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum", # Description of you character (max: 570 characters)
        "[defaultFolder]images/chars/michelle_pic_idle.png", # Profile picture of the character that will be on the button
        "", # Image that will be next to the character description
        {                            # Characters stats
            "knowledge": {           # Available stats: relationship, corruption, sluttiness, awareness, strength, fitness, charisma, knowledge,
                "current": 0,        # respect, libido and submission
                "max": 60            #
            },                       # You need to send the stats information in object format
            "fitness": {             # If you do not submit any information, the character will not display stats
                "current": 0,        # Some characters may only have events and don't need these stats
                "max": 50            # Max stats per character is currently four
            },                       #
            "charisma": {            # You need to send the current and maximum information about each of the stats
                "current": 0,        # If you do not submit this information, current will be zero and maximum will be one hundred
                "max": 30
            },
            "charm": {
                "current": 0,
                "max": 40
            }
        },
        True # Character is active (default is True)
    )

    $ mountCharacter.getCharByName("Michelle").setKnowledge(10)
    $ mountCharacter.getCharByName("Michelle").addKnowledge(30)  # Increasing the character's relationship
    $ mountCharacter.getCharByName("Michelle").subKnowledge(5)   # Increasing the character's relationship
    $ mountCharacter.getCharByName("Michelle").addCorruption(15) # You can also increase it using the char name as a parameter instead of the number
    $ mountCharacter.getCharByName("Michelle").addSluttiness(25) # The name can be capitalized or lowercase, it doesn't matter

    $ mountCharacter.addChar(
        "Lisa",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "[defaultFolder]images/chars/lisa_pic_idle.png",
        "",
    )

    $ mountCharacter.getCharByName("Lisa").addRelationship(15)

    $ mountCharacter.addChar(
        "Nina",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "[defaultFolder]images/chars/nina_pic_idle.png",
        "",
    )

    $ mountCharacter.addChar(
        "Jenny",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "[defaultFolder]images/chars/jenny_pic_idle.png",
        "",
    )

    $ mountCharacter.addChar(
        "Jill",
        "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making",
        "[defaultFolder]images/chars/jill_pic_idle.png",
        "",
    )