from flask import Flask
import nzdir_scraper as scraper

scraping_app = Flask(__name__)

@scraping_app.route('/')
def index():
    return str(scraper.scrape('automotives'))