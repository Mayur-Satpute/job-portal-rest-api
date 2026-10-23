from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Company
from .permissions import IsRecruiter
from .serializers import CompanySerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.select_related("created_by").all()
    serializer_class = CompanySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated(), IsRecruiter()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
