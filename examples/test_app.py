from flask import Flask

from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig
from pf_flask_swagger.flask.pf_flask_swagger import PFFlaskSwagger
from pf_flask_swagger.swagger.pf_swagger_decorator import get_request

app = Flask(__name__)


PFFlaskSwaggerConfig.default_tag_name = "Test API"
flask_swagger = PFFlaskSwagger(app)



@app.route('/')
def bismillah():
    return "PF Flask Swagger Test"


@app.route('/get-request')
@get_request()
def get_request_endpoint():
    return "PF Flask Swagger Test"


if __name__ == '__main__':
    app.run()
