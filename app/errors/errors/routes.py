"""
The module for Errors Routes.
Amer Ahmed
Version 0.0
"""

from flask import Blueprint, jsonify, render_template, request

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(403)
def forbidden(e):
    # Forbidden to access without authentication
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'forbidden'})
        response.status_code = 403
        return response
    return render_template('errors/403.html'), 403


@errors.app_errorhandler(404)
def page_not_found(e):
    # Returns 404 if page not found
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('errors/404.html'), 404


@errors.app_errorhandler(500)
def internal_server_error(e):
    """Return 500 if server no response or internal errors"""
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'internal server error'})
        response.status_code = 500
        return response
    return render_template('errors/500.html'), 500
