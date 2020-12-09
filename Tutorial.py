from Attributes import *



def start_tutorial(Object):
    tut_quit = False
    total_points = 75

    print("Welcome to the Cyberpunk 2020 character synthesis tutorial.\n"
          "This tool will guide you through the use of the character synthesis console.\n"
          "First, let's begin by giving your character a handle. Enter it in the space below.\n")

    Object.handle = input("$> ")

    print("Next, you will need to choose a role for your character.\n"
          "There are a number of various roles you can fulfill within Cyberpunk 2020.\n"
          "To print out a list of available roles, type in \"print roles\", to learn more about a role\n"
          "type 'describe [role]"
          "Once you have picked a role, type 'set role [role]")
    while not tut_quit:
        command = input("$> ").split()

        if command[0] == "print":
            if command[1] == "roles":
                print(*role_list)

        elif command[0] == "describe":
            print(eval(command[1]).description)

        elif command[0] == "set":
            exec("Object.role = \"%s\"" % command[2])
            tut_quit = True

    tut_quit = False
    print("Next, you will have to designate your character points.\n"
          "These will determine how effective your character is at a given action.\n"
          "There are 75 total character points to distribute across nine different skills.\n"
          "To set a skill, type 'set skill [skill] [value].  If you want to learn more about a skills\n"
          "type 'describe [skill].  If you would like to print a list of all skills, type 'print skills'")

    while not tut_quit:
        if total_points == 0:
            print("All character points have been allocated")
            tut_quit = True # Bug here - hangs instead of quitting

        command = input("$> ").split()

        if command[0] == "set":
            if int(command[3]) > 10 or int(command[3]) < 2:
                print("Skills are not able to be higher than 10 or lower than 2")
            else:
                exec("Object.%s = int(\"%s\")" % (command[2], command[3]))
                total_points -= int(command[3])
                print("You have %i point(s) remaining" % total_points)

        elif command[0] == "describe":
            print(eval(command[1]).description)

        elif command[0] == "print":
            print(*stat_list)


    print("Now that your skill points are properly allocated, this process is finished.\n"
          "You may continue to further edit your character or print your character sheet.")
    choice = input("[C]ontinue / [F]inish\n"
                   "$> ")
    if choice.lower() == "C":
        return
