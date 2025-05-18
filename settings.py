import os
DEBUG_MODE = os.environ.get("DEBUG_MODE", True)
DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+asyncpg://root:root@localhost:5432/sensordb")
