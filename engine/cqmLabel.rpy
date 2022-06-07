label cqm:
    define defaultFolder = "CharacterQuestManager/assets/"

    # Don't touch
    # Character 'n' Quest Manager

    # default images
    image bgChar         = "[defaultFolder]images/bg.png"
    image bgStats        = "[defaultFolder]images/bg_stats.png"
    image bgQuest        = "[defaultFolder]images/bg_quest.png"
    image noPhoto        = "[defaultFolder]images/no_photo.png"
    image noPicPhoto     = "[defaultFolder]images/no_pic_photo_idle.png"
    image noQuests       = "[defaultFolder]images/no_quests.png"

    # default icons
    image charIcon       = "[defaultFolder]images/icons/characters_icon.png"
    image questIcon      = "[defaultFolder]images/icons/quests_icon.png"

    # Calling Panel label
    call panelLabel

    # Calling Characters label
    call charactersLabel

    # Calling Quests label
    call questsLabel

    return