#!/usr/bin/env python
import os
import sys

ON_AWS = False
if os.environ.has_key('AWS'):
    ON_AWS = True

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bcdf.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
