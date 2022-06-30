from manim import *
 
class CircleFromPointsEx(Scene):
    def construct(self):
        circle=Circle().from_three_points(LEFT,LEFT+UP,UP*2, color=RED)
        dots=VGroup(
            Dot(LEFT),
            Dot(LEFT+UP),
            Dot(UP*2),
        )
        numberplane=NumberPlane()
        tex=Tex("See you soon at REANLEA.com")
        tex1=Tex("by")
        tex2=Tex("Gobinda Chandra")
        grp=VGroup(tex,tex1,tex2).arrange(DOWN)
 
        self.play(
            Create(
                numberplane,
                run_time=3
            )
        )
        self.play(
            Create(
                dots,
                run_time=2
            )
        )
        self.play(
            Create(
                circle,
                run_time=2
            )
        )
       
        self.wait()
        self.play(
            FadeOut(
                numberplane,dots,
                run_time=1
            )
        )
        self.wait()
        self.play(
            Transform(circle,tex),
        )
        self.play(
            Create(tex1),
            Create(tex2),
        )
        self.play(
            Circumscribe(tex),
            run_time=1.5
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
 
 
from manim import*
 
class Anagram(Scene):
    def construct(self):
        src=Tex("Welcome to REANLEA.com")
        trgt=Tex("Here we'll make your Imagination into Reality!")
        self.play(Write(src))
        self.wait()
        self.play(TransformMatchingShapes(src,trgt,path_arc=PI/2))
        self.wait(2)
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])
        self.wait(0.5)
 
        s=Square()
        circ=Circle()
        s.save_state()
        self.play(FadeIn(s),
            run_time=2)
        self.play(s.animate.set_color(PURPLE).set_opacity(0.5).shift(2*LEFT).scale(4))
        self.play(s.animate.shift(5*DOWN).rotate(PI/4),
            run_time=2  )
        self.play(
            Restore(s),
            run_time=4
        )
        def fn(x):
            x.scale(0.5)
            x.shift(UP*3)
            return x
 
        self.play(
            ApplyFunction(fn,s),
            run_time=5
        )
        self.wait()
 
        self.play(
            Transform(s,circ)
        )
   
        def fn(x):
            x.scale(0.5)
            x.shift(2*UP+4*RIGHT)
            x.set_fill(color=GREEN, opacity=0.5)
            return x
        self.play(
            *[FadeOut(mobj) for mobj in self.mobjects],
            ApplyFunction(fn,circ),
            run_time=3
        )    
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])
       
 
 
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)
 
        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")
 
        self.add(eq1)
        self.wait()
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait()
        self.play(*[FadeOut(mobje) for mobje in self.mobjects])
 
 
 
 
        mob=Circle(radius=4,color=TEAL_A)
        self.play(Write(Tex("Join Us Now!"),
            run_time=1.25),
            Broadcast(mob))
        self.wait()
        self.play(*[FadeOut(mobjec) for mobjec in self.mobjects])
 
 
from manim import *
 
class Reanlealogo(Scene):
    def construct(self):
        #plane = ComplexPlane()
        cloud = PointCloudDot(color=RED)
        logo=ImageMobject("reanlea.png").shift(LEFT).scale(0.4)
        #self.play(
         #   Create(plane)
        #)
        self.add(cloud)
        self.wait()
        self.play(
            cloud.animate.apply_complex_function(lambda z: np.exp(z)),
            FadeIn(logo, run_time=2)
        )
        #self.play(FadeOut(plane))
       
       
        #run_time=3)
        self.wait()
        #self.play(*[FadeOut(mob) for mob in self.mobjects])  
 
 
from manim import*
 
class ArcBtwnPts(Scene):
    def construct(self):
        dot1=Dot(color=RED_E).move_to([2,.5,0]).scale(.75)
        dot2=Dot(color=RED_E).move_to([0,2,0]).scale(.75)
        d1_tx=Tex("(2,0.5,0)").next_to(dot1, RIGHT).set_color(GREEN_D).scale(.3)
        d2_tx=Tex("(0,2,0)").next_to(dot2,UP).set_color(GREEN_D).scale(0.3)
        arc1=ArcBetweenPoints(start=2*RIGHT+.5*UP,end=2*UP,radius=PI/2, stroke_color=YELLOW)
        self.play(
            Create(dot1),
            Create(dot2),
            Create(d1_tx),
            Create(d2_tx)
        )
        self.play(
            Create(arc1)
        )
       
 
