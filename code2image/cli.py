import argparse

from code2image.cls import Code2ImageShadow


def main():
    parser = argparse.ArgumentParser(description='Create nice code snippets')
    parser.add_argument('codefile', type=str, help='The code file')
    parser.add_argument('imagename', type=str, help='The output image')

    parser.add_argument('--code', type=str, default='#661A0A',
                        help='Code background color')
    parser.add_argument('--background', type=str, default='#AAAAAA',
                        help='Image background color')
    parser.add_argument('--shadow-color', type=str, default='#111111',
                        help='Shadow color')
    parser.add_argument('--shadow-dt', type=int, default=4,
                        help='Shadow offset')
    parser.add_argument('--offset', type=int, default=10, help='Border width')
    parser.add_argument('--blur', type=int, default=20, help='Shadow blur')

    args = parser.parse_args()

    c2i = Code2ImageShadow(
        code_bg=args.code,
        img_bg=args.background,
        shadow_color=args.shadow_color,
        shadow_dt=args.shadow_dt,
        offset=args.offset,
        blur=args.blur,
    )

    with open(args.codefile) as f:
        code = f.read()

    img = c2i.highlight(code)
    img.save(args.imagename)
