# Text Adventure Tools

## Introduction
Python tools for converting marked-up txt files into high-level game layouts. Text file should be written in a linear fashion as the parser will start from the top of the document and work its way down. This tool is a work in progress and there are many new features to be added in th future.

This tool does not handle the low-level logic, you will still need to code this and adjust as necessary. It will handle the repetitive print statements and branching code. This level of abstraction will allow the story to be handled independently and the game-code can speak for itself.

## Use Cases
The main expectation is to use these tools to allow quick and rapid text based adventure games in you terminal. But take a look at the code, if you think there are some other use cases, such as a need for dialog and branch management in any games, scripts then your help is truly appreciated. The script is envisioned like a tree in which you game code is the trunk, each choice the user makes is like a branch and each ending game point is a leaf.

## RPGML (RPG Markup Language)
This is the language you will need to use and style your text, the list is a work in progress and to be honest i'm at a loss for a better name. But here are some example tags that will be implemented. As the project progresses we will add more tags as necessary, these are the most important.

- <begin> "Anything after this is considered a comment and ignored, could be used for labeling, etc."
Use this code at the beginning of your script file to tell the interpreter that the following data needs to be ran on a line by line basis.

- <next> "N/A"
Use this to proceed to the next file in the dictionary and load it in. Typically when writing you script files, I would recommend breaking them down into chapters or branches as you will see later.

- <end> "Anything after this is considered a comment and ignored, could be used for labeling, copyright, version-info, etc."
Use this tag to tell the interpreter that the file is done and it will close out of the loop. You will throw an index error if you don't to the last file in the dictionary.

- <dialog> "String"
Use this tag to print to the terminal for dialog and story-telling purposes. Similar to the python print() method.

- <prompt> "String"
Use this tag to get information from the user, similar to the python input() method.

- <branch> "Branch Name"
Use this tag to begin a new branching section that will be followed by an indented section in you text file that give the user to naviagte down the associated branch.

- <option> "Option Name, this will be saved in the list that will be returned to implement your game logic."
Use this tag after a branch to create multiple options for the user to choose from, if used outside a branch this will store it in the main trunk and may not be accessible later if the list is cleared.
