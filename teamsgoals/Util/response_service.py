from rest_framework.response import Response

from teamsgoals.Util.http_code_error import CodeHTTPError


class ResponseService:

    def __init__(self, json_response, request=None):
        self._json_response = json_response
        self._request = request

    def get_response(self):
        status_code = None
        if len(self._json_response['incidents']) > 0:
            if len(self._json_response['incidents']) > 1:
                self._json_response['incidents'] = [self._json_response['incidents'][0]]
            status_code, self._json_response = CodeHTTPError.get_http_code(self._json_response)
        else:
            del self._json_response['incidents']
        response_service = Response(self._json_response)
        response_service['Cache-Control'] = 'no-cache'
        if status_code:
            response_service.status_code = status_code
        return response_service
