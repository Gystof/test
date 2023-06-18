from flask import Blueprint
from backend.modules import b_clients

backend = Blueprint(
    'backend',
    __name__,
    template_folder='./views',
    static_folder='./assets/node_modules'
)

backend.clients_blueprint(
    b_clients,
    url_prefix='/clients'
)

__all__ = ['backend']