from manim import*
class PointAtAngleEx(Scene):
    def construct(self):
        circle=Circle(radius=2)
        p1=circle.point_at_angle(PI/2)
        p2=circle.point_at_angle(3*PI/2)
 
        s1=Square(side_length=0.25).move_to(p1)
        s2=Square(side_length=0.25).move_to(p2)
 
        arc=ArcBetweenPoints(start=p1,end=p2,radius=4)
 
        self.play(
            Create(circle),
            Create(s1),
            Create(s2)
        )      
 
        self.play(
            Create(arc)
        )
 
 
from manim import*
 
class CircleSurround(Scene):
    def construct(self):
 
        tri1=Triangle()
        cir1=Circle().surround(tri1)
        grp1=VGroup(tri1,cir1)
 
        lin1=Line()
        cir2=Circle().surround(lin1,buffer_factor=2)
        grp2=VGroup(lin1,cir2)
 
        sq1=Square()
        cir3=Circle().surround(sq1,buffer_factor=.5)
        grp3=VGroup(sq1,cir3)
 
        grp=VGroup(grp1,grp2,grp3).arrange(buff=1)
 
        self.play(
            Create(grp),
            run_time=6
        )
 
 
from manim import*
 
class BezierSplineEx(Scene):
    def construct(self):
 
        p1=np.array([-3,1,0])
        d1=Dot(point=p1).set_color(BLUE)
        p1b=p1+[1,0,0]
        l1=Line(p1b,p1)
 
        p2=np.array([3,-1,0])
        d2=Dot(point=p2).set_color(ORANGE)
        p2b=p2-[1,0,0]
        l2=Line(p2,p2b)
 
        bezier=CubicBezier(p1b,p1b+3*RIGHT,p2b-3*RIGHT,p2b)
 
        tex=Tex("REANLEA.com")
        grp0=VGroup(d1,d2,l1,l2,bezier)
        grp1=VGroup(grp0,tex).arrange(DOWN)
 
        self.play(
            Create(grp0, run_time=4)
        )
        self.play(
            Create(tex)
        )
        self.wait()
 
 
from manim import*
 
class DifferenceEx(Scene):
    def construct(self):
        sq=Square(color=RED,fill_opacity=1)
        cr=Circle(color=BLUE,fill_opacity=1)
        dot=Dot(color=YELLOW).move_to([-2,0,0])
        sq.move_to([-2,0,0])
        cr.move_to([-1.3,.7,0])
        un=Difference(sq,cr,color=GREEN,fill_opacity=1)
        un.move_to([2,0,0])
        self.play(
            Create(dot),
            Create(sq),
            Create(cr),
            Create(un)
        )
 
 
from manim import*
 
class RightArcAngleEx(Scene):
    def construct(self):
 
        line2=Line(DOWN,UP)
        line1=Line(LEFT,RIGHT)
 
        rightarcangles=[
            Angle(line1,line2,quadrant=(1,1),dot=True),
            Angle(line2,line1,quadrant=(-1,1),color=RED,dot=True,dot_color=RED_E),
            Angle(line1,line2,quadrant=(-1,1),color=GREEN,dot=True,dot_color=GREEN_E,radius=.4,stroke_width=8,stroke_color=YELLOW),
            Angle(line1,line2,quadrant=(1,-1),color=BLUE,dot=True,dot_color=BLUE_E,radius=.6,stroke_width=2,stroke_color=YELLOW,other_angle=True),
        ]
 
        plots=VGroup()
 
        for angle in rightarcangles:
            plot=VGroup(line1.copy(),line2.copy(),angle)
            plots.add(plot)
        plots.arrange(buff=1.5)
        self.play(
            Create(plots)
        )
        self.wait(2)
 
 
from manim import*
 
