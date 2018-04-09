#!/usr/bin/env python
import os
import sys
# for generate secret_key.
import json
import string, random

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "esl_chain.settings")

    # SECRTET_KEY Generate added by GeunYoung Lim 2018. 04. 08.
    if not os.path.isfile('secret.json') :
        secrets = {}
        chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')
        secrets['SECRET_KEY'] = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

        with open('secrets.json', 'w') as outfile:
            json.dump(secrets, outfile, indent=4)

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
