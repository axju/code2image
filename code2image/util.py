from PIL import ImageDraw


def rounded_rectangle(draw: ImageDraw, xy, r, fill=None, outline=None):
    draw.rectangle(
        [(xy[0][0], xy[0][1] + r), (xy[1][0], xy[1][1] - r)],
        fill=fill, outline=outline
    )
    draw.rectangle(
        [(xy[0][0] + r, xy[0][1]), (xy[1][0] - r, xy[1][1])],
        fill=fill, outline=outline
    )
    draw.pieslice(
        [xy[0], (xy[0][0] + r * 2, xy[0][1] + r * 2)],
        180, 270, fill=fill, outline=outline
    )
    draw.pieslice(
        [(xy[1][0] - r * 2, xy[1][1] - r * 2), xy[1]],
        0, 90, fill=fill, outline=outline
    )
    draw.pieslice(
        [(xy[0][0], xy[1][1] - r * 2), (xy[0][0] + r * 2, xy[1][1])],
        90, 180, fill=fill, outline=outline
    )
    draw.pieslice(
        [(xy[1][0] - r * 2, xy[0][1]), (xy[1][0], xy[0][1] + r * 2)],
        270, 360, fill=fill, outline=outline
    )
