from enum import Enum

from decouple import config


class FileExtension(Enum):
    LOGO = config("LOGO_FILE_EXTENSION")
