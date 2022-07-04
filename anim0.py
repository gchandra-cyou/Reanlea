from tkinter import font
from turtle import bgcolor
from manim import *
from numpy import array
 
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

from manim import*
from manim.mobject.geometry.tips import ArrowSquareTip

class ArrowEx(Scene):
    def construct(self):

        arrow1=Arrow(start=RIGHT,end=LEFT,color=GOLD)
        arrow2=Arrow(start=RIGHT,end=LEFT,color=GOLD,tip_shape=ArrowSquareTip).shift(DOWN)
        g1=VGroup(arrow1,arrow2)

        arrow3=Arrow(start=LEFT,end=RIGHT)
        arrow4=Arrow(start=RIGHT,end=LEFT,buff=.7).next_to(arrow3,UP)
        sq=Square(color=MAROON_C)
        g2=VGroup(arrow3,arrow4,sq)

        arrow5=Arrow(start=ORIGIN,end=config.top).shift(2*LEFT)
        arrow6=Arrow(start=config.top+DOWN,end=config.top).shift(LEFT)
        g3=VGroup(arrow5,arrow6)

        grp=VGroup(g1,g2,g3).arrange(buff=2)

        self.play(
            Create(grp),
            run_time=4
        )


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

        DRgrp=VGroup()
        DRgrp+=Arrow(start=LEFT,end=RIGHT,color=BLUE,tip_shape=ArrowSquareTip)
        DRgrp+=Arrow(start=LEFT,end=RIGHT,color=BLUE,tip_shape=ArrowSquareFilledTip)
        DRgrp+=Arrow(start=LEFT,end=RIGHT,color=RED,tip_shape=ArrowCircleTip)
        DRgrp+=Arrow(start=LEFT,end=RIGHT,color=RED,tip_shape=ArrowCircleFilledTip)
        DRgrp.arrange(DOWN)
        DRgrp.move_to(4*RIGHT+2*DOWN)

        grp=VGroup(lgrp,mgrp,URgrp,DRgrp)

        self.play(
            Create(grp),
            run_time=6
        )
        self.wait()


from manim import*
from manim_fonts import*
class ArrowTest0(Scene):
    def construct(self):
        arrow=Arrow(np.array([-1,-1,0]),np.array([1,1,0])).set_color_by_gradient(RED,BLUE)
        with RegisterFont("Comfortaa") as fonts:
            tex=Text("REANLEA.com",font=fonts[0]).next_to(arrow,DOWN)
        grp=VGroup(arrow,tex)    
        self.play(
            Create(grp),
            run_time=3
        ) 
        self.wait()   


from manim import*
from manim_fonts import*
class GradientTest(Scene):
    def construct(self):
        #dots
        dots = VGroup(*[Dot(radius=0.15) for i in range(20)])
        dots.arrange(RIGHT)
        dots.set_color_by_gradient(PINK, BLUE, YELLOW)

        #text

        with RegisterFont("Comfortaa") as fontz:
            a=Text("de ARTh.studio", font=fontz[1])
            a.set_color_by_gradient(YELLOW,GREEN,BLUE,RED)

        with RegisterFont("Tiro Bangla") as fonts:
            text = Text("শুভ রথযাত্রা",font=fonts[0])
            text.set_color_by_gradient(RED,BLUE,YELLOW)
            text.next_to(dots, UP)

        

        #play
        self.add_sound("piano.mp3")
        self.play(
            FadeIn(dots),
            Write(text),
            run_time=2,
        )
        self.wait(2)

        self.play(
            Transform(text,a),
            FadeOut(dots),
            run_time=2
        )
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        


from manim import*
class ArrowTest(Scene):
    def construct(self):
        a=[-1,-1,0]
        b=[1,1,0]
        arrow=Arrow(start=a,end=b,buff=1)
        arrow2=VMobject.scale(arrow,2)
        self.play(
            Create(arrow2)
        )
        self.play( 
            Rotate(arrow2,PI/4)
        )    

