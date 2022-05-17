from rest_framework import status


class CodeHTTPError:

    @staticmethod
    def get_http_code(json):
        incident_message = json['incidents']
        incidence = incident_message[-len(incident_message)]
        code_http = None
        if incidence:
            code_http = status.HTTP_400_BAD_REQUEST
        if 'result' in json:
            del json['result']
        return code_http, json
