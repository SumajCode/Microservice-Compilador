from flask import jsonify
class Controller:
    def __init__(self):
        pass

    def obtenerRequest(self, request):        
        return request.get_json() if request.is_json else request.form

    def response(self, datos):
        """
        Constructs a JSON response object from the provided data dictionary.

        Parameters
        ----------
        datos : dict
            A dictionary containing the following keys:
            - 'data': The response data to be included in the JSON.
            - 'message': A message string describing the response status.
            - 'status': A status string indicating the result of the operation.
            - 'code': An HTTP status code for the response.

        Returns
        -------
        Response
            A Flask response object with the specified JSON structure.
        """
        return jsonify({
            'data': datos['data'],
            'message': datos['message'],
            'status': datos['status'],
            'code': datos['code']
        })
