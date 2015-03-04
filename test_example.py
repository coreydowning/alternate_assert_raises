import sys
import unittest

class OtherException(Exception):
    pass

class RealException(Exception):
    pass

def function_under_test():
    raise RealException('hey!')
    
def other_function():
    pass

class CurrentAssertRaisesTest(unittest.TestCase):
    def test_passing(self):
        self.assertRaises(RealException, function_under_test)

    def test_failing(self):
        self.assertRaises(OtherException, function_under_test)

class NewAssertRaisesTest(unittest.TestCase):
    def alternateAssertRaises(self, excClass, callableObj, *args, **kwargs):
        try:
            callableObj(*args, **kwargs)
            raise self.failureException('Expected to raise "%s" but raised nothing' % (excClass.__name__))
        except excClass:
            return
        except:
            e = sys.exc_info()[1]
            raise self.failureException('Expected to raise "%s", actually raised "%s"' % (excClass.__name__, e.__class__.__name__))

    def test_passing(self):
        self.alternateAssertRaises(RealException, function_under_test)

    def test_failing(self):
        self.alternateAssertRaises(OtherException, function_under_test)
    
    def test_also_failing(self):
        self.alternateAssertRaises(RealException, other_function)
