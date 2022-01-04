from flask import Flask, redirect
from examples.example_dto import query_params, url_params, PersonDTO
from examples.student_blueprint import student_blueprint
from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig
from pf_flask_swagger.flask.pf_flask_swagger import PFFlaskSwagger
from pf_flask_swagger.swagger.pf_swagger_decorator import get_request, post_request, post_upload_request, \
    post_form_request, put_request, delete_request, patch_request, get_paginate_request

app = Flask(__name__)
app.register_blueprint(student_blueprint)


PFFlaskSwaggerConfig.default_tag_name = "Common API"
PFFlaskSwaggerConfig.title = "PF Flask Swagger Example Output"
PFFlaskSwaggerConfig.enable_pf_api_convention = True
PFFlaskSwaggerConfig.enable_swagger_view_page = True
PFFlaskSwaggerConfig.enable_jwt_auth_global = False
flask_swagger = PFFlaskSwagger(app)


@app.route('/')
def bismillah():
    return redirect("/pf-flask-swagger-ui")


@app.route('/get-request')
@get_request(query_params=query_params, url_params=url_params, response_obj=PersonDTO)
def get_request_endpoint():
    return "PF Flask Swagger Test"


@app.route('/post-request')
@post_request(request_obj=PersonDTO, response_list=PersonDTO)
def post_request_endpoint():
    return "PF Flask Swagger Test"


@app.route('/post-upload-request')
@post_upload_request(request_obj=PersonDTO)
def post_upload_request():
    return "PF Flask Swagger Test"


@app.route('/post-form-request')
@post_form_request(request_obj=PersonDTO)
def post_form_request():
    return "PF Flask Swagger Test"


@app.route('/put-request')
@put_request(pf_error_details_response=False, pf_message_response=True)
def put_request():
    return "PF Flask Swagger Test"


@app.route('/delete-request')
@delete_request()
def delete_request():
    return "PF Flask Swagger Test"


@app.route('/patch-request')
@patch_request()
def patch_request():
    return "PF Flask Swagger Test"


@app.route('/get-paginate-request')
@get_paginate_request()
def get_paginate_request():
    return "PF Flask Swagger Test"


if __name__ == '__main__':
    app.run(debug=True)
