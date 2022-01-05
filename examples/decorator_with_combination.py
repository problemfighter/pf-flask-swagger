from flask import Flask, redirect
from marshmallow import fields
from pf_flask_rest_com.api_def import APIDef, FileField
from pf_flask_swagger.swagger.data.swagger_constant import DataTypeConst
from pf_flask_swagger.flask.pf_flask_swagger import PFFlaskSwagger
from pf_flask_swagger.swagger.pf_swagger_decorator import get_request, get_paginate_request, post_upload_request, \
    post_form_request, put_request, delete_request, patch_request, post_request

GET_REQUEST_TAG = "GET Request Only"
POST_REQUEST_TAG = "POST Request Only"


class PersonDTO(APIDef):
    first_name = fields.String(required=True, error_messages={"required": "Please enter first name"})
    last_name = fields.String(allow_none=None)
    email = fields.Email(required=True, error_messages={"required": "Please enter email."})
    income = fields.Float(allow_none=None)
    image = FileField(allow_none=None)


app = Flask(__name__)
flask_swagger = PFFlaskSwagger(app)


@app.route('/')
def bismillah():
    return redirect("/pf-flask-swagger-ui")


@app.route('/simple-get-request')
@get_request(tag=GET_REQUEST_TAG)
def simple_get_request_endpoint():
    return "PF Flask Swagger Simple GET Request"


@app.route('/get-request-with-param')
@get_request(query_params=[("age", DataTypeConst.integer, True), ("name", DataTypeConst.string)], tag=GET_REQUEST_TAG)
def get_request_with_param():
    return "PF Flask Swagger GET request with param"


@app.route('/get-request-with-url-param')
@get_request(url_params=[("age", DataTypeConst.integer, True), ("name", DataTypeConst.string)], tag=GET_REQUEST_TAG)
def get_request_with_url_param():
    return "PF Flask Swagger GET request with URL param"


@app.route('/get-request-with-flask-url-param/<int:age>/<string:name>')
@get_request(tag=GET_REQUEST_TAG)
def get_request_with_flask_url_param(age: int, name: str):
    return "PF Flask Swagger GET request with Flask URL param"


@app.route('/get-paginate-request')
@get_paginate_request(tag=GET_REQUEST_TAG)
def get_paginate_request():
    return "PF Flask Swagger with pagination request"


@app.route('/post-form-request')
@post_form_request(request_obj=PersonDTO, tag=POST_REQUEST_TAG)
def post_form_request():
    return "PF Flask Swagger Form Request"


@app.route('/post-upload-request')
@post_upload_request(request_obj=PersonDTO, tag=POST_REQUEST_TAG)
def post_upload_request():
    return 'PF Flask Swagger File Upload Request'


@app.route('/post-request-single-object')
@post_request(request_obj=PersonDTO, response_list=PersonDTO, tag=POST_REQUEST_TAG)
def post_request_single_object():
    return "PF Flask Swagger POST request with single object"


@app.route('/post-request-list-object')
@post_request(request_list=PersonDTO, response_list=PersonDTO, tag=POST_REQUEST_TAG)
def post_request_list_object():
    return "PF Flask Swagger POST request with list object"


@app.route('/post-request-single-response')
@post_request(request_obj=PersonDTO, response_obj=PersonDTO, tag=POST_REQUEST_TAG)
def post_request_single_response():
    return "PF Flask Swagger POST request with single response"


@app.route('/post-request-list-response')
@post_request(request_list=PersonDTO, response_list=PersonDTO, tag=POST_REQUEST_TAG)
def post_request_list_response():
    return "PF Flask Swagger POST request with list response"


@app.route('/put-request')
@put_request(request_obj=PersonDTO)
def put_request():
    return "PF Flask Swagger using PUT method"


@app.route('/delete-request')
@delete_request()
def delete_request():
    return "PF Flask Swagger using DELETE method"


@app.route('/patch-request')
@patch_request(request_obj=PersonDTO)
def patch_request():
    return "PF Flask Swagger using PATCH method"


if __name__ == '__main__':
    app.run(debug=True)
