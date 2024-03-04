"""
Модуль содержит файлы с настройками проекта,
расщепленные по компонентам
"""

from pathlib import Path

from decouple import AutoConfig, Csv

BASE_DIR = Path(__file__).parent.parent.parent

config = AutoConfig(search_path=BASE_DIR)
