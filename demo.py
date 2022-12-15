from tools import Interpreter


scripts = {
    "Intro"         :  "storyline/intro.txt",
    "Chapter One"   :  "storyline/chapter_one.txt",
    "Chapter Two"   :  "storyline/chapter_two.txt",
    "Closing"       :  "storyline/closing.txt",
}

storyline = Interpreter(scripts)

storyline.start()

print(storyline.branches)
print(storyline.options)

# print(len(storyline.scripts))