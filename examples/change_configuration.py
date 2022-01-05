from flask import Flask, redirect
from pf_flask_swagger.swagger.pf_swagger_decorator import get_request
from pf_flask_swagger.flask.pf_flask_swagger import PFFlaskSwagger
from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig

app = Flask(__name__)

PFFlaskSwaggerConfig.default_tag_name = "Common API"
PFFlaskSwaggerConfig.title = "PF Flask Swagger Example Output"
PFFlaskSwaggerConfig.enable_pf_api_convention = True
PFFlaskSwaggerConfig.enable_swagger_view_page = True
PFFlaskSwaggerConfig.enable_jwt_auth_global = False
flask_swagger = PFFlaskSwagger(app)


@app.route('/')
def bismillah():
    return redirect("/pf-flask-swagger-ui")


@app.route('/simple-get-request')
@get_request()
def simple_get_request_endpoint():
    return "PF Flask Swagger Simple GET Request"


if __name__ == '__main__':
    app.run()
