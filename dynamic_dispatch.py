from functools import singledispatch


class Shape:
    pass


class Triangle(Shape):
    def __init__(self):
        self.shape = 'triangle'


class SubTriangle(Triangle):
    def __init__(self):
        self.shape = 'SUB triangle'


class Square():
    def __init__(self):
        self.shape = 'sqare'


@singledispatch
def draw(shape):
    raise TypeError(f"I can't draw this shape {shape}")


@draw.register(Triangle)
def _(shape):
    print(f' drawing {shape.shape}')


if __name__ == '__main__':
    draw(Triangle())
    draw(SubTriangle())
    draw(Square())  # this will use default handling ( in this case , throw TypeError )
