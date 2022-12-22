mt940-writer
============

Python library to create bank statements in the MT940 format

Only Python 3.7+ is supported.

.. code-block:: shell

    pip install mt940-writer

Development
-----------

.. image:: https://github.com/ministryofjustice/mt940-writer/actions/workflows/test.yml/badge.svg?branch=main
    :target: https://github.com/ministryofjustice/mt940-writer/actions/workflows/test.yml

.. image:: https://github.com/ministryofjustice/mt940-writer/actions/workflows/lint.yml/badge.svg?branch=main
    :target: https://github.com/ministryofjustice/mt940-writer/actions/workflows/lint.yml

Please report bugs and open pull requests on `GitHub`_.

Use ``python setup.py test`` or ``tox`` to run all tests.

Distribute a new version by updating the ``VERSION`` tuple in ``mt940_writer.py`` and
publishing a release in GitHub (this triggers a GitHub Actions workflow to automatically upload it).
Alternatively, run ``python setup.py sdist bdist_wheel upload`` locally.

Copyright
---------

Copyright (C) 2022 HM Government (Ministry of Justice Digital & Technology).
See LICENSE.txt for further details.

.. _GitHub: https://github.com/ministryofjustice/mt940-writer
