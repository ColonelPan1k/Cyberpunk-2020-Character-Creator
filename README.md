# Cyberpunk-2020-Character-Creator
This is a little thing I made to make Cyberpunk 2020 character creation a bit easier.  I had a bit of fun and made a very basic REPL to allocate skill points and 
set different character values.  In the future, I'd like to add some kind of scripted tutorial. I'm also reworking the REPL loop to be much cleaner.

# Use
For now, there are a few commands that can be used.  
- Describe: This will describe a given attribute (text taken from the Cyberpunk 2020 player handbook).
  describe [skill]
  
- Set: This will set a skill, handle or role.  The skill can be changed at any time by just running the same command again
  The command can either be run with "set skill [skill]" or with "set [role, handle] [custom role/handle]"
  
- Print: Prints out any info for roles or skills, along with the current stat sheet of the character you're making.  
  print [role/skill] or print [character]
  
- Help: Prints out a help message which describes the available functions in the program.  

- Finish: Finalizes all the information and writes it to a character sheet.  The character sheet will be saved in whichever file the main .py program is run from.
  
