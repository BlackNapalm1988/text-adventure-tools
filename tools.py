# Text Based Adventure Tools
# Abstraction of the story-telling, branching into a dedicated txt file using the RPGML Language.


class Interpreter():
    """
    Takes a loaded dictionary of one or more script files and loads them in.
    """

    # tags = [
    #     "dialog",
    #     "prompt",
    #     "begin",
    #     "end",
    #     "next",
    #     "branch",
    #     "option",
    # ]

    def __init__(self, scripts: dict):
        self.scripts = scripts
        self.text = ""
        self.branches = []
        self.options = []



    def start(self):

        def open_file():
            for index, path in enumerate(self.scripts):
                if index <= len(self.scripts):
                    with open(self.scripts.get(path)) as data:
                        read_file(data)
        
        def read_file(data: str):
            for line in data:
                for index, char in enumerate(line):
                    if char == "<":
                        open_tag = index
                    if char == ">":
                        close_tag = index
                
                tag = line[open_tag + 1:close_tag]
                tag_data = line[close_tag + 1:]

                tag.strip(" ")
                tag.capitalize()
                tag_data.strip(" ")
                tag_data.capitalize()

                process_tag(tag, tag_data)

        def process_tag(tag, tag_data):
            # for command in self.tags:
            #     if tag == command:
            #         print(tag_data)

            if tag == "dialog":
                self.dialog(tag_data)

            if tag == "prompt":
                self.prompt(tag_data)

            if tag == "begin":
                self.begin(tag_data)

            if tag == "end":
                self.end(tag_data)

            if tag == "next":
                self.next(tag_data)

            if tag == "branch":
                self.branch(tag)

            if tag == "option":
                self.option(tag_data)

        open_file()

    def dialog(self, text: str):
        print(text)

    def prompt(self, text: str):
        input(text)

    def begin(self, text: str):
        pass

    def end(self, text: str):
        pass

    def next(self, text: str):
        pass

    def branch(self, text: str):
        self.branches.append(text)

    def option(self, text: str):
        self.options.append(text)



