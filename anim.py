from manim import*

class DashedLineEx(Scene):
    def construct(self):
        d1=DashedLine(config.left_side,config.right_side,dash_length=1.0)
        d1.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        d2=DashedLine(config.left_side,config.right_side)
        d2.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        d3=DashedLine(config.left_side,config.right_side,dashed_ratio=0.2)
        d3.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)

        grp=VGroup(d1,d2,d3).arrange(DOWN)

        self.play(
            Create(grp),
            run_time=3
        )
        self.wait()