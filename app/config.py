"""Application settings — pydantic-settings, backed by .env.

One Settings class (grouped sub-models if it grows). Inject via Depends /
a cached accessor; never read os.environ directly elsewhere in the app.
"""

# TODO(dev): Step 3 — hand-write the Settings class (BaseSettings) here.
