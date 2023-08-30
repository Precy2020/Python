class Tv:
    def __init__(self):
        self.channel = 0
        self.volume = 0
        self.on = False

    def turn_on(self):
        return True

    def turn_off(self):
        return False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if channel > 0 or channel < 100:
            return self.channel

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        if volume > 0 or volume < 100:
            return volume

    def channel_up(self):
        return None

    def channel_down(self):
        return None

    def volume_up(self):
        return None

    def volume_down(self):
        return None
