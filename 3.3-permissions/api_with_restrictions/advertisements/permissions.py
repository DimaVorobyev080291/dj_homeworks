from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    """
    Проверка что Advertisement и creator принадлежит одному пользовтелю и возможность другим 
    пользователям просматривать Advertisement дргуих пользователей (без возможности их удалять, редактировать).
    """
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.creator