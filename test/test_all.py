# #START_LICENSE###########################################################
#
#
# #END_LICENSE#############################################################

import unittest

from datasets import *
from test_tree import *
from test_seqgroup import *
from test_phylotree import *
from test_arraytable import *
try:
    import numpy
except ImportError: # case numpy is not installed
    pass
else:
    from test_clustertree import *
from test_r_bindings import *
from test_evol import *

if __name__ == '__main__':
    unittest.main()
