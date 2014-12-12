#-*- coding: utf-8 -*-
# import this module to recognize non-ASCII characters
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from flask_wtf import Form
from wtforms import FileField, TextField, TextAreaField, SelectField, IntegerField


class IndexForm(Form):

    emri = TextField('Emri')
