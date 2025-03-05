from flask import Blueprint, request, jsonify, render_template
from .database import insert_jobs
from .parser import HHParser, AvitoParser, HabrCareerParser

app = Blueprint('routes', __name__)

@app.route('/search')
def search():
    job_title = request.args.get('job_title')
    city = request.args.get('city')
    company = request.args.get('company')

    parsers = [HHParser(), AvitoParser(), HabrCareerParser()]
    jobs = []

    for parser in parsers:
        jobs.extend(parser.parse(job_title, city, company))

    insert_jobs([(job['title'], job['company'], job['salary'], job['experience'], job['city']) for job in jobs])
    return jsonify({'jobs': jobs})

@app.route('/')
def index():
     return render_template('findJob.html')