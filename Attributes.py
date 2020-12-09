class Attribute:

    def __init__(self, str_name):
        self.name = str_name

    description = ""


stat_list = ["intellect", "reflex", "cool", "technical", "luck", "attractiveness", "movement", "empathy",
             "body_type"]
role_list = ["Rockerboy", "Solo", "Netrunner", "Corporate", "Techie", "Cop", "Fixer", "Media"]

intellect = Attribute("INT")
intellect.description = "This is a measure of your problem solving ability; figuring out problems,\n" \
                        "noticing things, remembering information. Almost every character type will need\n" \
                        "a high intelligence, with Netrunners and Corporates requiring the highest of all."

reflex = Attribute("REF")
reflex.description = "This is a combined index, covering not only your basic dexterity, but also how your level of\n" \
                     "physical coordination will affect feats of driving, piloting, fighting and athletics.\n" \
                     "Characters who intend to engage in a great deal of combat (such as Solos, Nomads or Rockerboys)\n" \
                     "should always invest in the highest possible Reflex."

cool = Attribute("COL")
cool.description = "This index measures how well the character stands up to stress, fear, pressure, physical pain,\n" \
                   "and/or torture.  In determining your willingness to fight on despite wounds or your fighting\n" \
                   "ability under fire, Cool (CL) is essential.  It is also a measure of how \"together\" your character\n" \
                   "is and how tough he/she appears to others. Rockerboys and Fixers should always have a high Cool,\n" \
                   "with Solos and Nomads having the highest of all."

technical = Attribute("TECH")
technical.description = "This is an index of how well you relate to hardware and other technically oriented things.\n" \
                        "In Cyberpunk, the ability to use and repair technology is or paramount importance -- TECH\n" \
                        "will be the stat used when fixing, repairing and attempting to use unfamiliar tech.\n" \
                        "While all characters should have a decent Tech stat, potential Techies should always opt\n" \
                        "for the highest possible score in this area."

luck = Attribute("LK")
luck.description = "This is the intangible \"something\" that throws the balance of events into your favor.\n" \
                   "your luck represents how many points you may use each game to influence the outcome of a critical\n" \
                   "event.  To use Luck, you may add any or all of the points of luck a character has to a critical\n" \
                   "die roll (declaring your intention to use luck before the roll is made) until all of your luck\n" \
                   "stat is used up.  Luck is always restored at the end of each game session."

attractiveness = Attribute("ATT")
attractiveness.description = "This is how good-looking you are.  In Cyberpunk, it's not enough to be good -- you have\n" \
                             "to look good while you're doing it (Attitude is Everything).\n" \
                             "Attractiveness is especially important to Medias and Rockerboys, as being good-looking\n" \
                             "is part of their job."

movement = Attribute("MA")
movement.description = "This is an index of how fast your character can run (important in combat situations).\n" \
                       "The higher your Movement Allowance (MA), the more distance you can cover in a turn."

empathy = Attribute("EM")
empathy.description = "This stat represents how well you relate to other living things - a measure of charisma\n" \
                      "and other sympathetic emotions. In a world of alienated, future-shocked survivors, the ability\n" \
                      "to be \"human\" can no longer be taken for granted. Empathy (EM) is critical when leading,\n" \
                      "convincing, seducing, or perceiving emotional undercurrents.\n" \
                      "Empathy is also a measure of how close he/she is to the line between feeling human being\n" \
                      "and cold blooded cyber-monster."

CONSOLE_HELP_MESSAGE = "This is the console, the place where you will define the skills of your character.\n" \
                       "There are a few commands you can use to set your characters attributes, these are:\n" \
                       "- describe [attribute]\n" \
                       "set (handle, role) [value]\n" \
                       "If you want to set a skill, just use: set skill [skill name] [value]" \
                       "print (character, skills, roles) - prints out your current character sheet or a list of the " \
                       "skills.\n" \
                       "There are a few things you have to do to create your character:\n" \
                       "1. Select your role: you can see the available roles by typing: print roles\n" \
                       "2. Distribute your character points: You will have 75 points to distribute across all skills.\n" \
                       "No skill may be lower than 2 or higher than 10.  You can manually distribute these points\n" \
                       "by using set [attribute] [skill] or by typing set random, which will create random rolls for\n" \
                       "all of your skills.\n" \
