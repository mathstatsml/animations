# Heavily inspired by Theorem of Beethoven - https://www.youtube.com/watch?v=OsZz2CQJHLQ

from math import e
from manim import *
from colour import Color

config.frame_rate = 60
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080

class SpiralPolygon(VGroup):
    def __init__(self, p:RegularPolygon, n, prop, **kwargs):
        super().__init__(**kwargs)
        vertices = p.get_vertices()
        n_vertices = len(vertices)
        lines = [
            Line(vertices[i], vertices[(i+1)%n_vertices]) for i in range(n_vertices)
        ]
        tmp_lines = lines[1:]
        for i in range(n):
            last_line = tmp_lines[-1]
            first_line = tmp_lines[0]
            next_line = Line(
                last_line.get_end(),
                first_line.point_from_proportion(prop),
                stroke_color=Color(hue=i/69, saturation=0.34, luminance=0.34),
                stroke_width=1,
                stroke_opacity=1
            )
            tmp_lines.pop(0)
            tmp_lines.append(next_line)
            self.add(next_line)

class Logo(Scene):
    def construct(self):
        grp = VGroup(*[
            RegularPolygon(6)
        ]).set_stroke(color=Color(hue=0, saturation=0.34, luminance=0.34), width=1)

        s_grp = VGroup(*[
            SpiralPolygon(_p, 69, prop=0.10134)
            for _p in grp
        ])

        self.play(AnimationGroup(*[Create(polygon, rate_func=rate_functions.smooth) for polygon in grp], lag_ratio=0.2), rate_func=rate_functions.linear, run_time=1)

        self.play(AnimationGroup(*[Create(line, rate_func=rate_functions.smooth) for line in s_grp], lag_ratio=0.1), rate_func=rate_functions.ease_out_cubic, run_time=3)

        self.wait()