import random

import pygame.image


class Fake:
    nameList = ["Sword", "Assault Rifle", "Pistol", "Cool Sword", "Piercing Gun" "Rage", "Invisibility", "Blood Bag",
                "Ammo Pack", "Apple"]
    descriptList = ["Your starting weapon came back to haunt you until you buy it again!",
                    "Pew pew... pew pew pew... pewpewpew!",
                    "It's a gun and it works. It might not be the best, but what other choice do you have?",
                    "Hey, this sword is all shiny and stuff, that must mean it's good.",
                    "Nothing can stop this bullet!"
                    "WHY DOESN'T THIS BUG GO AWAY! WHY! (Gain increase fire rate and heal for each enemy killed)",
                    "Why does nobody notice me? (Become invisible and gain fire rate)",
                    "Look at all those dead bodies you just made... It would be terrible if all those blood goes to waste. (Heal 20 health)",
                    "It's just ammo, nothing to say about it (gain 25% of ammo for your equipped weapon)"
                    "An Apple a day keeps the dentists away (Increase max health by 20)"
                    ]
    def __init__(self):
        num = random.randint(0, len(Fake.nameList)-1)
        self.name = Fake.nameList[num]
        self.description = Fake.descriptList[num]