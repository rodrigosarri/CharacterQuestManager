label charactersLabel:
    # Don't touch
    # Character 'n' Quest Manager

    $ mountCharacter = Characters()

    # Here is your playground ↓

    # $ mountCharacter.setStatusTitle("relationship", "???")
    # $ mountCharacter.setStatusTitle("corruption", "???")
    # $ mountCharacter.setStatusTitle("sluttiness", "???")
    # $ mountCharacter.setStatusTitle("awareness", "???")
    # $ mountCharacter.setStatusTitle("strength", "???")
    # $ mountCharacter.setStatusTitle("fitness", "!!!")
    # $ mountCharacter.setStatusTitle("charisma", "123")
    # $ mountCharacter.setStatusTitle("charm", "°°°°")
    # $ mountCharacter.setStatusTitle("knowledge", "???")

    # $ mountCharacter.setStatusTitle("respect", "???") # not yet =)
    # $ mountCharacter.setStatusTitle("libido", "???")  # not yet =)
    # $ mountCharacter.setStatusTitle("submission", "???")  # not yet =)

    # Example of how to assemble a character
    $ mountCharacter.addChar(
        "Emma", # Name of you character
        "This is the description of your character, in this case, the description of the fictional character Emma. This description must be a maximum of 570 characters.", # Description of you character (max: 570 characters)
        defaultFolder + "images/chars/emma_pic_idle.png", # Profile picture of the character that will be on the button
        defaultFolder + "images/chars/emma.png", # Char image
        {                            # Characters stats
            "relationship": {        # Available stats: relationship, corruption, sluttiness, awareness, strength, fitness, charisma, knowledge,
                "current": 0,        # charm, respect, libido and submission
                "max": 60            #
            },                       # You need to send the stats information in object format
            "charisma": {            # If you do not submit any information, the character will not display stats
                "current": 10,       # Some characters may only have events and don't need these stats
                "max": 70            # Max stats per character is currently four
            },                       #
            "knowledge": {           # You need to send the current and maximum information about each of the stats
                "current": 20,       # If you do not submit this information, current will be zero and maximum will be one hundred
                "max": 80
            },
            "fitness": {
                "current": 30,
                "max": 80
            }
        },
        True # Character is active (default is True)
    )

    $ mountCharacter.getCharByName("Emma").setRelationship(10)  # Setting a specific value
    $ mountCharacter.getCharByName("Emma").addRelationship(30)  # Increasing the character's relationship by 30
    $ mountCharacter.getCharByName("Emma").subRelationship(5)   # Decreasing the character's relationship by 5

    $ mountCharacter.addChar(
        "James",
        "Another character description, now of the fictional character James. See that James' status is different from Emma's status.",
        defaultFolder + "images/chars/james_pic_idle.png",
        defaultFolder + "images/chars/james.png",
        {
            "strength": {
                "current": 50,
                "max": 120
            },
            "charm": {
                "current": 5,
                "max": 50
            }
        }
    )

    $ mountCharacter.getCharByName("James").setStrength(10)  # Setting a specific value
    $ mountCharacter.getCharByName("James").addStrength(30)  # Increasing the character's strength by 15
    $ mountCharacter.getCharByName("James").subStrength(5)   # Decreasing the character's strength by 5

    $ mountCharacter.addChar(
        "Isabella",
        "This character does not have a profile picture, but can have an internal picture.",
        "",
        defaultFolder + "images/chars/isabella.png",
    )

    $ mountCharacter.addChar(
        "Olivia",
        "This is a character that does not have a photo defined at the time it was assembled, so an image warns that this character is without a photo. And this character also doesn't have any defined stats.",
        defaultFolder + "images/chars/olivia_pic_idle.png",
    )

    $ mountCharacter.addChar(
        "Jenny",
        "This character has neither a profile picture nor a description picture.",
    )

    return