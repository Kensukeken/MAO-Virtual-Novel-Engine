define r = Character("Rikano Ayatsuki", color="#8B0000") # Main Character
define i = Character("Itsuki Nekomori", color="#4B0082") # Mastermind (The creator of the game)
define k = Character("Kaoru Shigetsu", color="#228B22") # Computer Science Major
define t = Character("Tsubasa Kiryuu", color="#8B4513") # The Politics Major
define n = Character("Misaki Yoruhime", color="#DC143C") # The English Major
define y = Character("Yui Hizakura", color="#FF8C00") # The Chemistry Major
define m = Character("Masaru Takeyoshi", color="#4682B4") # The Gym Enthusiast

default has_mystery_unfolded = False

label start:    
    "The first day of university should have been normal. Instead, seven students wake up inside an unfamiliar campus—one that none of them remember entering."
    
    r "This... isn't where we were supposed to be. Something's off."
    
    i "Interesting. If this is a {color=#FFFF00}game{/color}, someone set it on purpose."
    
    k "Locked doors. No internet. We're stuck. This isn't just a campus—it's a controlled place."
    
    t "If this is some {color=#FFFF00}game{/color}, who's running it? What do they want from us?"
    
    n "A twisted story unfolding around us. But every story has clues. We just need to look closer."
    
    m "Let's not waste time. If we're trapped, we'll find a way out."
    
    y "Or... maybe blow the doors off, metaphorically. Maybe."
    
    menu:
        "Search for answers":
            jump mystery_discussion
        "Stay put and observe":
            jump normal_life
    
    label mystery_discussion:
        "As they explore, the group finds an old, dusty notice pinned to a bulletin board. The paper is aged, the words chilling."
        
        r "There was an incident here five years ago. A group of students disappeared. No trace. No explanations. No escape."
        
        y "Okay, now I officially don't like this place."
        
        m "Then let's train, strategize, and find a way to fight back. We won't just sit here."
        
        i "Ah, but... you can't fight everything. Sometimes, you need to listen to the silence."
        
        k "I need access to any systems. If there's data, I'll find it."
        
        t "Someone covered this up. If they did it once, they'll do it again."
        
        n "A ghost story, perhaps. But ghosts don't lock doors or erase files. This is someone's plan."
        
        "The mystery deepens... but will they uncover the truth before it's too late?"
        
        return
    
    label normal_life:
        "The group decides to wait and observe, but the silence around them feels too planned."
        
        r "Even if we ignore it, the truth has a way of coming out."
        
        n "Like a story that keeps unfolding, whether we like it or not..."
        
        r "I need to look on something."
        
        k "Bro I am cooked fr"
        
        "Strange... "
        
        t "Huh?"
        
        t "What is this?"
        
        " Ayatsuki checks in"
        
        menu:
            "Read the text.":
                jump box
            "Keep discovering the place.":
                jump discover
        
        label box:
            "Reads the text..."
            
            "..."

            r "Strange"
            
            return
        
        label discover:
            i "Ahahahahah"
            
            "Kaoru shocked fucking idk"
            return
        
        return

