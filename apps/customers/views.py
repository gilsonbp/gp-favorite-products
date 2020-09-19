from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer
from .permissions import AllowCreate
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [AllowCreate]

    @action(methods=["get"], detail=False, url_path="me", url_name="me")
    def me(self, request):
        customer = self.get_object()
        serializer = self.get_serializer(customer)
        return Response(serializer.data)

    def get_object(self):
        return self.request.user
