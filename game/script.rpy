define reika = Character("Reika Aoyama", color="#8B0000") # Main Character 
define hibiki = Character("Hibiki Arakawa", color="#4B0082") # Mastermind (The creator of the game)
define renji = Character("Renji Takahashi", color="#228B22") # Computer Science Major
define shoma = Character("Shoma Kanzaki", color="#8B4513") # The politics Major
define misaki = Character("Misaki Fujimura", color="#DC143C") # The English Major
define yui = Character("Yui Matsumoto", color="#FF8C00") # The Chemistry Major
define tatsuya = Character("Tatsuya Sakamoto", color="#4682B4") # The Gym Enthusiast

define sfx_notification = "notification.wav" # Sample sfx

default has_mystery_unfolded = False

label start:
    "The first day of university should have been normal. Instead, seven students wake up inside an unfamiliar campus—one that none of them remember entering."
    
    reika "This... isn’t where we were supposed to be. Something’s off."
    
    hibiki "Interesting. If this is a {color=#FFFF00}game{/color}, someone set it on purpose."
    
    renji "Locked doors. No internet. We’re stuck. This isn’t just a campus—it’s a controlled place."
    
    shoma "If this is some {color=#FFFF00}game{/color}, who’s running it? What do they want from us?"
    
    misaki "A twisted story unfolding around us. But every story has clues. We just need to look closer."
    
    tatsuya "Let’s not waste time. If we’re trapped, we’ll find a way out."
    
    yui "Or... maybe blow the doors off, metaphorically. Maybe."
    
    menu:
        "Search for answers":
            jump mystery_discussion
        "Stay put and observe":
            jump normal_life

label mystery_discussion:
    "As they explore, the group finds an old, dusty notice pinned to a bulletin board. The paper is aged, the words chilling."
    
    reika "There was an incident here five years ago. A group of students disappeared. No trace. No explanations. No escape."
    
    yui "Okay, now I officially don’t like this place."
    
    tatsuya "Then let’s train, strategize, and find a way to fight back. We won’t just sit here."
    
    hibiki "Ah, but... you can’t fight everything. Sometimes, you need to listen to the silence."
    
    renji "I need access to any systems. If there’s data, I’ll find it."
    
    shoma "Someone covered this up. If they did it once, they’ll do it again."
    
    misaki "A ghost story, perhaps. But ghosts don’t lock doors or erase files. This is someone’s plan."
    
    "The mystery deepens... but will they uncover the truth before it’s too late?"
    
    return

label normal_life:
    "The group decides to wait and observe, but the silence around them feels too planned."
    
    reika "Even if we ignore it, the truth has a way of coming out."
    
    misaki "Like a story that keeps unfolding, whether we like it or not..."
    
    reika "I need to look on something."
    
    renji "Bro I am cooked fr"

    "Strange... "

    shoma "Huh?"

    shoma "What is this?"

    "Reika Aoyama checks in"

    menu:
        "Read the text.":
            jump box
        "Keep discovering the place.":
            jump discover
        

    label box:
        "Reads the text..."

        "..."

        reika "Strange"
        
        return

    label discover:
        Hibiki "Ahahahahah"

        "Renji shocked fucking idk"
        return



    return
