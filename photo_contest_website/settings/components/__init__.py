from pathlib import Path

from decouple import AutoConfig
from decouple import Csv


BASE_DIR = Path(__file__).parent.parent.parent

config = AutoConfig(search_path=BASE_DIR)
