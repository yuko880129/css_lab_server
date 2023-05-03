import unittest
from ut.ut_cleaning_table  import CleaningTimeTableSystemCase

tests = ['test_CleaningTimeTableSystem_member_setter_getter', 'test_CleaningTimeTableSystem_StartD_setter_getter', 'test_CleaningTimeTableSystem_EndD_setter_getter', 'test_CleaningTimeTableSystem_StartD_failure', 'test_CleaningTimeTableSystem_EndD_failure']
suite = unittest.TestSuite(map(CleaningTimeTableSystemCase, tests))
suite.addTest(CleaningTimeTableSystemCase('test_CleaningTimeTableSystem_member_setter_getter'))

unittest.TextTestRunner(verbosity=2).run(suite)

from ut.ut_meeting_table  import MeetingTimeTableSystemCase
tests = ['test_MeetingTimeTableSystem_meeting_time_setter_getter', 'test_MeetingTimeTableSystem_double_time_failure']
suite = unittest.TestSuite(map(MeetingTimeTableSystemCase, tests))

unittest.TextTestRunner(verbosity=2).run(suite)

from ut.ut_school_table  import SchoolTimeTableSystemCase
tests = ['test_SchoolTimeTableSystem_member_class_getter', 'test_SchoolTimeTableSystem_all_member_getter']
suite = unittest.TestSuite(map(SchoolTimeTableSystemCase, tests))

unittest.TextTestRunner(verbosity=2).run(suite)