from flask import Blueprint, render_template, request, redirect
from .models import ShortenedURL
from .extensions import db
from .authentication import requires_auth

shortener = Blueprint('shortener', __name__)

@shortener.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        link = ShortenedURL(original_url=original_url)
        db.session.add(link)
        db.session.commit()
        return render_template('link_added.html', new_link=link.short_code, original_url=link.original_url)
    return render_template('index.html')

@shortener.route('/<short_code>')
def redirect_to_url(short_code):
    link = ShortenedURL.query.filter_by(short_code=short_code).first_or_404()
    link.visits += 1
    db.session.commit()
    return redirect(link.original_url)

@shortener.route('/stats')
@requires_auth
def stats():
    links = ShortenedURL.query.order_by(ShortenedURL.visits.desc()).all()
    return render_template('stats.html', links=links)

@shortener.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



