# Changing FONTS : import any font from Google
from manim import *
from manim_fonts import *
class Ex(Scene):
    def construct(self):
        with RegisterFont("The Nautigal") as fonts:
            a=Text("Gobinda Chandra",font=fonts[0])
            self.play(
                Write(a,run_time=3)
            )