from manim import*
class ArrowTest1(Scene):
    def construct(self):
        a=[-1,-1,0]
        b=[1,1,0]
        arrow=Arrow(start=a,end=b,buff=1)
        arrow0=Arrow(start=a,end=b,buff=1)
        arrow01=arrow0.scale(1)            #arrow tip length is equal to scaled arrow tip length
        arrow1=Arrow(start=a,end=b,buff=1)
        arrow11=arrow1.scale(2)            #arrow tip length is equal to scaled arrow tip length
        arrow2=Arrow(start=a,end=b,buff=1)
        arrow21=VMobject.scale(arrow2,2)   #arrow tip length is not equal to scaled arrow tip length

        grp=VGroup(arrow,arrow0,arrow01,arrow1,arrow11,arrow2,arrow21).arrange(buff=1)

        self.play(
            Create(grp),
            run_time=5
        )
        self.wait()      


from manim import*
class DashedLineEx(Scene):
    def construct(self):
        dl1=DashedLine(config.left_side,config.right_side,dash_length=2.0).shift(UP*2)
        dl1.set_color_by_gradient(RED,BLUE,GREEN,YELLOW)
        dl2=DashedLine(config.left_side,config.right_side)  
        dl2.set_color_by_gradient(GREEN,MAROON,BLUE,RED)        
        dl3=DashedLine(config.left_side,config.right_side,dashed_ratio=0.1).shift(2*DOWN)
        dl3.set_color_by_gradient(BLUE_D,RED_D,GREEN_D,GOLD_C)

        grp=VGroup(dl1,dl2,dl3)
        self.play(
            Create(dl1,run_time=2)
        )
        self.play(
            Create(dl2,run_time=4),
        )
        self.play(
            Create(dl3,run_time=3)
        )
        self.wait()


from manim import*
from manim.mobject.geometry.tips import ArrowCircleFilledTip
class DoubleArrowEx(Scene):
    def construct(self):
        circle=Circle(radius=2.0)
        darrow1=DoubleArrow(start=circle.get_left(),end=circle.get_right())
        darrow2=DoubleArrow(tip_shape_end=ArrowCircleFilledTip,tip_shape_start=ArrowCircleFilledTip)
        grp=VGroup(VGroup(circle,darrow1),darrow2).arrange(UP,buff=1)

        self.play(
            Create(grp),
            run_time=5
        )
        self.wait()


from manim import*
class DoubleArrowEx2(Scene):
    def construct(self):
        box=Square()
        p1=box.get_left()
        p2=box.get_right()
        d1=DoubleArrow(p1,p2,buff=0)   
        d2=DoubleArrow(p1,p2,buff=0,tip_length=0.2,color=YELLOW)
        d3=DoubleArrow(p1,p2,buff=0,tip_length=0.4,color=BLUE)    
        grp=VGroup(d1,d2,d3).arrange(DOWN)
        self.play(
            Create(box)
        )
        self.play(
            Create(grp)
        )
        self.wait()    


from manim import*

class DashedLineEx(Scene):
    def construct(self):
        d0=DashedLine(config.left_side,config.right_side,dashed_ratio=0.2)
        d0.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        d1=DashedLine(config.left_side,config.right_side,dash_length=1.0)
        d1.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        d2=DashedLine(config.left_side,config.right_side)
        d2.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        d3=DashedLine(config.left_side,config.right_side,dashed_ratio=0.2)
        d3.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)

        grp=VGroup(d0,d1,d2,d3).arrange(DOWN)

        self.play(
            Create(grp),
            run_time=3
        )
        self.wait()


from manim import*

class ElbowEx(Scene):
    def construct(self):
        el1=Elbow()
        el2=Elbow(width=2.0)
        el3=Elbow(width=2.0,angle=5*PI/4)
        grp=VGroup(el1,el2,el3).arrange(buff=1)
        self.play(
            Create(grp)
        )
        self.wait()

from manim import*

