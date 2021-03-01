import unittest
import sys

import student_ans as student
import corrDegree as correct


class TestEquation(unittest.TestCase):

    def test_not_none(self):
        rep = "Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument \nalors que la réponse " \
              "attendue est {}. Cela signifie qu'il manque un return ou que votre fonction \nretourne None alors que" \
              "les solutions sont réelles."
        args = ((2, -1, -1), (20, 5, -5), (2, 5, -5))
        for (a, b, c) in args:
            try:
                student_ans = student.secondDegree(a, b, c)
            except Exception as e:
                self.fail(
                    "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, (a, b, c)))
            correct_ans = correct.secondDegree(a, b, c)
            self.assertIsNotNone(student_ans, msg=rep.format(student_ans, (a, b, c), correct_ans))

    def test_must_be_none(self):
        rep = "Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument \nalors que la réponse " \
              "attendue est {}. Cela signifie que la fonction retourne des valeurs alors qu'elle devrait retourner\n" \
              "None puisque les solutions sont irréelles."
        args = ((1, 0, 1), (3, 1, 1), (10, 10, 30))
        for (a, b, c) in args:
            try:
                student_ans = student.secondDegree(a, b, c)
            except Exception as e:
                self.fail(
                    "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, (a, b, c)))
            correct_ans = correct.secondDegree(a, b, c)
            self.assertIsNone(student_ans, msg=rep.format(student_ans, (a, b, c), correct_ans))

    def test_values(self):
        rep = "Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse " \
              "attendue est {}.\nCela signifie qu'il y a une erreur de calcul ou que vous n'avez pas ordonné votre " \
              "liste."
        args = ((2, -1, -1), (20, 5, -5), (2, 5, -5))
        for (a, b, c) in args:
            try:
                student_ans = student.secondDegree(a, b, c)
            except Exception as e:
                self.fail(
                    "Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, (a, b, c)))
            correct_ans = correct.secondDegree(a, b, c)
            self.assertListEqual(student_ans, correct_ans, msg=rep.format(student_ans, (a, b, c), correct_ans))


if __name__ == '__main__':
    unittest.main()
