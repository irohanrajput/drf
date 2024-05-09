from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"
    # we've inherited everything from the class 'TokenAuthentication' and the changed the keyword to 'Bearer' from the default keyword 'Token', that's it.
