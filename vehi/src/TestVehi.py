import unittest
import sys

import corrVehicle as correct
import vehi as student


class TestVehicle(unittest.TestCase):

    def test0_0(self):
        lst = [("Peugeot", True, True, 5), ("Ducati", True, False, 2), ("Trek", False, False, 1)]
        rep = _(
            "Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}. Cela signifie que votre classe ne contient pas ou a un mauvais self.brand")
        for args in lst:
            try:
                student_ans = student.Vehicle(args[0], args[1], args[2], args[3])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, args))
            correct_ans = correct.Vehicle(args[0], args[1], args[2], args[3])
            self.assertEqual(student_ans.brand, correct_ans.brand,
                             rep.format(student_ans.brand, args, correct_ans.brand))

    def test0_1(self):
        lst = [("Peugeot", True, True, 5), ("Ducati", True, False, 2), ("Trek", False, False, 1)]
        rep = _(
            "Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}. Cela signifie que votre classe ne contient pas ou a un mauvais self.hasMotor")
        for args in lst:
            try:
                student_ans = student.Vehicle(args[0], args[1], args[2], args[3])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, args))
            correct_ans = correct.Vehicle(args[0], args[1], args[2], args[3])
            self.assertEqual(student_ans.hasMotor, correct_ans.hasMotor,
                             rep.format(student_ans.hasMotor, args, correct_ans.hasMotor))

    def test0_2(self):
        lst = [("Peugeot", True, True, 5), ("Ducati", True, False, 2), ("Trek", False, False, 1)]
        rep = _(
            "Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}. Cela signifie que votre classe ne contient pas ou a un mauvais self.hasBody")
        for args in lst:
            try:
                student_ans = student.Vehicle(args[0], args[1], args[2], args[3])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, args))
            correct_ans = correct.Vehicle(args[0], args[1], args[2], args[3])
            self.assertEqual(student_ans.hasBody, correct_ans.hasBody,
                             rep.format(student_ans.hasBody, args, correct_ans.hasBody))

    def test0_3(self):
        lst = [("Peugeot", True, True, 5), ("Ducati", True, False, 2), ("Trek", False, False, 1)]
        rep = _(
            "Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}. Cela signifie que votre classe ne contient pas ou a un mauvais self.seats")
        for args in lst:
            try:
                student_ans = student.Vehicle(args[0], args[1], args[2], args[3])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, args))
            correct_ans = correct.Vehicle(args[0], args[1], args[2], args[3])
            self.assertEqual(student_ans.seats, correct_ans.seats,
                             rep.format(student_ans.seats, args, correct_ans.seats))

    def test1(self):
        lst = [("Peugeot", True, True, 5), ("Ducati", True, False, 2), ("Trek", False, False, 1)]
        rep = _(
            "Votre fonction __str__ a retourné {} lorsque la classe Vehicle est créée avec {} comme argument alors que la réponse pour __str__ attendue est {}")
        for args in lst:
            try:
                student_ans = student.Vehicle(args[0], args[1], args[2], args[3])
            except Exception as e:
                self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e, args))
            correct_ans = correct.Vehicle(args[0], args[1], args[2], args[3])
            self.assertEqual(student_ans.__str__(), correct_ans.__str__(),
                             rep.format(student_ans.__str__(), args, correct_ans.__str__()))


if __name__ == '__main__':
    unittest.main()
