# Project 1: Alien invasion, p.225


# Chapter 12: A ship that fires bullets, p.227
""" 
Planning your project, p.228
Installing pygame, p.228
Startomg the game project, p.229
    Creating a pygame window and responding to user input, p.229
        alien_invasion.py
    Setting the background color, p.230
    Creating a settings class, p.231
        settings.py
    Adding the ship image, p.232
    Creating the ship class, p.233
    Drawing the ship to the screen, p.235
Refactoring: _check_events() and _update_screen(), p.236
    The _check_events() methogd, p.236
    The _update_screen() method, p.237
Try it yourself, p.238
        --- Moved to 'raiders_python: raiders.py' ---
Piloting the ship, p.238
    Responding to a keypress, p.238
    Allowing continuous movement
    Moving both left and right
    Adjusting the ship's speed, p.241
    Limiting the ship's range, p.243
    Refactoring _check_events(), p.243
    Running the game in fullscreen mode, p.244
A quick recap, p.245
    alien_invasion.py
    settings.py
    ship.py

Try it yourself, p.246
    12.4 rocket.py
    12.5 keys.py

Shooting bullets, p.246
    Adding the bullet settings, p.247
    Storing bullets in a group, p.248
    Firing bullets, p.249
    Deleting old bullets, p.250
    Limiting the number of bullets, p.251
    Creating the _update_bullets method, p.252
"""
#Try it yourself, p.253
"""
    12.6 Sideways shooter
        sideways_shooter.py
"""


# Chapter 13 Aliens, p.255
"""
Reviewing the project, p.256
    Creating the alien class, p.257
    Creating an instance of the alien, p.258
    Building the alien fleet, p.259
        Determining how many aliens fit in a row
        Creating a row of aliens
        Refactoring _create_fleet()
        Addiing rows

# Try it yourself, p.264
    13.1 Stars
    13.2 Better stars

Making the fleet move, p.265
     Moving the aliens right, p.265
     Creating setting for fleet direction, p.266
     Checking wether an alien had hit the edge, p.266
     Dropping the fleet and changing direction, p.267

# Try it yourself, p.268
    13.3 Raindrops
    # ToDo: 13.4 More rain
    
Shooting aliens, p.268
    Detecting bullet collisions, p.268
    Making bullets larger for testin, p.270
    Repopulating the fleet, p.270
    Speeding up the bullets, p.271
    Refactoring _update_bullets(), p.271

# Try it yourself, p.272
    # ToDo: 13.5 Sideways Shooter Part 2
    \Dev\pcc\sideway_shooter

Ending the game, p.272
    Detecting alien and ship collisions, p.272
    Responding to alien and ship collisions, p.273
    Aliens that reach the bottom of the screen, p.276
    Game over! p.276
"""


# Chapter 14 Scoring, p.279
"""
Adding the Play button, p.280
    Creating a Button class, p.280
    Drawing the button to the screen, p.281
    Resetting the game, p.283

# Try it yourself, p.285 
    14.1 Press P to Play, p.285
    # ToDo: 14.2 Target practice, p.285

Leveling up, p.285
    Modifying the speed settings, p.285
    Resetting the speed, p.287

# Try it yourself, p.288
    # ToDo: 14.3 Challenging target practice
    # ToDo: 14.4 Difficulty levels

Scoring, p.288
    Displaying the score, p.288
    Making a scoreboard, p.289
    Updating the score as aliens are shot down, p.291
    Resetting the score, p.291
    Making sure to score all hits, p.292
    Increasing point values, p.292
    Rounding the score, p.293
    High scores, p.294
    Displaying the level, p.296
    Displaying the number of ships, p.298

# Try it yourself, p.301
    14.5 All-time high score
    14.6 Refactoring 
    
    # ToDo: 
    prep_high_score() in scoreboard.py

    # ToDo:     
    _check_bullet_alien_collisions()
        - Create start_new_level()
    
    # ToDo: 
    Scoreboard __init__()
        - Create prep_images()
        - Simplify _start_game() with prep_images()
    
    14.7 Expanding the game
    14.8 Sideways Shooter, final version
"""

