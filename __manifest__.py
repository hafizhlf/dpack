{
    "name": "Simple Barcode Scanner",
    "version": "17.0.1.0.0",
    "summary": "Basic barcode scanning functionality",
    "description": """
        This module adds a simple barcode scanning feature 
        that can be used in inventory, POS, or custom modules.
    """,
    "category": "Tools",
    "author": "Hafizh Ibnu Syam",
    "website": "https://hafizhibnusyam.my.id",
    "license": "LGPL-3",
    "depends": ["base", "web", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_adjustment_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "dragon_custom/static/src/js/barcode_scanner.js",
            "dragon_custom/static/src/xml/barcode_scanner.xml",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False,
}
