
from flask import Flask, jsonify
from app.repositories.db import db
from blueprints.distributor import bp as distributor_bp
from blueprints.product import bp as product_bp
from blueprints.customer import bp as customer_bp
from blueprints.stock import bp as stock_bp



def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite3'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:Emraldss25@localhost/Pharmacy'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db = SQLAlchemy(app)
    db.init_app(app)

    # Return validation errors as JSON
    @app.errorhandler(422)
    @app.errorhandler(400)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code

    app.register_blueprint(distributor_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(stock_bp)
    return app

app = create_app()
# breakpoint()


if __name__ == "__main__":
    app.run(debug=True)

