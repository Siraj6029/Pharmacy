import copy
import unittest
from app.repositories.db import db
from app.repositories.models import *

db_uri = "sqlite:///test.db"

def _flask_impl(with_db=False):

    import api

    current_app = api.create_app()
    current_db = None

    old_url_map = copy.copy(current_app.url_map)
    old_view_functions = copy.copy(current_app.view_functions)

    @current_app.route("/test_errors")
    def test_errors():
        raise ValueError("Testing unknown failures")

    current_app.testing = True
    current_app.debug = False
    client = current_app.test_client()

    ctx = current_app.test_request_context()
    ctx.push()
    current_app.preprocess_request()

    if with_db:
        current_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        db.init_app(current_app)
        db.create_all()
        current_db = db
    return current_app, client, old_url_map, old_view_functions, ctx, current_db

class FlaskClient(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        self.current_app = None
        self.app_ctx = None
        self.old_url_map = None
        self.old_view_functions = None
        self.client = None
        self.db = None

    def setUp(self):
        (
            self.current_app,
            self.client,
            self.old_url_map,
            self.old_view_functions,
            self.app_ctx,
            self.db
        ) = _flask_impl()

    def tearDown(self):
        self.current_app.url_map = self.old_url_map
        self.current_app.view_functions = self.old_view_functions

        self.current_app._got_first_request = False
        self.app_ctx.pop()

class FlaskClientWithDB(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        self.current_app = None
        self.app_ctx = None
        self.old_url_map = None
        self.old_view_functions = None
        self.client = None
        self.db = None

    def setUp(self):
        (
            self.current_app,
            self.client,
            self.old_url_map,
            self.old_view_functions,
            self.app_ctx,
            self.db
        ) = _flask_impl(with_db=True)

    def tearDown(self):
        self.current_app.url_map = self.old_url_map
        self.current_app.view_functions = self.old_view_functions

        self.current_app._got_first_request = False
        self.app_ctx.pop()

