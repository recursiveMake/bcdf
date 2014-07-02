#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bcdf.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
