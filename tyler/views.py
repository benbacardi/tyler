from .models import Map
from .forms import MapForm

from django.http import HttpResponse
from django.core.cache import cache
from django.conf import settings

import json
import StringIO

def get_cache_key(request):
    keys = sorted(request.GET.keys())
    data = []
    for key in keys:
        data.append('%s=%s' % (key, request.GET[key]))
    return 'map:%s' % '&'.join(data)

def get_image(request):

    cache_key = get_cache_key(request)

    image_data = cache.get(cache_key)

    if not image_data:

        map_form = MapForm(request.GET)
        if not map_form.is_valid():
            return HttpResponse(json.dumps(map_form.errors), mimetype='application/json', status=400)

        output = StringIO.StringIO()
        Map(**map_form.cleaned_data).create(output)
        image_data = output.getvalue()

        cache.set(cache_key, image_data, getattr(settings, 'TYLER_CACHE_DURATION', 60 * 60 * 24 * 7))

    return HttpResponse(image_data, mimetype='image/png')