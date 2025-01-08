from enum import Enum
from typing import Dict

from pydantic import BaseModel


class Language(str, Enum):
    UKRAINIAN = "uk"
    ENGLISH = "en"


class TranslationUpdate(BaseModel):
    key: str
    value: str


class TranslationCreate(BaseModel):
    translations: Dict[str, str]
