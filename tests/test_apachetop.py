#!/usr/bin/env python
import sys
sys.path.insert(0, '../')
from apachetop import *

    
tool = ApacheStatusTool()

tool.parse_options()

host = 'localhost:10080'

try:
    tool.procs = tool.filter_procs(
        tool.parse_live_status('http://localhost:10080/server-status')
    )
except IOError:
    sys.stderr.write("Failed to read from %s\n" % (tool.options.host,))
    sys.exit(1)

if len(tool.procs) < tool.options.minprocs:
    if sys.stdout.isatty():
        sys.exit("Number of active Apache procs (%d) is less than --minprocs (%d), quitting" %
                 (len(tool.procs), tool.options.minprocs))
    else:
        sys.exit(0)

if not tool.options.quiet:
    tool.display()

if tool.options.kill:
    tool.control()