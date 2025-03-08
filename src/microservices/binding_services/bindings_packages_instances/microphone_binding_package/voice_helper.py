import numpy
from numpy import sqrt, mean


class VoiceHelper:
    @staticmethod
    def get_voice_volume(voice: numpy.ndarray[numpy.float32]):
        volume = sqrt(mean(voice ** 2))
        return volume
