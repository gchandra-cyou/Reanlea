# Changing FONTS : import any font from Google
#some of my fav fonts: Cinzel,Kalam,Prata,Kaushan Script,Cormorant,Poiret One,Merienda,Julius Sans One,Merienda One,Cinzel Decorative,Marcellus SC,Contrail One,Thasadith,Spectral SC,Dongle,Cormorant SC,Comfortaa
from manim import *
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
        