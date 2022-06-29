from enum import Enum

from decouple import config


class FileExtension(Enum):
    logo = config("LOGO_FILE_EXTENSION")
