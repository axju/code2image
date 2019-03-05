import argparse

from code2image.cls import Code2Image, Code2ImageShadow, Code2ImageBackground


def main():
    parser = argparse.ArgumentParser(description='Create nice code snippets')
    parser.add_argument('codefile', type=str, help='The code file')

    parser.add_argument('--kind', default='shadow',
                        choices=['simple', 'shadow', 'background'],
                        help='Change the result')
    parser.add_argument('--imagename', type=str, help='The output image')

    parser.add_argument('--code', type=str, default='#661A0A',
                        help='Code background color')
    parser.add_argument('--background', type=str, default='#FFFFFF',
                        help='Image background color')

    parser.add_argument('--font-size', type=int, default=16, help='font size')
    parser.add_argument('--font-name', type=str, default='Liberation Mono',
                        help='font name')
    parser.add_argument('--line_pad', type=int, default=5, help='line pad')
    parser.add_argument('--line-numbers', action='store_true',
                        help='line numbers')

    parser.add_argument('--shadow-color', type=str, default='#111111',
                        help='Shadow color')
    parser.add_argument('--shadow-dt', type=int, default=2,
                        help='Shadow offset')
    parser.add_argument('--offset', type=int, default=0, help='Border width')
    parser.add_argument('--blur', type=int, default=5, help='Shadow blur')
    parser.add_argument('--scale', type=int, default=None, help='A scale')

    parser.add_argument('--epilog', type=str,
                        default='\n\n# This image was created with code2image',
                        help='A epilog')

    args = parser.parse_args()

    kwargs = {
        'code_bg': args.code,
        'font_size': args.font_size,
        'font_name': args.font_name,
        'line_pad': args.line_pad,
        'line_numbers': args.line_numbers,
        'img_bg': args.background,
        'shadow_color': args.shadow_color,
        'shadow_dt': args.shadow_dt,
        'offset': args.offset,
        'blur': args.blur,
        'scale': args.scale,
    }

    CLS_MAP = {
        'simple': Code2Image,
        'shadow': Code2ImageShadow,
        'background': Code2ImageBackground
    }

    with open(args.codefile) as f:
        code = f.read()

    cls = CLS_MAP.get(args.kind)
    c2i = cls(**kwargs)
    c2i.set_lexer_by_filename(args.codefile)

    img = c2i.highlight(code+args.epilog)
    filename = args.imagename if args.imagename else 'out.png'
    img.save(filename)
    print(f'create code image "{filename}"')
