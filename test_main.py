import unittest
from main import RilakkumaHTML


html_sample = """
    <html>
      <head></head>
      <body>
        <p>hoge</p>
        <img src="images/9999.gif">
      </body>
"""


class RilakkumaHTMLTest(unittest.TestCase):

    def setUp(self):
        self.rirakkuma = RilakkumaHTML()
        self.rirakkuma.feed(html_sample)

    def test_get_img(self):
        imgs = self.rirakkuma.get_img()
        self.assertEqual(imgs, "images/9999.gif")

if __name__ == "__main__":
    unittest.main()
