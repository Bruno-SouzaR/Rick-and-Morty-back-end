from flask import jsonify

class ApiReponse: 

    @staticmethod
    def response(success=True, data=None, message=None, status_code=200):
      
        response = {
            "success": success, 
            "message": message,
            "data": data      
        }
        return jsonify(response), status_code