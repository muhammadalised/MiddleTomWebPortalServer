import os

from flask import Flask

import os





def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)


    # Register the BluePrints
    from . import patients,reports, doctors
    app.register_blueprint(patients.bp)
    app.register_blueprint(reports.bp)
    app.register_blueprint(doctors.bp)

    return app

if __name__ == "__main__":
   app = create_app()
   app.run(host='127.0.0.1', debug=True)

