import unittest
from meeting_time_table_system import MeetingTimeTableSystem

class MeetingTimeTableSystemCase(unittest.TestCase):
    def test_MeetingTimeTableSystem_meeting_time_setter_getter(self):
        meetingTimeTableSystem = MeetingTimeTableSystem()
        meetingTimeTableSystem.setmeeting_time('1111', '子瑩', ['1', '18:00'])
        meet = {'子瑩':['1', '18:00'], '上澤': ['1', '17:00'], '宇翔': ['2', '11:00'], '如儀': ['2', '12:00'], '宗霖':['2', '16:00'], '晨睿':['3', '11:00'], '華暄':['3', '16:00'], '聖翊':['3', '17:00'], '成彥': ['4', '17:00'], '永誠':['5', '13:00'], '立軒':['5', '14:00'], '振洋':['5', '15:00']}
        expected = list(meet.items())
        result = meetingTimeTableSystem.getmeeting_time('1111')
        self.assertEqual(expected, result)
    def test_MeetingTimeTableSystem_double_time_failure(self):
        meetingTimeTableSystem = MeetingTimeTableSystem()
        expected = "invalid time"
        self.assertEqual(expected, meetingTimeTableSystem.setmeeting_time('1111', '子瑩', ['1', '17:00']))