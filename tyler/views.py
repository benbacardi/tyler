from .models import Map
from .forms import MapForm
from django.http import HttpResponse

import json

def get_image(request):

    map_form = MapForm(request.GET)
    if not map_form.is_valid():
        return HttpResponse(json.dumps(map_form.errors), mimetype='application/json', status=400)

    import StringIO
    output = StringIO.StringIO()

    Map(**map_form.cleaned_data).create(output)

    return HttpResponse(output.getvalue(), mimetype='image/png')