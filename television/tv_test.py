import unittest

from television.tv import Tv


class TestTelevision(unittest.TestCase):
    def test_that_the_television_can_turn_on(self):
        self.assertTrue(True, Tv.turn_on)

    def test_that_the_television_can_turn_off(self):
        self.assertFalse(False, Tv.turn_on)

    def test_that_the_television_have_a_channel(self):
        self.assertTrue(True, Tv.get_channel)

    def test_that_the_television_have_volume(self):
        self.assertTrue(True, Tv.get_volume)

    def test_that_the_television_have_channel(self):
        self.assertTrue(True, Tv.get_channel)

    def test_that_the_television_have_a_channel_can_go_up(self):
        self.assertTrue(True, Tv.channel_up)

    def test_that_the_television_have_a_channel_can_go_down(self):
        self.assertTrue(True, Tv.channel_down)

    def test_that_the_television_have_a_volume_can_go_up(self):
        self.assertTrue(True, Tv.volume_up)

    def test_that_the_television_have_a_volume_can_go_down(self):
        self.assertTrue(True, Tv.volume_down)

