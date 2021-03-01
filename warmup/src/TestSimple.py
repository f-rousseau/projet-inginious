#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import list as student
import corrSimple as correct


class TestSimple(unittest.TestCase):
    def test_simple(self):
        try:
            student_ans = student.mylist
        except Exception as e:
            self.fail(
                "Votre fonction a provoqué l'exception {}: {}".format(type(e), e))
        correct_ans = correct.mylist
        self.assertEqual(student_ans,correct_ans,msg="Il s'agit sûrement d'une erreur d'inattention ou de syntaxe, assurez-vous de bien avoir incrementé de 1 et d'avoir classé la liste dans l'ordre croissant")
        
if __name__ == '__main__':
    unittest.main()
