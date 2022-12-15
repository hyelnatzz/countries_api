"""
THIS MODULE CONTAINS THE FUNCTION FOR INITIATING ALL ERROR HANDLING ENDPOINTS

"""

from flask import jsonify

def setup_error_handlers(app):

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(
                {
                    "success": False,
                    "error": 404, 
                    "message": error.description
                }
            ), 404
        

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify(
                {
                    "success": False, 
                    "error": 422, 
                    "message": "unprocessable entity"
                }
            ), 422


    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(
                {
                    "success": False, 
                    "error": 400, 
                    "message": "bad request"
                }
            ), 400


    @app.errorhandler(500)
    def not_allowed(error):
        return jsonify(
                {
                    "success": False, 
                    "error": 500, 
                    "message": "something went wrong"
                }
            ), 500
