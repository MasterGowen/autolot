from flask import Blueprint, render_template

mod = Blueprint('main', __name__)


@mod.route('/')
def index():
    return render_template(
        'main/index.html',
    )


@mod.route('/statistics')
def statistics():
    return render_template(
        'main/statistics.html',
    )


@mod.route('/auction')
def auction():
    return render_template(
        'main/auction.html',
    )


@mod.route('/news')
def news():
    return render_template(
        'main/news.html',
    )


@mod.route('/feedback')
def feedback():
    return render_template(
        'main/feedback.html',
    )


@mod.route('/articles')
def articles():
    return render_template(
        'main/articles.html',
    )
