#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Patrik Kullman
# Copyright (c) 2015 Patrik Kullman
#
# License: MIT
#

"""This module exports the Polylint plugin class."""

from SublimeLinter.lint import NodeLinter, util


class Polylint(NodeLinter):

    """Provides an interface to polylint."""

    syntax = ('html')
    cmd = ('polylint', '--no-recursion', '--stdin', '-i', '@')
    executable = None
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r'^[^:]*:(?P<line>\d+):(?P<col>\d+)\r?\n\s*(?P<message>.+)$'
    multiline = True
    line_col_base = (1, 1)
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
