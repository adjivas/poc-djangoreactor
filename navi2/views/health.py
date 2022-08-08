from django.http import HttpRequest
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@api_view(("GET",))
@renderer_classes((JSONRenderer,))
def health(_: HttpRequest):
    """
    Simple readyness check endpoint.

    :param _: ignored request
    :return: basic health response
    """
    return Response(data={"alive": True}, status=200)
