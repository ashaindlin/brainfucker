"""
Interpret Brainfuck code from the comfort of your Python shell.
"""
import brackets
import re

class Brainfucker:
    """
    To use Brainfucker, create an instance of the Brainfucker class and pass a
    string containing your Brainfuck program to the interpret method. It can
    contain comments; the text is cleaned before being interpreted.

    You can also use the clean method to remove non-Brainfuck characters from
    a program string without running the program.
    """

    def __init__(self, cells=9999, useASCII=True, verbose=False):
        """
        Construct a new Brainfucker instance.

        The cells array always contains at least 9999 cells, to be nice. The
        pointer is a index into the cell array, tracking program execution.
        """
        if cells < 9999:
            cells = 9999
        self.cells = [0]*cells
        self.pointer = 0
        self.useASCII = useASCII
        self.verbose = verbose

    def clean(self, program):
        """
        Remove all characters except '><+-.,[]' from program string and return
        a new string guaranteed to consist only of valid Brainfuck characters.
        """
        return re.sub('[^><+\-.,\[\]]', '', program)

    def interpret(self, program):
        """
        Interpret a string as a Brainfuck program.

        First, the string is stripped of non-Brainfuck characters and checked
        for balanced brackets. Unbalanced brackets after cleaning will raise an
        exception.

        Then, the program is run using the cell array and instruction pointer
        exposed as object properties. WARNING: Running multiple programs in a
        row without calling resetEnv can result in unpredictable behavior.

        The prompt for user input is 'bf> '. When giving input, be mindful of
        whether Brainfucker is running in ASCII or non-ASCII (numerical) mode.
        """
        program = self.clean(program)
        if not self.isBalanced(program):
            raise Exception("Unbalanced brackets")
        location = 0
        v = 0
        while location < len(program):
            instruction = program[location]
            if self.verbose and instruction != '[':
                if self.pointer > v:
                    v = self.pointer
                print "   "*self.pointer, 'v'
                print self.cells[0:(v+1)]
            if instruction == '+':
                self.cells[self.pointer] += 1
                location += 1
            elif instruction == '-':
                self.cells[self.pointer] -= 1
                location += 1
            elif instruction == '>':
                self.pointer += 1
                location += 1
            elif instruction == '<':
                self.pointer -= 1
                location += 1
            elif instruction == '.':
                if self.useASCII:
                    print str(unichr(self.cells[self.pointer]))
                else:
                    print self.cells[self.pointer]
                location += 1
            elif instruction == ',':
                p = raw_input('bf> ')
                if self.useASCII:
                    self.cells[self.pointer] = ord(p[0])
                else:
                    self.cells[self.pointer] = int(p)
                location += 1
            elif instruction == '[':
                if self.cells[self.pointer] == 0:
                    location = brackets.match(program, location)
                else:
                    location += 1
            elif instruction == ']':
                if self.cells[self.pointer] == 0:
                    location += 1
                else:
                    location = brackets.match(program, location)
            else:
                raise Exception("Invalid character in program.")

    def isBalanced(self, program):
        """
        Return True if brackets in program are balanced and False if not.
        """
        matches = 0
        for char in program:
            if char == '[':
                matches += 1
            elif char == "]":
                matches -= 1
                if matches < 0:
                    return False
        return matches == 0

    def resetEnv(self):
        """
        Set cell array to all 0s and instruction pointer to first cell.
        """
        self.cells = [0 for _ in self.cells]
        self.pointer = 0
