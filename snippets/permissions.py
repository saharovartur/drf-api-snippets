from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
     Пользовательское разрешение, позволяющее редактировать объект только владельцам.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение разрешены для любого запроса
        # поэтому мы всегда разрешаем запросы GET, HEAD или OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Редактировать объекты могут только из создатели.
        return obj.owner == request.user


