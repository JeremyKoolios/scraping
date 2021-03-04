from flask import Flask, render_template
import nzdir_scraper as scraper

scraping_app = Flask(__name__)

@scraping_app.route('/')
def index():
    return render_template('display_results.html')