
from pygments import highlight
from pygments.lexers import get_lexer_for_filename, PythonLexer
from pygments.formatters import ImageFormatter
from pygments.styles.monokai import MonokaiStyle
from PIL import Image, ImageDraw, ImageFilter
from io import BytesIO

from code2image.util import rounded_rectangle


class DefaultStyle(MonokaiStyle):
    code_bg = '#661A0A'


class Code2ImageBasic(object):

    formatter = None
    lexer = None

    def set_lexer_by_filename(self, filename):
        self.lexer = get_lexer_for_filename(filename)

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
        return Image.open(BytesIO(highlight(code, lexer, fm)))


class Code2Image(Code2ImageBasic):
    """Create a code box with rounded corners and a customized background"""

    def __init__(self, **kwargs):
        super(Code2Image, self).__init__()
        self.code_bg = kwargs.get('code_bg', '#661A0A')
        self.font_size = kwargs.get('font_size', 16)
        self.font_name = kwargs.get('font_name', 'Liberation Mono')
        self.line_pad = kwargs.get('line_pad', 5)
        self.line_numbers = kwargs.get('line_numbers', False)

        self.formatter = ImageFormatter(
            font_size=self.font_size,
            font_name=self.font_name,
            line_pad=self.line_pad,
            line_numbers=self.line_numbers,
            style=DefaultStyle,
        )
        self.lexer = PythonLexer()

        for name, attr in kwargs.items():
            setattr(self, name, attr)

    def get_formatter(self):
        style = DefaultStyle
        style.background_color = self.code_bg
        return ImageFormatter(
            font_size=self.font_size,
            font_name=self.font_name,
            line_pad=self.line_pad,
            line_numbers=self.line_numbers,
            style=style,
        )

    def highlight(self, code):
        img = super(Code2Image, self).highlight(code)
        m = tuple([round(s*1.03) for s in img.size])
        background = Image.new("RGBA", m)
        draw = ImageDraw.Draw(background)
        rounded_rectangle(draw, ((0, 0), m), 20, fill=self.code_bg)
        background.paste(
            img, ((m[0] - img.size[0]) // 2, (m[1] - img.size[1]) // 2)
        )
        return background


class Code2ImageShadow(Code2Image):
    """Add a shadow to the code box"""

    def __init__(self, **kwargs):
        super(Code2ImageShadow, self).__init__(**kwargs)
        self.shadow_dt = kwargs.get('shadow_dt', 2)
        self.shadow_color = kwargs.get('shadow_color', '#111111')
        self.blur = kwargs.get('blur', 5)

    def highlight(self, code):
        img = super(Code2ImageShadow, self).highlight(code)
        t = max(img.size)
        m = tuple(
            [round(s+t*(self.shadow_dt*0.03+self.blur*0.01)) for s in img.size]
        )
        box = (
            ((m[0]-img.size[0])//2, (m[1]-img.size[1])//2),
            ((m[0]+img.size[0])//2, (m[1]+img.size[1])//2)
        )
        dt = round(m[0]*self.shadow_dt*0.01)
        blur = round(m[0]*self.blur*0.002)

        background = Image.new("RGBA", m)
        draw = ImageDraw.Draw(background)
        rounded_rectangle(
            draw, ((box[0][0]+dt, box[0][1]+dt), (box[1][0]+dt, box[1][1]+dt)),
            20, fill=self.shadow_color
        )
        background = background.filter(ImageFilter.GaussianBlur(blur))
        background.paste(
            img, ((m[0] - img.size[0]) // 2, (m[1] - img.size[1]) // 2), img
        )
        return background


class Code2ImageBackground(Code2ImageShadow):

    def __init__(self, **kwargs):
        super(Code2ImageBackground, self).__init__(**kwargs)
        self.offset = kwargs.get('offset', 0)
        self.img_bg = kwargs.get('img_bg', '#AAAAAA')

    def highlight(self, code):
        img = super(Code2ImageBackground, self).highlight(code)
        m = round(max(img.size)*(1+(self.offset*0.01)))

        background = Image.new("RGB", (m, m), self.img_bg)
        background.paste(
            img, ((m - img.size[0]) // 2, (m - img.size[1]) // 2), img
        )
        return background
