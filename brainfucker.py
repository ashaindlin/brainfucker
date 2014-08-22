import brackets
import re

class Brainfucker:

    def __init__(self, cells=10000, useASCII=True, verbose=False):
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
