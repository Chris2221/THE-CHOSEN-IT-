
# The script of the game goes in this file.
#DEFINED IMAGES
image bg inter = "images/SCENE/intersec.jpg"
image bg strt  = "images/SCENE/noon02.jpg"
image bg kubeta = "images/SCENE/kubeta.jpg"
image bg mansfronteve = "images/Mansion/mansion_front2_evening.png"
image bg mansdoorfrontdark = "images/Mansion/mansion_front3_nightlb.png"
image bg busstop = "images/modernBG/busstop/bus stop noon.jpg"
image bg mansnight1 = "images/Mansion/interior_entrance_nightl.png"
image bg black = "images/SCENE/blackscene.png"
image bg bedroom01_day2 = "images/Mansion/bedroom01_day2.png"
image bg mkitchen_day = "images/Mansion/mkitchen_day.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
define p = Character("[playername]", color="#121df2ff")
define r = Character("Rob", color="#f2503e")
define isip = Character("{size=-10}{i}Thoughts{i}{/size}",color="#ffff")
define narr = Character("{size=-9}{i}Narrator{i}{/size}",color="#ffff")

#define effects
define flash = Fade(.25, 0, .75, color="#000000")
# The game starts here.

label start:

    "{size=50}{i}THE CHOSEN IT STUDENT XD{i}{/size}"
    "{size=50}{i}ENJOY <3{i}{/size}" 

    $playername = renpy.input("What is your name?",default ="")
    $playername == playername.strip()
    if playername == "":
        jump start
    else:
        play music "audio/ambience/busycity.mp3" fadeout 1
        show bg busstop

        isip "{i}Hmmmm.. Sana marami akong oppurtunity dito{i}"

        narr "While walking in the street's"
        with hpunch
        hide bg busstop
        with flash 
        show bg inter
        narr "You saw your long time friend"
        p"!!!" 

        show taishirooutinghappy:
            xalign 0.30
            yalign 1.0
            zoom 0.75
            # These display lines of dialogue.

        r "Oy Pre Kamusta."
        menu:

            "What's up dog?.":
                jump choice1_yes

            "Oy Pre long time no see.":
                jump choice1_no

        label choice1_yes:

        $ menu_flag = True

        r "Anong What's dog ka dyan?."
        p "What's up dog yun pre"
        r "what what watten kita eh"
        p "Biro lang pre"
        "{size=-10}{i}*Laugh*{i}{/size}"
        r "So dito kana pala mag papatuloy ng 4th year mo pre?"

        menu:
            "Oo pre dito nako.":
                jump oo_pre

            "Dipako sure eh.":
                jump notsure

        label oo_pre:
        $ menu_flag = True
        p "San ka nga nag aaral ulit?"
        r "Dyan lang"
        p "Dito ba sa UST?"
        r "Oo pre"
        p "San nga Pre"
        r "QCU Pre"
        p "Ah.. Pwede mo ba tulungan makapag transfer dyan?"
        r "Syempre Naman"
        p "Salamat Pre"
        jump choice1_done

        label notsure:
            $ menu_flag = False
            r "Bakit naman"
            p "Baka kasi mag trabaho nalang ako pre"
            r "Ah.."
            p "Pero kung mag transfer ako dyan pwede mo ba tulungan?"
            r "Syempre Naman"
            p "Salamat Pre"
            jump choice1_done
        label choice1_no:

        $ menu_flag = False
        show taishirooutinghappy:
            xalign 0.30
            yalign 1.0
            zoom 0.75
        r "Long time no see din pre kamusta ka?"
        p "Kamusta naman pre"
        r "Ok pa naman"

        jump oo_pre

        jump choice1_done

        label choice1_done:
        

        p "Sige pre una na ako."        


        r "Sige sige"
        hide taishirooutinghappy
        stop music
        with pushleft
        
        narr "You and your friend parted ways"

        with flash
        hide bg inter
        with pushright

        show bg kubeta:
            zoom 0.50
            

        narr "While you walking"
        

        # This ends the game.

        return
