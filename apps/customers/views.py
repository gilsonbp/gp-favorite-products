from rest_framework import viewsets

from .models import Customer
from .permissions import AllowCreate
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [AllowCreate]
    pagination_class = None

    def get_queryset(self):
        qs = super(CustomerViewSet, self).get_queryset()
        return qs.filter(pk=self.request.user.pk)
