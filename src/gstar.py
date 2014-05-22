import urllib2

from bs4 import BeautifulSoup

class GooglePlayUrls(object):
    DETAILS_BASE_URL = "https://play.google.com/store/apps/details?"
    DETAILS_ID_PARAM = "id="

class GStar(object):
    @staticmethod
    def star_rating(package):
        url = GooglePlayUrls.DETAILS_BASE_URL + GooglePlayUrls.DETAILS_ID_PARAM + str(package)
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        ratings_div_attrs = { HtmlAttributes.CSS_CLASS : CssClassHelper.RATING_HISTOGRAM }
        ratings_div = soup.find(HtmlTags.DIV, attrs = ratings_div_attrs)

        five_star_div = ratings_div.find(HtmlTags.DIV, attrs = GStar.__ratings_div_attrs("five"))
        four_star_div = ratings_div.find(HtmlTags.DIV, attrs = GStar.__ratings_div_attrs("four"))
        three_star_div = ratings_div.find(HtmlTags.DIV, attrs = GStar.__ratings_div_attrs("three"))
        two_star_div = ratings_div.find(HtmlTags.DIV, attrs = GStar.__ratings_div_attrs("two"))
        one_star_div = ratings_div.find(HtmlTags.DIV, attrs = GStar.__ratings_div_attrs("one"))

        star_number_span_attrs = { HtmlAttributes.CSS_CLASS : CssClassHelper.BAR_NUMBER}
        five_star_span = five_star_div.find(HtmlTags.SPAN, attrs = star_number_span_attrs)
        four_star_span = four_star_div.find(HtmlTags.SPAN, attrs = star_number_span_attrs)
        three_star_span = three_star_div.find(HtmlTags.SPAN, attrs = star_number_span_attrs)
        two_star_span = two_star_div.find(HtmlTags.SPAN, attrs = star_number_span_attrs)
        one_star_span = one_star_div.find(HtmlTags.SPAN, attrs = star_number_span_attrs)

        star_ratings = StarRatings()
        star_ratings.package = str(package)
        star_ratings.five = str(five_star_span.string)
        star_ratings.four = str(four_star_span.string)
        star_ratings.three = str(three_star_span.string)
        star_ratings.two = str(two_star_span.string)
        star_ratings.one = str(one_star_span.string)

        return star_ratings

    @staticmethod
    def __ratings_div_attrs(star_string):
        return { HtmlAttributes.CSS_CLASS : CssClassHelper.rating_class(star_string) }

class StarRatings(object):
    @property
    def package(self): return self._package
    @package.setter
    def package(self, value): self._package = value

    @property
    def five(self): return self._five
    @five.setter
    def five(self, value): self._five = value

    @property
    def four(self): return self._four
    @four.setter
    def four(self, value): self._four = value

    @property
    def three(self): return self._three
    @three.setter
    def three(self, value): self._three = value

    @property
    def two(self): return self._two
    @two.setter
    def two(self, value): self._two = value

    @property
    def one(self): return self._one
    @one.setter
    def one(self, value): self._one = value

class HtmlAttributes(object):
    CSS_CLASS = "class"

class HtmlTags(object):
        DIV = "div"
        SPAN = "span"

class CssClassHelper(object):
    BAR_NUMBER = "bar-number"
    HTML_CLASS_ATTR = "class"
    RATING_HISTOGRAM = "rating-histogram"
    RATING_BAR = "rating-bar-container"
    
    @staticmethod
    def rating_class(rating):
        return CssClassHelper.RATING_BAR + " " + str(rating)

def main():
    bbm_rating = GStar.star_rating("com.bbm");
    pretty_print(bbm_rating)
    
def pretty_print(star_ratings):
    print "package: " + str(star_ratings.package)
    print "five" 
    print str(star_ratings.five)
    print "four"
    print str(star_ratings.four)
    print "three" 
    print str(star_ratings.three)
    print "two"
    print str(star_ratings.two)
    print "one"
    print str(star_ratings.one)  

if __name__ == '__main__':
    main()