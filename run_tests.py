# -*- coding: utf 8 -*-
"""
Run all the tests.

This is the same as doing this on the command line:

  py.test --mpl --cov jeepr

We have to run tests this way because we need to set the
matplotlib backend for travis.
"""
import pytest
import matplotlib
matplotlib.use('agg')

# To generate new images, uncomment this line and instead
# comment out the last one (below).
# pytest.main(["--mpl-generate-path=tests/baseline", "--cov", "jeepr"])

# To test as normal
pytest.main(["--mpl", "--cov", "jeepr"])
