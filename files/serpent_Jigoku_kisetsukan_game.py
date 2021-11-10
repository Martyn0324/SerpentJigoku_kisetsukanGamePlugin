from serpent.game import Game

from .api.api import Jigoku_kisetsukanAPI

from serpent.utilities import Singleton

import time


class SerpentJigoku_kisetsukanGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Jigoku Kisetsukan: Sense of the seasons v.1.09"

        kwargs["app_id"] = "368950"
        kwargs["app_args"] = None
        

        super().__init__(**kwargs)

        self.api_class = Jigoku_kisetsukanAPI
        self.api_instance = None
        
        self.frame_transformation_pipeline_string = "RESIZE:100x100|GRAYSCALE"
        

    @property
    def screen_regions(self):
        
        # Window mode regions
        regions = {
            "Lifes": (550, 140, 575, 197), #Y, X, Y, X
            "Power": (605, 140, 620, 197),
            "Aura": (650, 140, 675, 197),
            "Multiplier_score": (603, 950, 623, 1013),
            "Score": (653, 875, 670, 1013)
        }

        '''Fullscreen regions
        regions = {
            "Lifes": (849, 400, 904, 498), #Y, X, Y, X
            "Power": (923, 405, 978, 503),
            "Aura": (1001, 400, 1045, 497),
            "Multiplier_score": (933, 1536, 978, 1723),
            "Score": (1008, 1429, 1046, 1723)
        }'''

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
