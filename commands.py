import helpers

class Command:
    def __init__(self, name="", alias=[],cmd="",helptext=""):
        self.name = name #Name of command, automatically checks for match
        self.alias = alias #List of regexes to run program if there's a match
        self.cmd = cmd #Command to execute
        self.helptext = helptext
        
    def execute(self, args=None):
        output = ""
        exec(self.cmd)
        return output
    
allCommands = []
#Built in commands go here
bHelp = Command("help",helptext="Displays the help list")
bHelp.cmd = """for command in allCommands:
    output += command.helptext
    output += '\n'"""
allCommands.append(bHelp)