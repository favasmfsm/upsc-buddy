from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAcademyAdminOrSuperuser
from .serializers import AcademyBrandingSerializer, AcademyBrandingUpdateSerializer
from .utils import require_academy


class CurrentAcademyView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        academy = require_academy(request)
        return Response(
            AcademyBrandingSerializer(academy, context={"request": request}).data
        )


class AcademyBrandingView(APIView):
    permission_classes = [IsAuthenticated, IsAcademyAdminOrSuperuser]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get(self, request):
        academy = require_academy(request)
        return Response(
            AcademyBrandingSerializer(academy, context={"request": request}).data
        )

    def patch(self, request):
        academy = require_academy(request)
        serializer = AcademyBrandingUpdateSerializer(
            academy,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            AcademyBrandingSerializer(academy, context={"request": request}).data
        )
