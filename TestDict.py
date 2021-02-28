import unittest
import sys

import corrDict as correct
import corrDictStudent as student


class MyDict(unittest.TestCase):

    def test_find_0(self):
        rep = "Votre fonction a trouvé une personne {} lorsqu'elle a été appellée avec {} alors que {} n'existait pas " \
              "dans la liste.\nVotre fonction devait retourner None "
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
        client = "Fanchon"
        try:
            student_ans = student.findClientByName(clients, client)
        except Exception as e:
            self.fail(
                "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, client))
        self.assertIsNone(student_ans, msg=rep.format(student_ans, client, client))

    def test_find_1(self):
        rep = "Votre fonction a retourné {} lorsqu'elle a été appellée avec {} alors que la bonne réponse était {}. " \
              "\nCela signifie que votre aglorithme de recherche n'est pas bon."
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
        client = "Rousseau"
        try:
            student_ans = student.findClientByName(clients, client)
            print(student_ans)
        except Exception as e:
            self.fail(
                "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, client))
        correct_ans = correct.findClientByName(clients, client)
        print(correct_ans)
        self.assertEqual(student_ans, correct_ans, msg=rep.format(student_ans, client, correct_ans))

    def test_add_0(self):
        rep = rep = "Votre dictionnaire de clients était {} lorsque votre fonction est appelée avec {} comme argument " \
                    "\nalors que la réponse attendue est {} puisque le client était déjà présent dans le dictionnaire"
        clients_student = {"Fanchon": {
            "number": 58,
            "street": "Rue des Wallons",
            "city": "Louvain-la-Neuve"}
        }
        clients_correct = {"Fanchon": {
            "number": 58,
            "street": "Rue des Wallons",
            "city": "Louvain-la-Neuve"}
        }
        params = ("Fanchon", 58, "Rue des Wallons", "Louvain-la-Neuve")
        try:
            student_ans = student.addClient(clients_student, params[0], params[1], params[2], params[3])
        except Exception as e:
            self.fail(
                "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, params))
        correct_ans = correct.addClient(clients_correct, params[0], params[1], params[2], params[3])
        self.assertEqual(clients_student, clients_correct, msg=rep.format(clients_student, params, clients_correct))

    def test_add_1(self):
        rep = rep = "Votre dictionnaire de clients était {} lorsque votre fonction est appelée avec {} comme argument \nalors que la réponse " \
                    "attendue est {}."
        clients_student = {}
        clients_correct = {}
        params = ("Fanchon", 58, "Rue des Wallons", "Louvain-la-Neuve")
        try:
            student_ans = student.addClient(clients_student, params[0], params[1], params[2], params[3])
        except Exception as e:
            self.fail(
                "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, params))
        correct_ans = correct.addClient(clients_correct, params[0], params[1], params[2], params[3])
        self.assertEqual(clients_student, clients_correct, msg=rep.format(clients_student, params, clients_correct))

    def test_add_0(self):
        rep = rep = "Votre dictionnaire de clients était {} lorsque votre fonction est appelée avec {} comme argument " \
                    "\nalors que la réponse attendue est {} puisque le client était présent dans le dictionnaire"
        clients_student = {"Fanchon": {
            "number": 58,
            "street": "Rue des Wallons",
            "city": "Louvain-la-Neuve"}
        }
        clients_correct = {"Fanchon": {
            "number": 58,
            "street": "Rue des Wallons",
            "city": "Louvain-la-Neuve"}
        }
        params = ("Fanchon", 58, "Rue des Wallons", "Louvain-la-Neuve")
        try:
            student_ans = student.removeClient(clients_student, params[0])
        except Exception as e:
            self.fail(
                "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, params[0]))
        correct_ans = correct.removeClient(clients_correct, params[0])
        self.assertEqual(clients_student, clients_correct, msg=rep.format(clients_student, params[0], clients_correct))

    def test_remove_1(self):
        rep = rep = "Votre fontion a retourné {} lorsqu'elle est appelée avec {} comme argument \nalors que la réponse " \
                    "attendue est {} puisque le client n'était pas présent dans le dictionnaire."
        clients_student = {}
        clients_correct = {}
        params = ("Fanchon", 58, "Rue des Wallons", "Louvain-la-Neuve")
        try:
            student_ans = student.removeClient(clients_student, params[0])
        except Exception as e:
            self.fail(
                "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, params[0]))
        correct_ans = correct.removeClient(clients_correct, params[0])
        self.assertEqual(student_ans, correct_ans, msg=rep.format(student_ans, params[0], correct_ans))


if __name__ == '__main__':
    unittest.main()
