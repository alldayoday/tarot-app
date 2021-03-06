from flask import render_template, request, Blueprint
from myapp.models import TarotPost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    tarot_posts = TarotPost.query.order_by(TarotPost.date.desc()).paginate(page=page, per_page=8)
    return render_template('index.html', tarot_posts=tarot_posts)

@core.route('/info')
def info():
    return render_template('info.html')