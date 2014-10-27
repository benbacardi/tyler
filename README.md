Tyler
=====

Python webservice for tiling static maps.

[![Build Status Badge](https://travis-ci.org/benbacardi/tyler.png?branch=master)](https://travis-ci.org/benbacardi/tyler)
[![Code Health Badge](https://landscape.io/github/benbacardi/tyler/master/landscape.png)](https://landscape.io/github/benbacardi/tyler)
[![Version Badge](https://pypip.in/v/tyler/badge.png)][pypi]
[![Downloads Badge](https://pypip.in/d/tyler/badge.png)][pypi]
[![Wheel Status Badge](https://pypip.in/wheel/tyler/badge.png)][pypi]
[![License Badge](https://pypip.in/license/tyler/badge.png)][pypi]

[pypi]: https://pypi.python.org/pypi/tyler/

Demo
----

A demo can be found at https://tyler-demo.herokuapp.com - the Heroku project code is at https://github.com/benbacardi/tyler-heroku

[![Usage example](https://tyler-demo.herokuapp.com/?greyscale=False&lat=51.5132&lon=-0.1032&zoom=11&width=800&height=400&tile_url=http://[abcd].tile.stamen.com/watercolor/{zoom}/{x}/{y}.jpg "Usage example")](https://tyler-demo.herokuapp.com/?greyscale=False&lat=51.5132&lon=-0.1032&zoom=11&width=800&height=400&tile_url=http://[abcd].tile.stamen.com/watercolor/{zoom}/{x}/{y}.jpg)

Installation
------------

Tyler is designed to be deployed in your own Django environment.

* Add `cacheback` and `tyler` to your `INSTALLED_APPS` setting.
* Add `tyler.urls` to your `urls.py`:

```python
urlpatterns = patterns('',
    url(r'^', include('tyler.urls')),
)
```

* Optionally, set `TYLER_CACHE_DURATION` to cache . It defaults to one week.

Usage
-----

To use the service, call the URL with optional parameters to return the image in a `.png` format:

```
GET /?lat=51.5008198&lon=-0.1427437&width=800&height=600
```

The available parameters are:

* **lat**: The latitude to center the map on.
* **lon**: The longitude to center the map on.
* **zoom**: The zoom level (`0` to `19`). Defaults to `17`.
* **width**: The pixel width of the resulting image. Defaults to `800`.
* **height**: The pixel height of the resulting image. Defaults to `600`.
* **greyscale**: Whether to render the image in greyscale. Defaults to `False`.
* **tile_url**: The URL of the tiling service. Defaults to OpenStreetMap's: `http://[abc].tile.openstreetmap.org/{zoom}/{x}/{y}.png`. Requires the following parameters in the URL:
  * **{zoom}**: Where the zoom level is defined.
  * **{x}**: The x-tile coordinate.
  * **{y}**: The y-tile coordinate.
  * **[???]**: Available content sharding domains. For example, OpenStreetMap uses `[abc]`. MapQuest uses `[1234]`.

Caching
-------

To control the caching of the resultant image, set `TYLER_CACHE_DURATION` in `settings.py` to the number of seconds to cache for. This defaults to one week.

To control the caching of the individual tiles used to create the image, set `TYLER_TILE_CACHE_DURATION` in `settings.py` to the number of settings to cache for. This also defaults to one week.