class LineEx(Scene):
    def construct(self):
        d=VGroup()
        for i in range(0,10):
            d.add(Dot())
        d.arrange_in_grid(buff=1)
        d.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        self.play(
            Create(d)
        )       
        l=Line(d[0],d[1])
        l.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        self.play(
            Create(l)
        )
        self.wait()
        l.put_start_and_end_on(d[1].get_center(),d[2].get_center())
        l.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        self.play(
            Create(l)
        )
        self.wait()
        l.put_start_and_end_on(d[2].get_center(),d[8].get_center())
        l.set_color_by_gradient(RED,BLUE,GREEN,MAROON,GOLD)
        self.play(
            Create(l)
        )
        self.wait()


from manim import*    

class RightAngleEx(Scene):
    def construct(self):
        line1=Line(LEFT,RIGHT)
        line2=Line(DOWN,UP)
        x=[
            RightAngle(line1,line2),
            RightAngle(line1,line2,quadrant=(-1,1),color=RED),
            RightAngle(line1,line2,quadrant=(-1,-1),stroke_width=8,length=0.5),
            RightAngle(line1,line2,quadrant=(1,-1),color=YELLOW,length=0.7)
        ]
        plots=VGroup()
        for y in x:
            plot=VGroup(line1.copy(),line2.copy(),y)
            plots.add(plot)
        plots.arrange(buff=1)
        self.play(
            Create(plots),
            run_time=5
        )    
        self.wait()


from manim import*
class TangentLineEx(Scene):
    def construct(self):
        circle=Circle()
        l1=TangentLine(circle,alpha=0,length=4,color=BLUE_D)
        l2=TangentLine(circle,alpha=0.25,length=4,color=GREEN)
        l3=TangentLine(circle,alpha=0.5,length=4,color=RED)
        l4=TangentLine(circle,alpha=0.75,length=4,color=YELLOW)
        l5=TangentLine
        self.play(
            Create(circle)
        )
        self.play(
            Create(l1)
        )
        self.play(
            Create(l2)
        )
        self.play(
            Create(l3)
        )
        self.play(
            Create(l4)
        )
        self.wait()


from manim import*
class TangentLineEx2(Scene):
    def construct(self):
        circle=Circle(radius=2)
        grp=VGroup()
        for i in np.arange(0,1,0.15):
            grp+=TangentLine(circle,alpha=i,length=2.25,color=GREEN_C)
        grpc=VGroup(circle,grp)
        self.play(
            Create(grpc),
            run_time=5
        )  
        self.wait()  

from manim import*
class VectorEx(Scene):
    def construct(self):
        plane=NumberPlane()

        v1=Vector([1,2])
        v2=Vector([-3,-2])
        vl1=v1.coordinate_label()
        vl2=v2.coordinate_label(color=BLUE)

        grp=VGroup(plane,v1,v2,vl1,vl2)
        self.play(
            Create(grp),
            run_time=7
        )
        self.wait()


#Cutout Example

from manim import*
class CutoutEx(Scene):
    def construct(self):
        s1=Square().scale(2.5)
        #s2=Triangle().shift(DOWN+RIGHT).scale(.5)
        #s4=Square().shift(LEFT+DOWN).scale(.5)
        #s8=RegularPolygon(5).shift(UP+LEFT).scale(0.5)
        s3=RegularPolygon(6).shift(UP + LEFT).scale(0.5)
        #s5=RegularPolygon(6).shift(LEFT+DOWN).scale(.5)
        s6=RegularPolygon(3).shift(DOWN+LEFT).scale(0.5)
        #s7=RegularPolygon(7)
        c=Cutout(s1,s6,s3,fill_opacity=1,color=
        BLUE,stroke_color=RED)
        self.play(
            Write(c),
            run_time=6
        )        
        self.wait()


from manim import *

