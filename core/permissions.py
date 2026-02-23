from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_api_key.models import APIKey

class HasValidAPIKey(BasePermission):
    def has_valid_api_key(self, request):
        key = request.headers.get('X-API-KEY') # Header'dan API anahtarını al

        if not key:
            raise AuthenticationFailed('X-API-KEY header is missing')
        
        try:
            api_key_obj = APIKey.objects.get_from_key(key) # Veritabanında API anahtarını doğrula
        except APIKey.DoesNotExist:
            raise AuthenticationFailed('Invalid API key')
        
        request.auth = api_key_obj
        return True
    
    def has_permission(self, request, view):
        return self.has_valid_api_key(request)
    
class IsAuthenticatedWithAPIKey(HasValidAPIKey):
    def has_permission(self, request, view):
        self.has_valid_api_key(request)

        user = request.user

        if not user or not user.is_authenticated:
            raise AuthenticationFailed('JWT authentication failed or user is not authenticated')
        
        return True
    
class IsAdminWithAPIKey(HasValidAPIKey):
    def has_permission(self, request, view):
        self.has_valid_api_key(request)

        user = request.user

        if not user or not user.is_authenticated:
            raise AuthenticationFailed('JWT authentication failed or user is not authenticated')
        
        if not user.is_staff or not user.is_superuser:
            raise AuthenticationFailed('User is not an admin')
        
        return True