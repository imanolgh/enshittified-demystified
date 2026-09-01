"""Logging bootstrap. main.py calls setup_logging() before anything else.

Named logging_setup (not logging) to avoid shadowing the stdlib module.
Start with logging.basicConfig; grow into dictConfig only when needed.
"""

# TODO(dev): hand-write setup_logging() here.
