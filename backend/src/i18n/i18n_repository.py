from pathlib import Path
import json
from typing import Dict, Set, Tuple
from fastapi import HTTPException, status

from src.entity.models import User


def check_admin_rights(current_user: User):
    """Перевірка прав адміністратора"""
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied. Admin rights required"
        )


class I18nRepository:
    def __init__(self, languages_dir: Path = None):
        self.languages_dir = languages_dir or Path(__file__).parent.parent / "i18n" / "languages"
        self.languages_dir.mkdir(parents=True, exist_ok=True)

    def get_translations(self, language: str) -> dict:
        path = self.languages_dir / f"{language}.json"

        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            translations = json.load(f)
            return translations

    def save_translations(self, language: str, translations: dict):
        path = self.languages_dir / f"{language}.json"

        with open(path, "w", encoding="utf-8") as f:
            json.dump(translations, f, ensure_ascii=False, indent=2)

    def create_nested_translations(self, language: str, translations: Dict[str, str]) -> dict:
        existing = self.get_translations(language)

        for key, value in translations.items():
            parts = key.split('.')
            current = existing

            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]

            current[parts[-1]] = value

        self.save_translations(language, existing)
        return existing

    def update_translation(self, language: str, key: str, value: str) -> dict:
        translations = self.get_translations(language)
        parts = key.split('.')
        current = translations

        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]

        current[parts[-1]] = value
        self.save_translations(language, translations)
        return translations

    def delete_translation(self, language: str, key: str) -> bool:
        translations = self.get_translations(language)
        parts = key.split('.')
        current = translations

        for part in parts[:-1]:
            if part not in current:
                raise HTTPException(status_code=404, detail="Translation key not found")
            current = current[part]

        if parts[-1] not in current:
            raise HTTPException(status_code=404, detail="Translation key not found")

        del current[parts[-1]]
        self.save_translations(language, translations)
        return True

    def validate_translations(self) -> Tuple[bool, Dict[str, list]]:
        all_translations = {}
        all_keys: Set[str] = set()

        # Load all translations
        for file in self.languages_dir.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                all_translations[file.stem] = json.load(f)

        # Collect all keys
        def get_keys(d: dict, prefix="") -> Set[str]:
            keys = set()
            for k, v in d.items():
                full_key = f"{prefix}{k}" if not prefix else f"{prefix}.{k}"
                if isinstance(v, dict):
                    keys.update(get_keys(v, full_key + "."))
                else:
                    keys.add(full_key)
            return keys

        # Get all keys from all languages
        for translations in all_translations.values():
            all_keys.update(get_keys(translations))

        # Check for missing keys
        missing_keys = {}
        for lang, translations in all_translations.items():
            lang_keys = get_keys(translations)
            missing = all_keys - lang_keys
            if missing:
                missing_keys[lang] = list(missing)

        return not bool(missing_keys), missing_keys
