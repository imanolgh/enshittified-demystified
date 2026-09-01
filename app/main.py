"""App factory. Order matters:

1. setup_logging()  (app.logging_setup)
2. load Settings    (app.config)
3. app = FastAPI(...)
4. app.include_router(...) for each router module in app/api/
"""

# TODO(dev): Step 3 — hand-write the app factory here.
