#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Iancecil Waweru 134669
"""

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import werkzeug
import os
import job_finder as jf
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

CORS(app)



parser = reqparse.RequestParser()

UPLOAD_DIR="Users/Iancecil/Documents/Flask_Project/job_finder-main/api/assets/cvs"

ALLOWED_EXTENSIONS = set(['docx', 'pdf',])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# class RetrieveJobs(Resource):
#     def get(self, filename):
#         print(f'Filename -- {filename}')
        
#         if (filename == None):
#             resp = jsonify({
#                 'status' : 'fail',
#                 'message': 'File Not Found'
#                 })
#             resp.status_code = 404
#             return resp
        
#         jobs_df = jf.main(filename)
        
#         resp = jsonify({
#                 'status' : 'success',
#                 'data': jobs_df.to_dict('records')
#                 })
#         resp.status_code = 200
#         return resp
    
    

class CVProcessor(Resource):
    
    def post(self):
        parser.add_argument('cv_file', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()
        
        cv_file = args['cv_file']
        
        # check if the post request has the file part
        if cv_file == None:
            resp = jsonify({
                'status' : 'fail',
                'message' : 'No file part in the request'
                })
            resp.status_code = 400
            return resp
        if (cv_file.filename == ''):
            resp = jsonify({
                'status' : 'fail',
                'message' : 'No file selected for uploading'
                })
            resp.status_code = 400
            return resp
        
        if cv_file and allowed_file(cv_file.filename):
            
            cv_file.save(os.path.join(UPLOAD_DIR, cv_file.filename))
            
            jobs_df = jf.main(cv_file.filename)
            print(f'FILENAME {cv_file.filename}')
            
            resp = jsonify({
                'status' : 'success',
                'message' : 'File successfully uploaded',
                'data': jobs_df.to_dict('records')
                })
            resp.status_code = 201
            return resp
        else:
            resp = jsonify({
                'status' : 'fail',
                'message' : 'Only txt and pdf files allowed'
                })
            resp.status_code = 400
            return resp
        
    

api.add_resource(CVProcessor,'/cv_processor')


if __name__ == "__main__":
    app.run(debug=True, port=8080)
    