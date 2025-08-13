import asyncio
from camoufox.async_api import AsyncCamoufox
from camoufox import DefaultAddons

config = {
    # Navigator
    "navigator.userAgent": (
        "Mozilla/5.0 (Linux; Android 13; Pixel 9) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Mobile Safari/537.36"
    ),
    "navigator.doNotTrack": "0",
    "navigator.appCodeName": "Mozilla",
    "navigator.appName": "Netscape",
    "navigator.appVersion": "5.0 (Android)",
    "navigator.oscpu": "Android 13; Pixel 9",
    "navigator.language": "en-US",
    "navigator.languages": ["en-US", "en"],
    "navigator.platform": "Linux armv8l",
    "navigator.hardwareConcurrency": 6,
    "navigator.product": "Gecko",
    "navigator.productSub": "20030107",
    "navigator.maxTouchPoints": 5,
    "navigator.cookieEnabled": True,
    "navigator.globalPrivacyControl": False,
    "navigator.buildID": "20250801",
    "navigator.onLine": True,

    # Cursor
    "humanize": True,
    "humanize:maxTime": 1.5,
    "humanize:minTime": 0.5,
    "showcursor": False,

    # Screen
    "screen.availHeight": 732,     # approx. usable height (excluding browser chrome)
    "screen.availWidth": 412,      # approx. usable width
    "screen.availTop": 0,
    "screen.availLeft": 0,
    "screen.height": 600,          # full device screen height
    "screen.width": 412,           # full device screen width
    "screen.colorDepth": 24,
    "screen.pageXOffset": 0.0,
    "screen.pageYOffset": 0.0,

    # Fonts
    "fonts": [],
    "fonts:spacing_seed": 1,

    # Window
    "window.scrollMinX": 0,           # Minimum horizontal scroll offset
    "window.scrollMinY": 0,           # Minimum vertical scroll offset
    "window.scrollMaxX": 0,           # Max horizontal scroll offset (no overscroll)
    "window.scrollMaxY": 0,           # Max vertical scroll offset
    "window.outerHeight": 600,       # Total outer height in pixels
    "window.outerWidth": 412,        # Total outer width in pixels
    "window.innerHeight": 600,       # Viewport height
    "window.innerWidth": 412,        # Viewport width
    "window.screenX": 0,              # Horizontal distance from left border
    "window.screenY": 0,              # Vertical distance from top border
    "window.history.length": 1,       # Single entry in session history
    "window.devicePixelRatio": 2.6,   # Pixel ratio matching screen config

    # Canvas
    "canvas:aaOffset": 0,
    "canvas:aaCapOffset": True,

    # Webgl
    "webGl:vendor": "Google Inc.",
    "webGl:renderer": "ANGLE (Google, SwiftShader)",
    "webGl:supportedExtensions": [
        "ANGLE_instanced_arrays",
        "EXT_color_buffer_float",
        "EXT_disjoint_timer_query"
    ],
    "webGl2:supportedExtensions": [
        "ANGLE_instanced_arrays",
        "EXT_color_buffer_float",
        "EXT_disjoint_timer_query"
    ],
    "webGl:contextAttributes": {
        "alpha": True,
        "antialias": True,
        "depth": True
    },
    "webGl2:contextAttributes": {
        "alpha": True,
        "antialias": True,
        "depth": True
    },
    "webGl:parameters": {
        "2849": 1,     # MAX_TEXTURE_IMAGE_UNITS
        "2884": False, # DEPTH_TEST enabled flag
        "2928": [0, 1] # SAMPLE_BUFFERS list
    },
    "webGl2:parameters": {
        "2849": 1,
        "2884": False,
        "2928": [0, 1]
    },
    "webGl:parameters:blockIfNotDefined": False,
    "webGl2:parameters:blockIfNotDefined": False,
    "webGl:shaderPrecisionFormats": {
        "35633,36336": {"rangeMin": 127, "rangeMax": 127, "precision": 23}
    },
    "webGl2:shaderPrecisionFormats": {
        "35633,36336": {"rangeMin": 127, "rangeMax": 127, "precision": 23}
    },
    "webGl:shaderPrecisionFormats:blockIfNotDefined": False,
    "webGl2:shaderPrecisionFormats:blockIfNotDefined": False,

    # Geolocation
    "geolocation:latitude": 37.4219983,
    "geolocation:longitude": -122.084,
    "geolocation:accuracy": 30.0,       # in meters
    "timezone": "America/Los_Angeles",  # timezone identifier
    "locale:language": "en",
    "locale:region": "US",
    # "locale:script": "Latn", Automatically passed by Camoufox
    "locale:all": "en-US, en",

    # WebRTC
    "webrtc:ipv4": "127.0.0.1",
    "webrtc:ipv6": "::1",

    # Media
    "mediaDevices:enabled": True,
    "mediaDevices:micros": 1,
    "mediaDevices:webcams": 0,
    "mediaDevices:speakers": 1,

    # Audio
    "AudioContext:sampleRate": 48000,
    "AudioContext:outputLatency": 0.05,
    "AudioContext:maxChannelCount": 2,

    # Voices
    "voices": [
        {
            "isLocalService": True,
            "isDefault": True,
            "voiceUri": "en-US-Standard-B",
            "name": "en-US-Standard-B",
            "lang": "en-US"
        }
    ],
    "voices:blockIfNotDefined": False,
    "voices:fakeCompletion": False,
    "voices:fakeCompletion:charsPerSecond": 12.5,

    # Battery
    "pdfViewerEnabled": True,
    "battery:charging": True,
    "battery:chargingTime": 0.0,
    "battery:dischargingTime": 1800.0,
    "battery:level": 0.85,
}


async def main():
    async with AsyncCamoufox(
        i_know_what_im_doing=True,
        # headless=True,
        # addons=['/path/to/addon', '/path/to/addon2'],
        # exclude_addons=[DefaultAddons.UBO],
        main_world_eval=True,
        enable_cache=True,
        # persistent_context=True,
        # user_data_dir='/path/to/profile/dir',
        # geoip=True,
        # proxy={
        #     'server': 'http://example.com:8080',
        #     'username': 'username',
        #     'password': 'password'
        # },
        config=config,
    ) as browser:
        page = await browser.new_page()
        await page.goto("https://abrahamjuliot.github.io/creepjs/tests/fonts.html")
        await page.wait_for_timeout(5000)
        input("Press Enter to exit...")


if __name__ == "__main__":
    asyncio.run(main())