class ArcAngleEx(Scene):
    def construct(self):
 
        line1=Line(LEFT+(1/3)*UP,RIGHT+(1/3)*DOWN)
        line2=Line(DOWN+(1/3)*RIGHT,UP+(1/3)*LEFT)
 
        arcangles=[
            Angle(line1,line2,quadrant=(1,1),color=RED),
            Angle(line2,line1,quadrant=(-1,1),color=BLUE),
            Angle(line2,line1,quadrant=(1,-1),color=YELLOW),
            Angle(line1,line2,quadrant=(-1,-1),color=GREEN),
        ]
 
        plots1=VGroup()
        for angle in arcangles:
            plot1=VGroup(line1.copy(),line2.copy(), angle)
            plots1.add(plot1)
        plots1.arrange(buff=1.5)
 
        arcangles1=[
            Angle(line1,line2,quadrant=(1,1),color=RED,other_angle=True),
            Angle(line2,line1,quadrant=(-1,1),color=BLUE,other_angle=True),
            Angle(line2,line1,quadrant=(1,-1),color=YELLOW,other_angle=True),
            Angle(line1,line2,quadrant=(-1,-1),color=GREEN,other_angle=True),
        ]
 
        plots2=VGroup()
        for angle in arcangles1:
            plot2=VGroup(line1.copy(),line2.copy(), angle)
            plots2.add(plot2)
        plots2.arrange(buff=1.5)
 
        plots=VGroup(plots1,plots2).arrange(DOWN)
 
        self.play(
            Create(plots),
            run_time=4
        )
        self.wait(3)
           
 
from manim import*
 
class FilledAngleEx(Scene):
    def construct(self):
 
        line1=Line(ORIGIN,RIGHT+2*UP,color=GREEN)
        line2=(line1.copy().rotate(-20*DEGREES,about_point=ORIGIN))
 
        norm=line1.get_length()
        a1=Angle(line1,line2,other_angle=True, radius=norm-0.5).set_color(GREEN)
        a2=Angle(line1,line2,radius=norm,other_angle=True).set_color(GREEN)
        q1=a1.points
        q2=a2.reverse_direction().points
        mfil=VMobject().set_color(ORANGE)
        pts=np.concatenate([q1,q2,q1[0].reshape(1,3)])
        mfil.set_points_as_corners(pts)
        mfil.set_fill(GREEN,opacity=1)
        self.play(
            Create(line1),
            Create(line2),
            Create(a1),
            Create(a2),
            Create(mfil),
            run_time=3
        )
        self.wait()
 
from manim import*
class AngleFromThreePointsEx(Scene):
    def construct(self):
        p1=Dot(point=UP,radius=0.03)
        p2=Dot(point=ORIGIN,radius=0.06).set_color(GREEN)
        p3=Dot(point=LEFT,radius=0.03)
        p4=Dot(point=UP+LEFT,radius=0.03).set_color(RED)
        p5=Dot(point=RIGHT,radius=0.03).set_color(RED)
        pts=VGroup(p1,p2,p3,p4,p5)
        angle1=Angle.from_three_points(UP,ORIGIN,LEFT)
        angle2=Angle.from_three_points(UP+LEFT,ORIGIN,RIGHT, radius=0.8,color=RED,other_angle=True, quadrant=(-1,1))
        self.play(
            Create(pts)
        )
        self.play(
            Create(angle1)
        )        
        self.play(
            Create(angle2)
        )
        self.wait(3)
 
 
from manim import*
class GetValueEx(Scene):
    def construct(self):
        line1=Line(LEFT+(1/3)*UP,RIGHT+(1/3)*DOWN)
        line2=Line(DOWN+(1/3)*RIGHT,UP+(1/3)*LEFT)
 
        angle=Angle(line1,line2,radius=0.4).set_color(RED)
        value=DecimalNumber(angle.get_value(degrees=True),unit="^{\circ}").set_color(GREEN)
 
        value.next_to(angle,UR)
        mob=VGroup(line1,line2,angle,value)
        tex=Tex("Welcome to REANLEA.com")
        self.play(
            Create(line1)
        )
        self.play(
            Create(line2)
        )
        self.play(
            Create(angle)
        )
        self.play(
            Create(value)
        )
        self.wait()
        self.play(
            Transform(mob,tex)
        )
        self.wait()
