from django import forms

class MapForm(forms.Form):
    lat = forms.FloatField(min_value=-90, max_value=90, required=False)
    lon = forms.FloatField(min_value=-180, max_value=180, required=False)
    zoom = forms.IntegerField(min_value=0, max_value=19, required=False)
    width = forms.IntegerField(min_value=1, max_value=3000, required=False)
    height = forms.IntegerField(min_value=1, max_value=3000, required=False)
    greyscale = forms.BooleanField(required=False)
    tile_url = forms.CharField(required=False)
    format = forms.CharField(required=False)

    def check(self, field, default):
        current = self.cleaned_data[field]
        if current is None or current == '':
            return default
        return current

    def clean_lat(self):
        return self.check('lat', 51.5008198)

    def clean_lon(self):
        return self.check('lon', -0.1427437)

    def clean_zoom(self):
        return self.check('zoom', 17)

    def clean_width(self):
        return self.check('width', 800)

    def clean_height(self):
        return self.check('height', 600)

    def clean_greyscale(self):
        return self.check('greyscale', False)

    def clean_format(self):
        return self.check('format', 'png')

    def clean_tile_url(self):
        return self.check('tile_url', 'http://[abc].tile.openstreetmap.org/{zoom}/{x}/{y}.png')
