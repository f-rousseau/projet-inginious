clients = {
    "Hallaert": {
        "city": "Louvain-la-Neuve",
        "number": 23,
        "street": "Rue des Bruyères"
    },
    "Rousseau": {
        "city": "Louvain-la-Neuve",
        "number": 18,
        "street": "Rue Constantin Meunier"
    },
    "Pirson": {
        "city": "Sambreville",
        "number": 155,
        "street": "Rue des pierres"
    }
}


def findClientByName(clientsDict: dict, clientName: str):
    if clientName in clientsDict:
        return True
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


def findClientByAddress(clientsDic: dict, clientNumber: int, clientStreet, clientCity: str):
    for key, value in clientsDic.items():
        if value["number"] == clientNumber and value["street"] == clientStreet and value["city"] == clientCity:
            return key
    return None


print(findClientByName(clients, "Pirson"))
print(addClient(clients, "Marchese", 25, "Rue des débiles", "Outsiplou"))
print(clients)
print(removeClient(clients, "Pirson"))
print(clients)
print(findClientByAddress(clients, 23, "Rue des Bruyères", "Louvain-la-Neuve"))
