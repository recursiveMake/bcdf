#!/usr/bin/env python
import os
import sys

ON_OPENSHIFT = False
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True

if __name__ == "__main__":
    if ON_OPENSHIFT:
        sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi'))
    else:
        sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bcdf.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
