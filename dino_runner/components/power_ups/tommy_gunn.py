from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import TOMMY_GUNN, GUNN_TYPE

class TommyGunn(PowerUp):
    def __init__(self):
        super().__init__(TOMMY_GUNN, GUNN_TYPE)