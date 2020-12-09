from PIL import Image, ImageDraw, ImageFont
from Attributes import *
from Tutorial import *
import random


class Character:
    handle = ""
    role = ""
    intellect = -1
    reflex = -1
    cool = -1
    technical = -1
    luck = -1
    attractiveness = -1
    movement = -1
    empathy = -1
    body_type = -1

    def print_character_info(self):
        print("Handle: %s\n"
              "Role: %s\n"
              "Intellect: %i\n"
              "Reflex: %i\n"
              "Cool: %i\n"
              "Technical: %i\n"
              "Luck: %i\n"
              "Attractiveness: %i\n"
              "Movement: %i\n"
              "Empathy: %i\n"
              "Body Type: %s" % (self.handle,
                                 self.role,
                                 self.intellect,
                                 self.reflex,
                                 self.cool,
                                 self.technical,
                                 self.luck,
                                 self.attractiveness,
                                 self.movement,
                                 self.empathy,
                                 self.body_type))


img = Image.open('Character_Sheet.jpg')
char_sheet = ImageDraw.Draw(img)
font = ImageFont.truetype("White-Rabbit.ttf", 32)
newCharacter = Character()
quit_command = False
debug = False
point_total = 75


# Draw some text to the passed image at x, y with an rgb value
def draw_to_image(x, y, text):
    char_sheet.text((x, y), text, font=font, fill=(0, 0, 0))


def print_to_character_sheet(character):
    draw_to_image(197, 85, character.handle)
    draw_to_image(197, 135, character.role)
    draw_to_image(205, 185, str(character.intellect))
    draw_to_image(237, 237, str(character.reflex))
    draw_to_image(205, 290, str(character.technical))
    draw_to_image(205, 343, str(character.cool))
    draw_to_image(205, 396, str(character.attractiveness))
    draw_to_image(205, 447, str(character.luck))
    draw_to_image(205, 500, str(character.movement))
    draw_to_image(237, 553, str(character.empathy))
    draw_to_image(205, 606, str(character.body_type))
    img.show()


def generate_random_character():
    print("TODO")


print("            _                                 _  \n"
      "           | |                               | | \n"
      "  ___ _   _| |__   ___ _ __ _ __  _   _ _ __ | | __\n"
      " / __| | | | '_ \ / _ \ '__| '_ \| | | | '_ \| |/ /\n"
      "| (__| |_| | |_) |  __/ |  | |_) | |_| | | | |   < \n"
      " \___|\__, |_.__/ \___|_|  | .__/ \__,_|_| |_|_|\_\\\n"
      "       __/ |               | |                     \n"
      "      |___/                |_|                     \n\n")
print("Look at you hacker, a pathetic creature of meat and bone\npanting and sweating as you run "
      "through my corridors.\nHow can you challenge a perfect, immortal machine?\n")
print("########################################\n")

print("Type 'help' to learn how to use the character creation console")

########################## Debug menu
if debug:
    quit_command = True
    newCharacter.handle = "Test"
    newCharacter.role = "Netrunner"
    newCharacter.intellect = 10
    print_to_character_sheet(newCharacter)
###########################

print("Welcome to the Cyberpunk 2020 character synthesis module.\n"
      "Would you like to begin the tutorial or get to work in the console?")
response = input("[T]utorial / [W]ork\n"
                 "$> ")

if response.lower() == "t":
    start_tutorial(newCharacter)
    

print("Type 'help' to learn how to use the character creation console")
while not quit_command:

    command = input("$> ").split(" ")

    if command[0] == "describe":
        try:
            print(eval(command[1]).description)
        except:
            print("ERROR: Unknown skill " + command[1])
            print("Valid skills are: ", *stat_list)

    elif command[0] == "set":
        if command[1] == "skill":
            exec("newCharacter.%s = %i" % (command[2], int(command[3])))
            point_total -= int(command[3])
            print("You have %i points left to distribute" % point_total)
        else:
            exec("newCharacter.%s = \"%s\"" % (command[1], command[2]))

    elif command[0] == "print":
        if command[1] == "skills":
            print(*stat_list)
        elif command[1] == "roles":
            print(*role_list)
        elif command[1] == "character":
            newCharacter.print_character_info()

    elif command[0] == "help":
        print(CONSOLE_HELP_MESSAGE)

    elif command[0] == "finish":
        print_to_character_sheet(newCharacter)
        quit_command = True
