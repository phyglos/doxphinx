#
# __init__.py - doxphinx module initialization
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

from os import path

def setup(app):
    app.add_html_theme('doxphinx', path.abspath(path.dirname(__file__)))
