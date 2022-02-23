# Cheddarbutler_v2_baconsaver
A quick data frame creator for options chains of given stocks that are passed through simple signal parameters

# Set up and installation

Cheddarbutler version 2: Baconsaver is an app that is a simplified version of Cheddarbutler version 1. It does 
not have the broker configuration files that version 1 had, and relies on a different and more autonomous
system of getting stock tickers from websites by scraping them and getting them unto a iterable list.

1) install the requirements file using pip

pip install -r requirements.txt

2) configure the starting script

the start.py script will have ### sections prompting for user input for setting up variables like dates and 
stock tickers to work from.

run 

python start.py

3) configure additional files

the ticker_scraper.py script can be edited to include additional sites. The default sites to search stock
tickers are the after hours stock market activity webpages on marketwatch and the nasdaq page.


# Customization

Baconsaver is open source code that is just a culmination of research and training with videos that are credited
in the credits and references file. The author of this repository takes no credit in the concepts applied in this script. 
Similarly the user license is MIT which is a permissive license, meaning "As a permissive license, it puts only
very limited restriction on reuse and has, therefore, high license compatibility."

Some suggestions of additionals applications of this script:
  -run alongside a machine learning model
  -wait for deployment of Cheddarbutler version 1 to see examples of broker connectivity and fully automated trading.
  -build database of stock tickers to track apply social media apis
  -see credits and references page for original inspiration and true credits of this project :)
