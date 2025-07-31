def arraysCompareTo(listContain: list, listCompareTo: list):
    if listContain is not None and listCompareTo is not None:
        for string in listContain:
            if string in listCompareTo:
                return True, f"No se encuentra en el codigo: {string}"
    return False, None

def codeCompareTo(codes: list, restrictions: list):
    if codes is not None and restrictions is not None:
        tempCodes = [item.replace(' ', '').replace('\n', '') for item in codes]
        tempRestrictions = [item.replace(' ', '').replace('\n', '') for item in restrictions]
        position = 0
        for string in tempRestrictions:
            if string not in tempCodes:
                return True, f"No se encuentra en el codigo: {codes[position]}"
            position += 1
        position = 0

        for string in codes:
            if len(codes) == 1:
                break
            if str(string).lower() in tempRestrictions:
                codes.remove(string)
    return False, codes