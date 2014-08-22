def match(string, pos):
    """
    Return the position of the matching bracket to the bracket at string[pos],
    or -1 if pos is an invalid index or string[pos] is not a bracket.

    Works for parentheses, square brackets, and curly braces.
    """
    if pos not in range(len(string)) or string[pos] not in "([{}])":
        return -1
    else:
        partner = { "(": ")", "[": "]", "{": "}", "}": "{", "]": "[", ")": "(" }
        matched = 1
        newPos = pos
        while matched > 0:
            if string[pos] in "([{":
                newPos += 1
            else:
                newPos -= 1
            if string[newPos] == string[pos]:
                matched += 1
            elif string[newPos] == partner[string[pos]]:
                matched -= 1
        return newPos

def isBalanced(program):
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
