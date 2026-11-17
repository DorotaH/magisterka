import os
from flask_mail import Mail

def task_func(app):
    """
    Initialize a Flask application with Flask-Mail. 

    Parameters:
    app (Flask): The Flask application to configure.

    Returns:
    tuple: A tuple containing the Flask-Mail instance and the app's mail configurations.

    Note:
    - The details of the email server are retrieved from environment variables. 
    - If the variables do not exist, use defaults.
    
    Requirements:
    - os
    - flask_mail

    Example:
    >>> from flask import Flask
    >>> app = Flask("test")
    >>> mail, configs = task_func(app)
    >>> 'MAIL_SERVER' in configs
    True
    """

    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'localhost')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 25))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', False) == 'True'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', None)
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', None)
    
    mail = Mail(app)
    
    return mail, {
        'MAIL_SERVER': app.config['MAIL_SERVER'],
        'MAIL_PORT': app.config['MAIL_PORT'],
        'MAIL_USE_TLS': app.config['MAIL_USE_TLS'],
        'MAIL_USERNAME': app.config['MAIL_USERNAME'],
        'MAIL_PASSWORD': app.config['MAIL_PASSWORD']
    }
