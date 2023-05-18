    README - General description of the doxphinx project

    Copyright (C) 2018-2023 Angel Linares Zapater

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License, version 2, as
    published by the Free Software Foundation. See the COPYING file.

    This program is distributed WITHOUT ANY WARRANTY; without even the
    implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Getting started
===============

doxphinx is a theme for the Sphinx documentation system. The purpose of doxphinx
is to provide a single mechanism to generate the documentation of a project,
both in HTML and PDF formats, from a common source.

This common source of documentation consists of a set of text files written in
reStructuredText markup language along with a set of conventions for writing and
organizing the different files. The Sphinx tool can then be used to
automatically generate a HTML website or a PDF book, both from the same single
documentation source.

How to use
==========

In order to use doxphinx to document any project, just install it using:

  $ pip install doxphinx

Then create a directory for the documentation files and using the Sphinx tool:

  $ sphinx-quickstart

Initialize the directory as a Sphinx project and configure the conf.py file that
has been created, and you are ready to build the documentation using doxphinx.

See "The doxphinx Handbook" <https://docs.phyglos.org/doxphinx> to learn how to use
doxphinx in your documentation project.

At this point you can focus on the actual documentation work for your project.
Whenever the documentation is ready to be published or updated, use Sphinx to format
again the HTML website or the PDF book from the documentation source files.

Status
======

The doxphinx project is in STABLE status.

More information
================

The COPYING file contains the GNU License for this software.

The RELEASE file describes the main changes in this release.

See https://docs.phyglos.org/doxphinx for more information.
