# Changing FONTS : import any font from Google
#some of my fav fonts: Cinzel,Kalam,Prata,Kaushan Script,Cormorant,Poiret One,Merienda,Julius Sans One,Merienda One,Cinzel Decorative,Marcellus SC,Contrail One,Thasadith,Spectral SC,Dongle,Cormorant SC,Comfortaa
from manim import *
config.background_color='#000033'
from manim_fonts import *
class Ex(Scene):
    def construct(self):

        #text
        with RegisterFont("The Nautigal") as fonts:
            a=Text("Gobinda Chandra",font=fonts[0])
            a.set_color_by_gradient(YELLOW,GREEN,BLUE,RED) #set color by gradient example

        #dots
        dots=VGroup(*[Dot(radius=0.05) for i in range(10)])
        dots.arrange(RIGHT)
        dots.next_to(a,DOWN)
        dots.set_color_by_gradient(PINK, BLUE, YELLOW)
        
        #add sound
        self.add_sound("piano.mp3")

        #play
        self.play(
            Write(a,run_time=4),
            Create(dots,run_time=4)
        )
        self.wait(4)

        #Fade out
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        


#neglecting repeat code for Range 

from manim import*
class ArrowEXl(Scene):
    def construct(self):

        lgrp=VGroup()
        for buf in np.arange(0,2.2,.45):
            lgrp += Arrow(buff=buf, start=2*LEFT,end=2*RIGHT)
            lgrp.arrange(DOWN)
            lgrp.move_to(4*LEFT)

        mgrp=VGroup()
        for i in np.arange(0,5,.5):
            mgrp+=Arrow(max_stroke_width_to_length_ratio=i)
            mgrp.arrange(DOWN)

        URgrp=VGroup()
        for i in np.arange(0,.3,.1):
            URgrp+=Arrow(max_tip_length_to_length_ratio=i)
            URgrp.arrange(DOWN)
            URgrp.move_to(4*RIGHT+2*UP)

        grp=VGroup(lgrp,mgrp,URgrp)

        self.play(
            Create(grp),
            run_time=6
        )
        self.wait()    