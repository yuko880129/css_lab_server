import unittest
from cleaning_time_table_system import CleaningTimeTableSystem

class CleaningTimeTableSystemCase(unittest.TestCase):
    def test_CleaningTimeTableSystem_member_setter_getter(self):
        cleaningTimeTableSystem = CleaningTimeTableSystem()
        cleaningTimeTableSystem.setHatarakuMembers('1111', ['上澤', '宇翔', '駿頤'])
        expected = ['上澤', '宇翔', '駿頤']
        result = cleaningTimeTableSystem.getHatarakuMembers('1111')
        self.assertEqual(expected, result)
    def test_CleaningTimeTableSystem_StartD_setter_getter(self):
        cleaningTimeTableSystem = CleaningTimeTableSystem()
        cleaningTimeTableSystem.setsemesterStartD('1111', [4, 5])
        expected = [4, 5]
        result = cleaningTimeTableSystem.getSemesterStartD('1111')
        self.assertEqual(expected, result)
    def test_CleaningTimeTableSystem_EndD_setter_getter(self):
        cleaningTimeTableSystem = CleaningTimeTableSystem()
        cleaningTimeTableSystem.setsemesterEndD('1111', [7, 10])
        expected = [7, 10]
        result = cleaningTimeTableSystem.getSemesterEndD('1111')
        self.assertEqual(expected, result)
    def test_CleaningTimeTableSystem_StartD_failure(self):
        cleaningTimeTableSystem = CleaningTimeTableSystem()
        expected = "invalid month and day"
        self.assertEqual(expected, cleaningTimeTableSystem.setsemesterStartD('1111', [4, 5, 6]))
    def test_CleaningTimeTableSystem_EndD_failure(self):
        cleaningTimeTableSystem = CleaningTimeTableSystem()
        expected = "invalid month and day"
        self.assertEqual(expected, cleaningTimeTableSystem.setsemesterEndD('1111', [5, 6, 7]))
        
# tests = ['test_CleaningTimeTableSystem_member_setter_getter', 'test_CleaningTimeTableSystem_StartD_setter_getter', 'test_CleaningTimeTableSystem_EndD_setter_getter', 'test_CleaningTimeTableSystem_StartD_failure', 'test_CleaningTimeTableSystem_EndD_failure']
# suite = unittest.TestSuite(map(CleaningTimeTableSystemCase, tests))
# suite.addTest(CleaningTimeTableSystemCase('test_CleaningTimeTableSystem_member_setter_getter'))

# unittest.TextTestRunner(verbosity=2).run(suite)