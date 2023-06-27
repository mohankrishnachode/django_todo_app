from rest_framework.permissions import BasePermission

class CanViewBook(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the 'view' permission
        return request.user and request.user.has_perm('books_app.view_books')

class CanEditBook(BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the 'edit' permission
        return request.user and request.user.has_perm('books_app.change_books')