
def f21(path):
    if path[2] == 'shen':
        return 11
    if path[2] == 'opa':
        if path[0] == 'golo':
            if path[4] == 2020:
                if path[1] == 'tex':
                    return 0
                elif path[1] == 'arc':
                    return 1
                elif path[1] == 'go':
                    return 2
            elif path[4] == 1985:
                if path[1] == 'tex':
                    return 3
                elif path[1] == 'arc':
                    return 4
                elif path[1] == 'go':
                    return 5
        if path[0] == 'eagle':
            if path[1] == 'tex':
                if path[4] == 2020:
                    return 6
                elif path[4] == 1985:
                    return 7
            elif path[1] == 'arc':
                if path[4] == 2020:
                    return 8
                elif path[4] == 1985:
                    return 9
            elif path[1] == 'go':
                return 10

f21(['eagle', 'tex', 'shen', 1987, 2020])
#'eagle', 'tex', 'shen', 1987, 2020
#'eagle', 'arc', 'opa', 1987, 2020