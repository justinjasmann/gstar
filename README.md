#gstar
***
##Overview

I needed a quick and easy way to get the star ratings for any app that was available on the Google Play Store.

I have written this simple module in Python that enables any developer to do just that.

###Description

This is a simple python module that will help retrieve star ratings from the Google Play Store.

###TODO

* Ability to retrieve the star ratings for multiple apps at once
* Retrieve averaged star rating as well
* Expand to retrieve other info (# of installs, current version, etc.)

###Install

1. Clone this repository

	```
	git clone https://github.com/justinjasmann/gstar.git
	```

2. Extract the distributable `.tar`

	```
	cd dist/
	tar -xvf gstar-Google-Play-Scraper-0.1dev
	```
	
3. Run the installer

	```
	cd gstar-Google-Play-Scraper-0.1dev
	python setup.py install
	```
	
	Note: Depending on your environment, you may need to execute using `sudo`. 

####Usage

Sample

	from gstar import GStar

	gstar = GStar()
	star_ratings = gstar.star_rating("com.android.chrome")

	print "Package: " + star_ratings.package
	print "Five stars: " + star_ratings.five
	print "Four stars: " + star_ratings.four
	print "Three stars: " + star_ratings.three
	print "Two stars: " + star_ratings.two
	print "One star: " + star_ratings.one
	
	...
	
	# Output
	Package: com.android.chrome
	Five stars: 995,805
	Four stars: 262,189
	Three stars: 118,266
	Two stars: 53,407
	One star: 120,073


###Feedback

Any and all feedback is, of course, welcome. 

If you've got suggestions/comments, feel free to send me an email. Otherwise, I look forward to your pull requests :D

Thanks for your time!

###Contact

Justin Jasmann | @JustinJasmann | <justin.jasmann@gmail.com>
