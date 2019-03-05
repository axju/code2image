import unittest
from PIL import Image

from code2image.cls import Code2ImageBasic
from code2image.cls import Code2Image
from code2image.cls import Code2ImageShadow
from code2image.cls import Code2ImageBackground


class TestCode2ImageBasic(unittest.TestCase):

    def test_except(self):
        t = Code2ImageBasic()
        self.assertRaises(AttributeError, t.get_formatter)
        self.assertRaises(AttributeError, t.get_lexer)
        self.assertRaises(AttributeError, t.highlight, ['test'])


class TestCode2Image(unittest.TestCase):

    def test_highlight(self):
        t = Code2Image()
        img = t.highlight('print("Hello")')
        self.assertIsInstance(img, Image.Image)
        self.assertGreater(img.size[0], 0)
        self.assertGreater(img.size[1], 0)


class TestCode2ImageShadow(unittest.TestCase):

    def test_shadow(self):
        t = Code2ImageShadow()
        img = t.highlight('print("Hello")')
        self.assertIsInstance(img, Image.Image)
        self.assertGreater(img.size[0], 0)
        self.assertGreater(img.size[1], 0)


class TestCode2ImageBackground(unittest.TestCase):

    def test_shadow(self):
        t = Code2ImageBackground()
        img = t.highlight('print("Hello")')
        self.assertIsInstance(img, Image.Image)
        self.assertGreater(img.size[0], 0)
        self.assertGreater(img.size[1], 0)


if __name__ == '__main__':
    unittest.main()
