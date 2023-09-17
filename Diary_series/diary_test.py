from unittest import TestCase

from Diary_series.custom_exception import IncorrectPassword
from Diary_series.diary import Diary


class DiaryTest(TestCase):
    def setUp(self) -> None:
        self.diary: Diary = Diary()

    def test_That_Diary_IsLocked(self):
        self.assertTrue(self.diary.is_locked())

    def test_That_Diary_Can_Be_Unlocked(self):
        self.diary.unlock_diary("1234")
        self.assertFalse(self.diary.is_locked())

    def test_That_Diary_RaisesError_WhenPasswordIsIncorrect(self):
        self.diary.unlock_diary("1237")
        self.assertRaises(IncorrectPassword, self.diary.unlock_diary)

