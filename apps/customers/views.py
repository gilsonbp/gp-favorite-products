from rest_framework import viewsets

from .models import Customer
from .permissions import AllowCreate
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [AllowCreate]
