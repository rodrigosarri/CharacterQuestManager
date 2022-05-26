style openButton is button:
    xpos 120
    ypos 60
    xysize (240, 80)
    background "[defaultFolder]images/open_button_idle.png"
    xalign .5
    yalign .5
    hover_background "[defaultFolder]images/open_button_over.png"

style openButton_text is text:
    yalign .5
    xalign .5
    color "#e12345"
    outlines [ (0, "#ffffff", 1, 1, 1) ]
    size 38

style charButton is button:
    xpos 0
    ypos 0
    ymargin 32
    xysize (176, 150)
    padding [16, 10, 16, 8]
    hover_background "[defaultFolder]images/bg/[configPanel.getColor]/selected_char_idle.png"
    selected_idle_background "[defaultFolder]images/bg/[configPanel.getColor]/selected_char_idle.png"
    selected_hover_background "[defaultFolder]images/bg/[configPanel.getColor]/selected_char_idle.png"

style tabButton is button:
    xpos 0
    ypos 0
    xysize (404, 78)
    background "[defaultFolder]images/bg/[configPanel.getColor]/tab_hover.png"
    hover_background "[defaultFolder]images/bg/[configPanel.getColor]/tab_idle.png"
    selected_idle_background "[defaultFolder]images/bg/[configPanel.getColor]/tab_idle.png"
    selected_hover_background "[defaultFolder]images/bg/[configPanel.getColor]/tab_idle.png"

style tabButton_text is text:
    yalign .5
    xalign .5
    color "#333333"
    size 64

style charTitle is text:
    size 50
    color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style charDesc is text:
    size 25
    color "333333"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    line_leading 8
    xmaximum 971
    justify True

style statsTitle is text:
    size 25
    color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsRelationship is text:
    size 25
    color "#72ff00"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsCorruption is text:
    size 25
    color "#ff0000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsSluttiness is text:
    size 25
    color "#005aff"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style statsAwareness is text:
    size 25
    color "#fff600"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style filterTitle is button:
    hover_background Transform("[defaultFolder]images/arrow_down.png", align=(0.5, 1.4))
    selected_idle_background Transform("[defaultFolder]images/arrow_down.png", align=(0.5, 1.4))
    selected_hover_background Transform("[defaultFolder]images/arrow_down.png", align=(0.5, 1.4))

style filterTitle_text is text:
    size 35
    color "#525252"
    hover_color "#000000"
    selected_color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style questTitle is text:
    size 35
    color "#000000"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

style questDesc is text:
    size 20
    color "#797979"
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

style titleIconDone is text:
    size 20
    color "#75d40f"
    font defaultFolder + "/fonts/ARLRDBD.ttf"
    xpos 0.42

style titleIconInprogress is text:
    size 20
    color "#d40f0f"
    font defaultFolder + "/fonts/ARLRDBD.ttf"

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