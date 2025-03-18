from typing import Dict, Tuple

from src.i18n.i18n_repository import I18nRepository


class I18nService:
    def __init__(self, repository: I18nRepository):
        self.repository = repository

    async def get_translations(self, language: str) -> dict:
        return self.repository.get_translations(language)

    async def create_translations(self, language: str, translations: Dict[str, str]) -> dict:
        return self.repository.create_nested_translations(language, translations)

    async def update_translation(self, language: str, key: str, value: str) -> dict:
        return self.repository.update_translation(language, key, value)

    async def delete_translation(self, language: str, key: str) -> bool:
        return self.repository.delete_translation(language, key)

    async def validate_translations(self) -> Tuple[bool, Dict[str, list]]:
        return self.repository.validate_translations()