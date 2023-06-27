from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
class BearerAuthentication(TokenAuthentication):
    keyword = 'Bearer'

class QueryParameterTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        # Extract the token from query parameters
        token = request.query_params.get('key')
        
        if token:
            return self.authenticate_credentials(token)
        else:
            raise AuthenticationFailed('Token not provided in query parameters')