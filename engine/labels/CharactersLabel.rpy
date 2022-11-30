label charactersLabel:
    # Don't touch
    # Character 'n' Quest Manager

    $ mountCharacter = Characters()

    # Here is your playground ↓

    # $ mountCharacter.setStatusTitle("awareness", "Perception")
    # $ mountCharacter.setStatusTitle("charisma", "Personality")
    # $ mountCharacter.setStatusTitle("charm", "Appeal")
    # $ mountCharacter.setStatusTitle("corruption", "Crime")
    # $ mountCharacter.setStatusTitle("fitness", "Vigor")
    # $ mountCharacter.setStatusTitle("knowledge", "Mastery")
    # $ mountCharacter.setStatusTitle("libido", "Horniness")
    # $ mountCharacter.setStatusTitle("relationship", "Love")
    # $ mountCharacter.setStatusTitle("respect", "Approval")
    # $ mountCharacter.setStatusTitle("sluttiness", "Perverted")
    # $ mountCharacter.setStatusTitle("strength", "Power")
    # $ mountCharacter.setStatusTitle("submission", "Consent")

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
                "max": 90
            },
            "corruption": {
                "current": 0,
                "max": 100
            },
            "awareness": {
                "current": 10,
                "max": 50
            },
            "respect": {
                "current": 20,
                "max": 60
            },
            "libido": {
                "current": 30,
                "max": 60
            },
            "sluttiness": {
                "current": 0,
                "max": 70
            },
            "strength": {
                "current": 10,
                "max": 80
            },
            "charm": {
                "current": 20,
                "max": 90
            },
            "submission": {
                "current": 30,
                "max": 100
            },
            "fishing": {
                "current": 50,
                "max": 100
            },
            "exhibitionist": {
                "current": 40,
                "max": 50
            },
            "sharing": {
                "current": 45,
                "max": 90
            },
        },
        True # Character is active (default is True)
    )

    # You can add different images for each character's stats.


    # To add it, you must use the setImageByStat method, sending as a parameter which stat you want to change the image and which is the image linked to that stat.

    # Two remarks:
    # 1 - You need to put the full path to the image.
    # 2 - If you don't upload an image to the stat, the image displayed will be the character's original image

    # Example of how to add an image for each stat
    $ mountCharacter.getCharByName("Emma").setImageByStat("relationship", defaultFolder + "images/chars/james.png")
    $ mountCharacter.getCharByName("Emma").setImageByStat("charisma", defaultFolder + "images/chars/isabella.png")

    $ mountCharacter.getCharByName("Emma").setStats("relationship", 10)  # Setting a specific value
    $ mountCharacter.getCharByName("Emma").addStats("relationship", 30)  # Increasing the character's relationship by 30
    $ mountCharacter.getCharByName("Emma").subStats("relationship", 5)   # Decreasing the character's relationship by 5

    $ mountCharacter.addChar(
        "James",
        "Another character description, now of the fictional character James. See that James' status is different from Emma's status.",
        defaultFolder + "images/chars/james_pic_idle.png",
        defaultFolder + "images/chars/james.png",
        {
            "strength": {
                "current": 0,
                "max": 120
            },
            "charm": {
                "current": 25,
                "max": 50
            }
        }
    )

    # Hide the character's name until you know him
    $ mountCharacter.getCharByName("James").setHideName(True)

    # You can use as a second parameter the character option you want to use to hide the name
    # $ mountCharacter.getCharByName("James").setHideName(True, "-----")

    # To redisplay the name use the same method but pass the value as false
    # $ mountCharacter.getCharByName("James").setHideName(False)

    # Hide the status of one of the character's items
    $ mountCharacter.getCharByName("Emma").setHideStat("strength", True)

    # You can use as a third parameter the character option you want to use to hide the stat
    # $ mountCharacter.getCharByName("Emma").setHideStat("strength", True, "-----")

    # To redisplay the stat name use the same method but pass the value as false
    # $ mountCharacter.getCharByName("Emma").setHideStat("strength", False)

    $ mountCharacter.getCharByName("James").setStats("strength", 50)  # Setting a specific value
    $ mountCharacter.getCharByName("James").addStats("strength", 30)  # Increasing the character's strength by 30
    $ mountCharacter.getCharByName("James").subStats("strength", 5)   # Decreasing the character's strength by 5

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

    # Adding stats after character creation
    $ mountCharacter.getCharByName("Jenny").setAllStats({
        "fitness": {
            "current": 30,
            "max": 90
        },
    })

    return