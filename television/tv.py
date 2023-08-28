class Tv:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def turn_on(self):
        return None

    def turn_off(self):
        return None

    @property
    def channel(self):
        return None

    @channel.getter
    def channel(self):
        return self.channel

    @channel.setter
    def channel(self, channel):
        return None

    @property
    def volume(self):
        return None

    @volume.getter
    def volume(self):
        return self.volume

    @volume.setter
    def volume(self, volume):
        return None

    def channel_up(self):
        return None

    def channel_down(self):
        return None

    def volume_up(self):
        return None

    def volume_down(self):
        return None
