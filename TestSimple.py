import unittest
import list as student
import corrSimple as correct


class TestSimple(unittest.TestCase):
    def test_simple(self):
        rep = "votre code n'est pas correcte, "
        try:
            student_ans = student.mylist
        except Exception as e:
            self.fail(
                "Votre fonction a provoqué l'exception {}: {}".format(type(e), e))
        correct_ans = correct.mylist
        self.assertEqual(student_ans,correct_ans,msg="")



if __name__ == '__main__':
    unittest.main()
