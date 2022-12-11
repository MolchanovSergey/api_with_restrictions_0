from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(f'IsOwnerOrReadOnly: , request.user= {request.user}, obj.creator={ obj.creator}')
        if request.method == 'GET':
            #Просмотр всех объявлений
            return True
        #Менять и создавать может только автор
        return request.user == obj.creator
