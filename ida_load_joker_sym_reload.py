import sys
for mod in sys.modules.keys():
    if 'import_sym' in mod:
        del sys.modules[mod]

import import_sym
import import_sym as imp

print 'Reloaded module as imp'
