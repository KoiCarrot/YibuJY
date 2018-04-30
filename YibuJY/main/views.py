from flask import render_template,redirect,url_for
from . import main
from .forms import SearchForm
import elasticsearch
es = elasticsearch.Elasticsearch()

@main.route('/',methods =['GET','POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        content = form.content.data
        return redirect(url_for('main.page',content = content))
    return render_template('index_templates/index.html',form=form)

@main.route('/search/<content>',methods = ['GET','POST'])
def page(content):
    res = es.search(index='scrapy_tv', doc_type='text-type',
                    body={"query": {"match": {
                        "name": content
                    }}})
    post = res['hits']['hits']
    return render_template('page_templates/index.html',post = post)