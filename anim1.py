from manim import*

class DashedLineEx(Scene):
    def construct(self):
        d1=DashedLine(config.left_side,config.right_side,dash_length=2.0)
        d1.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        d2=DashedLine(config.left_side,config.right_side)
        d2.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        d3=DashedLine(config.left_side,config.right_side,dashed_ratio=0.2)
        d3.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)

        self.play(
            Create(d1)
        )