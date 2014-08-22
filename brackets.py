def match(string, pos):
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
