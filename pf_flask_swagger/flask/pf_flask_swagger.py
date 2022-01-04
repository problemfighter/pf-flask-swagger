from flask import Blueprint, render_template, request
from pf_flask_swagger.common.pf_flask_swagger_config import PFFlaskSwaggerConfig
from pf_flask_swagger.flask.basic_authentication import login_required
from pf_flask_swagger.flask.pf_flask_action_to_definition import PFFlaskActionToDefinition
from pf_flask_swagger.swagger.pf_swagger_generator import PFSwaggerGenerator


class PFFlaskSwagger:
    _app = None
    _blue_print = None

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self._app = app
        if self._app:
            self._init_swagger_blue_print()

    def _init_swagger_blue_print(self):
        if PFFlaskSwaggerConfig.enable_swagger_view_page and self._app:
            blue_print = Blueprint("PFFlaskSwagger", __name__, template_folder="templates", static_folder="pf-swagger-static")
            blue_print.add_url_rule("/pf-flask-swagger-json", "pf-flask-swagger-json", self.swagger_json)
            blue_print.add_url_rule("/pf-flask-swagger-ui", "pf-flask-swagger-ui", self.swagger_ui)
            self._app.register_blueprint(blue_print)

    def swagger_json(self):
        auth = self.check_auth()
        if auth:
            return auth
        pf_flask_action_to_definition = PFFlaskActionToDefinition(self._app)
        definitions = pf_flask_action_to_definition.get_action_to_definitions()
        pf_swagger_generator = PFSwaggerGenerator()
        pf_swagger_generator.process_list(definitions)
        return pf_swagger_generator.get_swagger_spec()

    def swagger_ui(self):
        auth = self.check_auth()
        if auth:
            return auth
        return render_template('pf-swagger-ui.html', config=PFFlaskSwaggerConfig)

    def check_auth(self):
        if PFFlaskSwaggerConfig.enable_api_auth:
            auth = request.authorization
            if not (auth and auth.username == PFFlaskSwaggerConfig.swagger_page_auth_user and auth.password == PFFlaskSwaggerConfig.swagger_page_auth_password):
                return ('You are not authorize to access the URL.', 401, {
                    'WWW-Authenticate': 'Basic realm="Login Required"'
                })
        return None