class PolygonEx(Scene):
    def construct(self):
       x=Polygon([-5,1.5,0],[-2,1.5,0],[-3.5,-2,0])
       position=[
        [4,1,0],
        [5,2,0],
        [-3,4,0],
        [7,1,0],
        [-5,9,0],
        [2,-4,0]
       ]   
       y=Polygon(*position,color=PURPLE)
       tex=Tex("REANLEA.com").next_to(y,RIGHT).scale(2)
       grp=VGroup(x,y,tex)
       grp=grp.scale(.2).shift(2.4*DOWN,3.4*LEFT)
       self.play(
        Create(y),
        run_time=3
       )
       self.wait()
       self.play(
        Rotate(y,-PI/2)
       )
       self.play(
        Create(tex)
       )
       self.wait(2)
       self.play(*[FadeOut(mob) for mob in self.mobjects])


from manim import*
import numpy as np
class PolygramEx(Scene):
    def construct(self):
        hexa=Polygram(
            [[0,2,0],[-np.sqrt(3),-1,0],[np.sqrt(3),-1,0]],
            [[-np.sqrt(3),1,0],[0,-2,0],[np.sqrt(3),1,0]],
        ).set_color(PURPLE)      
        dot=Dot(color=PURE_GREEN)
        tex=Tex("REANLEA.com").set_color(PURE_GREEN)
        grp=VGroup(hexa,tex).arrange(DOWN)
        hexa2=hexa.copy().round_corners(radius=0.25) #Rounds off the corners of the Polygram.

        self.wait()
        self.play(
            Create(hexa,run_time=3),
            Create(tex,run_time=3)
        )
        self.play(
            Transform(hexa,hexa2),
            run_time=2.5
        )
        self.play(
            MoveAlongPath(dot,hexa2),run_time=5,rate_func=linear
        )
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


from manim import*
class RectEx(Scene):
    def construct(self):
        rect1=Rectangle(width=4.0,height=2.0,grid_xstep=1.0,grid_ystep=0.5).set_color_by_gradient(BLUE,PURE_RED,PURE_GREEN,PURE_BLUE)
        rect2=Rectangle(width=1.0,height=4.0)
        grp=VGroup(rect1,rect2).arrange(buff=1)
        self.play(
            Create(grp),
            run_time=3
        )        
        self.wait()


from manim import*
class RegularPolygonEx(Scene):
    def construct(self):
        p1=RegularPolygon(n=6)
        p2=RegularPolygon(n=6,start_angle=30*DEGREES,color=PURE_GREEN)
        p3=RegularPolygon(n=10,color=PURE_RED)  
        grp=VGroup(p1,p2,p3).arrange(buff=1)
        self.play(
            Create(grp),
            run_time=3
        )      
        self.wait()


from manim import*
class RegularPolygramEx(Scene):
    def construct(self):
        p1=RegularPolygram(3,radius=1,color=PURE_GREEN)
        p2=RegularPolygram(4,radius=1,color=PURE_GREEN)
        p3=RegularPolygram(5,radius=1,color=PURE_GREEN)
        p4=RegularPolygram(6,radius=1,color=PURE_GREEN)
        p5=RegularPolygram(7,radius=1,color=PURE_GREEN)
        p6=RegularPolygram(8,radius=1,color=PURE_GREEN)
        p7=RegularPolygram(9,radius=1,color=PURE_GREEN)
        p8=RegularPolygram(10,radius=1,color=PURE_GREEN)
        p9=RegularPolygram(11,radius=1,color=PURE_GREEN)
        p10=RegularPolygram(12,radius=1,color=PURE_GREEN)
        p11=RegularPolygram(13,radius=1,color=PURE_GREEN)
        p12=RegularPolygram(14,radius=1,color=PURE_GREEN)
        p13=RegularPolygram(15,radius=1,color=PURE_GREEN)
        p14=RegularPolygram(16,radius=1,color=PURE_GREEN)
        p15=RegularPolygram(17,radius=1,color=PURE_GREEN)
        grp1=VGroup(p1,p2,p3,p4,p5).arrange(buff=1)
        grp2=VGroup(p6,p7,p8,p9,p10).arrange(buff=1)
        grp3=VGroup(p11,p12,p13,p14,p15).arrange(buff=1)
        grp=VGroup(grp1,grp2,grp3).arrange(DOWN)
        self.play(
            Create(grp),
            run_time=6
        )        
        self.wait()


