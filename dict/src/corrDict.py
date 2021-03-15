def findClientByName(clientsDict: dict, clientName: str):
    if clientName in clientsDict:
        return clientsDict[clientName]
    return None


def addClient(clientsDic: dict, clientName: str, clientNumber: int, clientStreet: str, clientCity: str):
    if findClientByName(clientsDic, clientName) is None:
        clientsDic[clientName] = {"number": clientNumber,
                                  "street": clientStreet,
                                  "city": clientCity}
        return True
    return False


def removeClient(clientsDic: dict, clientName: str):
    if findClientByName(clientsDic, clientName) is not None:
        del clientsDic[clientName]
        return True
    return False
