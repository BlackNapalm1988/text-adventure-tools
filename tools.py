# Text Based Adventure Tools
# Abstraction of the story-telling, branching into a dedicated txt file using the RPGML Language.


class Interpreter():

    def __init__(self, scripts: dict):
        self.scripts = scripts
        self.text = ""
        self.branches = []
        self.options = []
        self.branch_count = 0

    def start(self):

        def open_file():
            for index, path in enumerate(self.scripts):
                if index <= len(self.scripts):
                    with open(self.scripts.get(path), 'r') as raw_data:
                        read_file(raw_data)
        
        def read_file(data: str):
            for line in data:
                for index, char in enumerate(line):
                    if char == "<":
                        open_tag = index
                    if char == ">":
                        close_tag = index
                
                tag = line[open_tag + 1:close_tag]
                tag_data = line[close_tag + 1:]

                process_tag(tag, tag_data)

        def process_tag(tag, tag_data):

            if tag == "dialog":
                self.dialog(tag_data)

            if tag == "prompt":
                player_response = self.prompt()

                if player_response == tag_data:
                    return player_response
                else:
                    return "Error"

            if tag == "begin":
                pass

            if tag == "end":
                self.end(tag_data)

            if tag == "next":
                self.next(tag_data)

            if tag == "branch":
                self.branch(tag_data)

            if tag == "option":
                self.option(tag_data)

        open_file()

    def dialog(self, text: str):
        print(text)

    def prompt(self):
        x = input(">> ")
        return x

    def begin(self, text: str): 
        pass

    def end(self, text: str):
        pass

    def next(self, text: str):
        pass

    def branch(self, tag_data):
        clean_tag = tag_data.strip().upper()
        self.branches.append([clean_tag])
        self.branch_count += 1

    def option(self, tag_data):
        clean_tag = tag_data.strip().upper()
        self.branches[self.branch_count - 1].append(clean_tag)