from manim import*
class xy(Scene):
    def construct(self):
        p5=RegularPolygram(5, radius=2,color=PURE_GREEN)
        p6=RegularPolygram(6,radius=2,color=PURE_GREEN)
        p5c=p5.copy().round_corners(radius=0.25)
        p6c=p6.copy().round_corners(radius=0.25)  
        grp=VGroup(p5,p6).arrange(buff=1)
        grp1=VGroup(p5c,p6c).arrange(buff=3)
        self.play(
            Create(grp),
            run_time=2
        )
        self.play(
            Transform(grp,grp1)
        )     
        self.wait()


from manim import*
class StarEx(Scene):
    def construct(self):
        p=RegularPolygram(5,radius=1.5,color=PURE_GREEN)
        s=Star(5,outer_radius=1.5,color=PURPLE)
        s1=Star(7,outer_radius=1.5,density=2,color=PURE_RED)
        s2=Star(7,outer_radius=1.5,density=3,color=PURE_BLUE)
        grp1=VGroup(p,s)
        grp2=VGroup(s1,s2).arrange(buff=1)
        grp=VGroup(grp1,grp2).arrange(buff=1)
        
        self.play(
            Create(grp),
            run_time=6
        )    
        self.wait()    



#Shape Matchers (manim.mobject.geometry.shape\_matchers)

from manim import*
class BackgroundRectangleEx(Scene):
    def construct(self):
        circle=Circle().shift(LEFT)
        triangle=Triangle().shift(2*RIGHT)
        circle.set_stroke(color=GREEN,width=20)
        triangle.set_fill(PURPLE,opacity=0.5)
        b1=BackgroundRectangle(circle,color=WHITE,fill_opacity=.5)
        b2=BackgroundRectangle(triangle,color=WHITE,fill_opacity=0.5)
        grp=VGroup(circle,triangle,b1,b2)
        self.play(
            Create(grp)
        )
        self.play(
            Rotate(b1,PI/2)
        )
        self.play(
            Rotate(b2,PI/2)
        )
        self.wait()


from manim import*
class CrossEx(Scene):
    def construct(self):
        cross=Cross().set_color(PURE_RED)
        self.play(
            Create(cross),
            run_time=2
        )
        self.wait()


from manim import*
class UnderlineEx(Scene):
    def construct(self):
        man=Tex("Gobinda Chandra").set_color(PURPLE)
        ul=Underline(man).set_color(PURE_GREEN)
        grp=VGroup(man,ul)
        self.play(
            Create(grp),
            run_time=2
        )       
        self.wait() 


from manim import*
class Grapg1Ex(Scene):
    def construct(self):
        vertices=[1,2,3,4]
        edges=[(1,2),(2,3),(3,4),(1,3),(1,4)]
        g=Graph(vertices,edges, vertex_config={"fill_color":PURE_RED},
        edge_config={
            (1,2):{"stroke_color":PURE_GREEN},
            (2,3):{"stroke_color":PURPLE_B},
            (3,4):{"stroke_color":PURE_BLUE},
            (1,3):{"stroke_color":BLUE_C},
            (1,4):{"stroke_color":YELLOW},
        })  
        self.play(
            Create(g),
            run_time=2
        )   
        self.wait()
        self.play(
            g[1].animate.move_to([1,1,0]),
            g[2].animate.move_to([-1,1,0]),
            g[3].animate.move_to([1,-1,0]),
            g[4].animate.move_to([-1,-1,0]),
        )
        self.wait()


from manim import*
class GraphAutoPosition(Scene):
    def construct(self):
        vertices=[1,2,3,4,5,6,7,8]
        edges=[(1,2),(1,8),(1,7),(2,6),(2,5),(2,4),(3,6),(3,8),(4,5),(4,7),(5,8)] 
        auto=["spring","circular","planar","random","shell","spectral","spiral",]       