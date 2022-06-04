style exampleButton is button:
    xpos 120
    ypos 60
    xysize (240, 80)
    background "[defaultFolder]images/open_button_idle.png"
    xalign .5
    yalign .5
    hover_background "[defaultFolder]images/open_button_over.png"

style exampleButton_text is text:
    yalign .5
    xalign .5
    color "#e12345"
    outlines [ (0, "#ffffff", 1, 1, 1) ]
    size 38

style charButton is button:
    xpos 0
    ypos 0
    ymargin 32
    xysize (162, 150)
    padding [16, 10, 16, 8]
    # background "[defaultFolder]images/bg/[configPanel.getColor]/selected_char_idle.png"

style tabButton1 is button:
    xpos 175
    ypos 0
    xysize (361, 133)
    background "[defaultFolder]images/tabs/tab_button1.png"
    hover_background "[defaultFolder]images/tabs/tab_button1_hover.png"
    selected_idle_background "[defaultFolder]images/tabs/tab_button1_hover.png"
    selected_hover_background "[defaultFolder]images/tabs/tab_button1_hover.png"

style tabButton1_text is text:
    ypos 17
    xalign .5
    color "#333333"
    size 60

style tabButton2 is button:
    xpos 145
    ypos 0
    xysize (373, 104)
    background "[defaultFolder]images/tabs/tab_button2.png"
    hover_background "[defaultFolder]images/tabs/tab_button2_hover.png"
    selected_idle_background "[defaultFolder]images/tabs/tab_button2_hover.png"
    selected_hover_background "[defaultFolder]images/tabs/tab_button2_hover.png"

style tabButton2_text is text:
    ypos 17
    xalign .5
    color "#333333"
    size 60

style tabButton3 is button:
    xpos 130
    ypos 0
    xysize (373, 104)
    background "[defaultFolder]images/tabs/tab_button3.png"
    hover_background "[defaultFolder]images/tabs/tab_button3_hover.png"
    selected_idle_background "[defaultFolder]images/tabs/tab_button3_hover.png"
    selected_hover_background "[defaultFolder]images/tabs/tab_button3_hover.png"

style tabButton3_text is text:
    ypos 17
    xalign .5
    color "#333333"
    size 60

style tabButton4 is button:
    xpos 115
    ypos 0
    xysize (353, 133)
    background "[defaultFolder]images/tabs/tab_button4.png"
    hover_background "[defaultFolder]images/tabs/tab_button4_hover.png"
    selected_idle_background "[defaultFolder]images/tabs/tab_button4_hover.png"
    selected_hover_background "[defaultFolder]images/tabs/tab_button4_hover.png"

style tabButton4_text is text:
    ypos 17
    xalign .5
    color "#333333"
    size 60

style tabButtonIcon is button:
    xpos 0
    ypos 0
    xysize (226, 78)
    background "[defaultFolder]images/bg/[configPanel.getColor]/tab_icon_hover.png"
    hover_background "[defaultFolder]images/bg/[configPanel.getColor]/tab_icon_idle.png"
    selected_idle_background "[defaultFolder]images/bg/[configPanel.getColor]/tab_icon_idle.png"
    selected_hover_background "[defaultFolder]images/bg/[configPanel.getColor]/tab_icon_idle.png"

style charTitle is text:
    size 50
    color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style charDesc is text:
    size 25
    color "333333"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    line_leading 8
    xmaximum 963
    justify True

style statsTitle is text:
    size 25
    xalign 0.5
    color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsAwareness is text:
    size 25
    xalign 0.5
    color "#fffb04"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsCharisma is text:
    size 25
    xalign 0.5
    color "#fe7295"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsCharm is text:
    size 25
    xalign 0.5
    color "#3f456f"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsCorruption is text:
    size 25
    xalign 0.5
    color "#a031b6"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsFitness is text:
    size 25
    xalign 0.5
    color "#cae963"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsKnowledge is text:
    size 25
    xalign 0.5
    color "#3c7dbd"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsLibido is text:
    size 25
    xalign 0.5
    color "#fd4e0f"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsRelationship is text:
    size 25
    xalign 0.5
    color "#9b0909"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsRespect is text:
    size 25
    xalign 0.5
    color "#338372"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsSluttiness is text:
    size 25
    xalign 0.5
    color "#c30068"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsStrength is text:
    size 25
    xalign 0.5
    color "#241d34"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsSubmission is text:
    size 25
    xalign 0.5
    color "#88303c"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style filterTitle is button:
    hover_background Transform("[defaultFolder]images/arrow_down.png", align = (0.5, 1.4))
    selected_idle_background Transform("[defaultFolder]images/arrow_down.png", align = (0.5, 1.4))
    selected_hover_background Transform("[defaultFolder]images/arrow_down.png", align = (0.5, 1.4))

style filterTitle_text is text:
    size 35
    color "#333333"
    hover_color "#000000"
    selected_color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style questTitle is text:
    size 35
    color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style noQuestTitle is text:
    size 35
    color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    xanchor 0.0

style questDesc is text:
    size 20
    color "#71461b"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    line_leading 4
    xmaximum 1170
    justify True

style questHint is text:
    size 16
    color "#d40f0f"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    justify True
    yanchor -1.0

style questProgress is text:
    size 20
    color "#333333"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    yanchor -0.7

style titleIconNew is text:
    size 20
    color "#e0218a"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    xpos 0.42

style titleIconDone is text:
    size 20
    color "#75d40f"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    xpos 0.42

style titleIconInprogress is text:
    size 20
    color "#ff9c00"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style titleIconUnderDev is text:
    size 20
    color "#d40f0f"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style titleIconClose is text:
    size 20
    color "#b01919"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    xpos 0.42

style mainFrame is default:
    xysize(1580, 872)
    xalign .5
    yalign .5
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0
    modal True
    background None

style defaultFrame is default:
    xanchor 0.0
    yanchor 0.0
    xalign 0
    yalign 0
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0
    modal False
    background None


style statsFrame is default:
    xysize(963, 228)
    xalign 0
    yalign 0
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0
    modal False
    background None

style questFrame is default:
    xysize(1342, 183)
    xalign .5
    yalign .5
    xpadding 0
    ypadding 0
    xmargin 0
    ymargin 0
    modal False
    background None