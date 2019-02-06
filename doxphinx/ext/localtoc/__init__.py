#
# __init__.py - localtoc module initialization
#
# Copyright (C) 2019 Angel Linares Zapater
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2, as
# published by the Free Software Foundation. See the COPYING file.
#
# This program is distributed WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#

from .localtoc import html_page_context

def setup(app):
    app.connect('html-page-context', html_page_context)
