
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from pygments.styles.monokai import MonokaiStyle
from PIL import Image, ImageDraw, ImageFilter
from io import BytesIO

from code2image.util import rounded_rectangle


class DefaultStyle(MonokaiStyle):
    background_color = '#661A0A'


class Code2ImageBasic(object):

    formatter = None
    lexer = None

    def get_formatter(self):
        if not self.formatter:
            raise AttributeError('You need a "formatter"')
        return self.formatter

    def get_lexer(self):
        if not self.lexer:
            raise AttributeError('You need a "lexer"')
        return self.lexer

    def highlight(self, code):
        lexer = self.get_lexer()
        fm = self.get_formatter()
        return Image.open(BytesIO(highlight(code, lexer(), fm)))


class Code2Image(Code2ImageBasic):

    formatter = ImageFormatter(
        font_name="Liberation Mono", line_pad=10,
        line_numbers=False, style=DefaultStyle, font_size=25)

    lexer = PythonLexer

    def __init__(self, background_color='#661A0A'):
        super(Code2Image, self).__init__()
        self.background_color = background_color

    def get_formatter(self):
        style = DefaultStyle
        style.background_color = self.background_color
        return ImageFormatter(
            font_name="Liberation Mono", line_pad=10,
            line_numbers=False, style=style, font_size=25)


class Code2ImageShadow(Code2Image):

    def __init__(self, **kwargs):
        super(Code2ImageShadow, self).__init__(
            kwargs.get('code_bg', '#661A0A')
        )
        self.img_bg = kwargs.get('img_bg', '#AAAAAA')
        self.shadow_dt = kwargs.get('shadow_dt', 4)
        self.shadow_color = kwargs.get('shadow_color', '#111111')
        self.offset = kwargs.get('offset', 10)
        self.blur = kwargs.get('blur', 20)

    def highlight(self, code):
        img = super(Code2Image, self).highlight(code)
        m = round(max(img.size)*(1+(self.offset*0.01)))

        dt = round(m*self.shadow_dt*0.01)
        blur = round(m*self.blur*0.002)

        box = (
            ((m-img.size[0]*1.03)//2, (m-img.size[1]*1.03)//2),
            ((m+img.size[0]*1.03)//2, (m+img.size[1]*1.03)//2)
        )

        background = Image.new("RGB", (m, m), self.img_bg)
        draw = ImageDraw.Draw(background)
        rounded_rectangle(
            draw, ((box[0][0]+dt, box[0][1]+dt), (box[1][0]+dt, box[1][1]+dt)),
            20, fill=self.shadow_color
        )
        background = background.filter(ImageFilter.GaussianBlur(blur))

        draw = ImageDraw.Draw(background)
        rounded_rectangle(draw, box, 20, fill=self.background_color)

        background.paste(img, ((m - img.size[0]) // 2, (m - img.size[1]) // 2))
        return background
