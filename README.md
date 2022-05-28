# Character 'n' Quest Manager!

Hello, I'm Rodrigo Sarri, author of this project. This project aims to provide a tool for those who are developing their visual novel game.

The tool allows you to manage characters and quests using classes and methods capable of allowing greater ease in management in addition to presenting a friendly screen for your players.

# How to use?

Copy the `CharacterQuestManager` folder to your project and follow some examples and instructions left in the file: `CharacterQuestManager/engine/script.rpy`

In your main `script.rpy` file add the line `call cqm`.

Add a button and in your button action add the variable: `cqmAction` see an example:
`textbutton "Menu" action cqmAction style "openButton"`

I made a simple button if you want to use it for testing and example.
To see how it works, just add this line to your main `script.rpy` `show screen exampleButton`

![Character screen example](https://github.com/rodrigosarri/CharacterQuestManager/blob/master/assets/images/example_characters.png)

![Quest Log screen example](https://github.com/rodrigosarri/CharacterQuestManager/blob/master/assets/images/example_questlog.png)

## version 1.0.0-alpha.0

Keep in mind that this is an alpha release, so it's not a production release yet, I'm making this release available for you to use, test and report any issues or suggestions when using it in your game.

But I don't just do this project, so if I don't respond quickly to your suggestion or bug report, please be patient.

## Use license

You can use it in your free or paid game at no cost. If you want to add to your game credits that you used this feature, I'd be grateful, but it's not mandatory.