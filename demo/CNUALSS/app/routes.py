from app import app
from flask import render_template
from sqlalchemy import desc,asc,and_,or_
from app.models import Cate,Beauty,Recreation


@app.route('/')
def index():
    # 获取一些价格比较低的项目，价位从低到高，前6条
    cheap_cate = Cate.query.filter_by().order_by('person_price').limit(6).all()
    cheap_beauty = Beauty.query.filter_by().order_by('person_price').limit(6).all()
    cheap_recreation = Recreation.query.filter_by().order_by('person_price').limit(6).all()
    return render_template('index.html', cheap_cate=cheap_cate, cheap_beauty=cheap_beauty, cheap_recreation=cheap_recreation)


@app.route('/about')
def about():
    return render_template('about.html')