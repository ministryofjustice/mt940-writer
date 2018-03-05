mt940-writer
============

Python library to create bank statements in the MT940 format

.. code-block:: bash

    pip install mt940-writer

Development
-----------

.. image:: https://travis-ci.org/ministryofjustice/mt940-writer.svg?branch=master
    :target: https://travis-ci.org/ministryofjustice/mt940-writer

Please report bugs and open pull requests on `GitHub`_.

Use ``python setup.py test`` or ``tox`` to run all tests.

Distribute a new version by updating the ``version`` argument in ``setup.py:setup`` and run ``python setup.py sdist bdist_wheel upload``.

Copyright
---------

Copyright (C) 2018 HM Government (Ministry of Justice Digital Services).
See LICENSE.txt for further details.

.. _GitHub: https://github.com/ministryofjustice/mt940-writer
