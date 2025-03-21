from pathlib import Path

LINUX_PATH = Path(__file__).parent.parent.absolute() / "linux-4.14"

assert LINUX_PATH.exists(), f"Path {LINUX_PATH} does not exist"
LINUX_PATH = LINUX_PATH.as_posix()

# DATABASE_CONFIG = {
#     "host": "127.0.0.1",
#     "database": "ubidb1",
#     "user": "ubiuser1",
#     "password": "ubitect",
# }

DB_CONFIG = "postgresql://ubiuser1:ubitect@db:5432/ubidb1"

EVAL_SAMPLING_TABLE = "case_sampling"
EVAL_RES_TABLE = "sampling_res"
