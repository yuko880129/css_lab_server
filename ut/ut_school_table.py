import unittest
from school_time_table_system import SchoolTimeTableSystem

class SchoolTimeTableSystemCase(unittest.TestCase):
    def test_SchoolTimeTableSystem_member_class_getter(self):
        schoolTimeTableSystem = SchoolTimeTableSystem()
        expected = [
            ["檔案與儲存系統", ["2,5", "2,6", "2,7"]],
            ["機器學習", ["2,8", "3,8", "3,9"]],
            ["物件導向分析與設計", ["4,3", "4,4", "4,6"]],
            ["專題討論", ["4,7", "4,8"]],
            ["字體設計與文字編碼", ["5,5", "5,6", "5,7"]],
        ]
        result = schoolTimeTableSystem.getMemberClassTimeSchedual('1111', '子瑩')
        self.assertEqual(expected, result)
    def test_SchoolTimeTableSystem_all_member_getter(self):
        schoolTimeTableSystem = SchoolTimeTableSystem()
        expected = ["子瑩", "成彥", "晨睿"]
        result = schoolTimeTableSystem.getAllMembers('1111')
        self.assertEqual(expected, result)