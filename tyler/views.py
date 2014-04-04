from .models import Map
from .forms import MapForm

from cacheback.decorators import cacheback

from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.conf import settings

import json
from PIL import Image
import StringIO

@cacheback(getattr(settings, 'TYLER_CACHE_DURATION', 60 * 60 * 24 * 7))
def cached_get_image(**kwargs):
    output = StringIO.StringIO()
    Map(**kwargs).create(output)
    return output.getvalue()

def get_image(request):

    map_form = MapForm(request.GET)
    if not map_form.is_valid():
        return HttpResponse(json.dumps(map_form.errors), mimetype='application/json', status=400)

    image_data = cached_get_image(**map_form.cleaned_data)

    format = map_form.cleaned_data['format'].upper()
    if format not in Image.MIME:
        raise ValidationError("Unsupported format: %s" % format)
    return HttpResponse(image_data, mimetype=Image.MIME[format])
