from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class SearchForm(FlaskForm):
    content = StringField('content',validators=[DataRequired(message=u'查询不能为空')])