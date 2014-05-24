import unittest
import gstar

from urllib2 import URLError
from mock import Mock, patch

class gstarTester(unittest.TestCase):

    def setUp(self):
        self.package = "package"
        self.gstar = gstar.GStar()

    @patch('gstar.urllib2.urlopen')
    def test_star_rating_url_error(self, mock_urllib_urlopen):
        mock_urllib_urlopen.side_effect = URLError("some error")
        self.assertRaises(URLError, self.gstar.star_rating(self.any_package))
        self.assertRaisesRegexp(URLError, "some error", self.gstar.star_rating(self.any_package))
        self.assertEqual(None, self.gstar.star_rating(self.any_package))

    @patch('gstar.urllib2.urlopen')
    def test_ratings_div_css_changed(self, mock_urllib_urlopen):
        with patch('gstar.BeautifulSoup') as mock_beautiful_soup:
            soup = Mock()
            soup.find.return_value = None
            mock_beautiful_soup.return_value = soup

            html = Mock()
            response = Mock()
            response.read.return_value = html
            mock_urllib_urlopen.return_value = response

            self.assertRaises(gstar.CssHasChangedException, self.gstar.star_rating(self.package))
            self.assertRaisesRegexp(\
                gstar.CssHasChangedException,
                gstar.CssClassHelper.RATING_HISTOGRAM,
                self.gstar.star_rating(self.package))
            self.assertEqual(None, self.gstar.star_rating(self.package))

    @patch('gstar.urllib2.urlopen')
    def test_star_div_css_changed(self, mock_urllib_urlopen):
        with patch('gstar.BeautifulSoup') as mock_beautiful_soup:
            soup = Mock()
            ratings_div = Mock()
            ratings_div.find.return_value = None
            soup.find.return_value = ratings_div
            mock_beautiful_soup.return_value = soup

            html = Mock()
            response = Mock()
            response.read.return_value = html
            mock_urllib_urlopen.return_value = response

            self.assertRaises(gstar.CssHasChangedException, self.gstar.star_rating(self.package))
            self.assertRaisesRegexp(\
                gstar.CssHasChangedException,
                gstar.CssClassHelper.rating_class(""),
                self.gstar.star_rating(self.package))
            self.assertEqual(None, self.gstar.star_rating(self.package))
            self.assertEqual(None, self.gstar.star_rating(self.package))
#
    @patch('gstar.urllib2.urlopen')
    def test_star_span_css_changed(self, mock_urllib_urlopen):
        with patch('gstar.BeautifulSoup') as mock_beautiful_soup:
            soup = Mock()
            ratings_div = Mock()
            star_div = Mock()
            star_div.find.return_value = None
            ratings_div.find.return_value = star_div
            soup.find.return_value = ratings_div
            mock_beautiful_soup.return_value = soup

            html = Mock()
            response = Mock()
            response.read.return_value = html
            mock_urllib_urlopen.return_value = response

            self.assertRaises(gstar.CssHasChangedException, self.gstar.star_rating(self.package))
            self.assertRaisesRegexp(\
                gstar.CssHasChangedException,
                gstar.CssClassHelper.BAR_NUMBER,
                self.gstar.star_rating(self.package))
            self.assertEqual(None, self.gstar.star_rating(self.package))
            self.assertEqual(None, self.gstar.star_rating(self.package))
#
    def test_star_rating_expected(self):
        star_ratings = gstar.StarRatings()
        star_ratings.five = Mock(return_value = 5)
        star_ratings.four = Mock(return_value = 4)
        star_ratings.three = Mock(return_value = 3)
        star_ratings.two = Mock(return_value = 2)
        star_ratings.one = Mock(return_value = 1)

        self.gstar.star_rating = Mock()
        self.gstar.star_rating.return_value = star_ratings
        self.results = self.gstar.star_rating(self.package)

        self.assertEqual(5, self.results.five())
        self.assertEqual(4, self.results.four())
        self.assertEqual(3, self.results.three())
        self.assertEqual(2, self.results.two())
        self.assertEqual(1, self.results.one())

if __name__ == "__main__":
    unittest.main()
