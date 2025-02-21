from rest_framework import permissions

class isOwner(permissions.BasePermission):
    #Permiso que permite modificar o eliminar solo si el usuario es el creador de la tarea.

    def has_object_permission(self, request, view, obj):
        # Permitir lectura para cualquier solicitud
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permitir modificación/eliminación solo si el usuario es el propietario
        return obj.user == request.user