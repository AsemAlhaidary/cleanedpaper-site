from django.utils.translation import gettext as _

from typing import Dict, Any

DEFAULT_SETTINGS: Dict[str, Any] = {
    "logo": "CLEANEDPAPER",
    "title": _("Cleaned Paper Blog"),
    "meta_title": _("A blog for Cleaned Paper community"),
    "description": _("A blog concerned with publishing topics in various useful fields with the aim of sharing information and discussions"),
    "keywords": "CND, Blog, Technical, University, University Blog, Programming, Engineering, Communication, Network, Distribution",
    "created_at": "2023",
    "author": {
        "name": "Asem Alhaidary",
        "email": "asem@cleanedpaper.com",
    },
    "language": "ar",
    "url": "blog.cleanedpaper.com",
    "footer": _("All rights reserved."),
    "pages": {
        "home": {
            "title": _("Home"),
            "meta_title": _("Discover tons of interesting posts"),
            "description": _("From here you can start your journey in the blog and discover different of interesting posts"),
            "keywords": "CND, Blog, Technical, University, University Blog, Programming, Engineering, Communication, Network, Distribution",
            "language": "ar",
        },
        "archive": {
            "title": _("Archive"),
            "meta_title": _("Find all posts published in the blog"),
            "description": _("You can find a list of all posts have been published in the blog"),
            "keywords": "CND, Blog, Technical, University, University Blog, Programming, Engineering, Communication, Network, Distribution",
            "language": "ar",
        },
        "tags": {
            "title": _("Tags"),
            "meta_title": _("Find all tags in the blog"),
            "description": _("You can find a list of all tags in the blog"),
            "keywords": "CND, Blog, Technical, University, University Blog, Programming, Engineering, Communication, Network, Distribution",
            "language": "ar",
        }
    }
}

THEME_SETTINGS: Dict[str, Any] = {
    "color_palette": {
        "light": {
            "primary": "#F2F6FA",
            "secondary": "#FFFFFF",
            # "secondary": "#7DE9FF",
            "primary_text": "#136C94",
            "secondary_text": "#6B8487",
            "secondary_transparent": "#F9FBFCAA",
            "shadow": "#1C263955",
        },
        "dark": {
        },
        "general": {
            "accent": "#ff5c97",
            # "accent": "#28BCD5",
        }
    }
}
