from flask import render_template, request, redirect, url_for
from br.views.forms.indexform import IndexForm
from flask.views import MethodView
from br import mongo
from br.utils.utils import Utils

utils = Utils()


class Index(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        ''' Dispatch request
        '''
        return "Good to be back in Gjakova!"
    def post(self):
        '''process data and save them in database
        '''

        return redirect(url_for('index'))

    def save_business_form(self, doc_id):
        '''save form '''

