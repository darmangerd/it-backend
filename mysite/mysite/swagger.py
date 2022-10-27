from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from drf_yasg.inspectors import SwaggerAutoSchema

schema_view = get_schema_view(
    openapi.Info(
        title="mysite API",
        default_version="v1",
        description="API allowing to manage",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


class CustomAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        tags = self.overrides.get("tags", None) or getattr(self.view, "swagger_tag", [])
        if not tags:
            tags = [operation_keys[0]]

        return tags
