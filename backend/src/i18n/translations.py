import json
from pathlib import Path
from typing import Dict, Optional
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class I18nMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, default_language: str = "uk"):
        super().__init__(app)
        self.default_language = default_language
        self.translations: Dict[str, Dict] = {}
        self._load_translations()

    def _load_translations(self):
        """Load all translation files from i18n directory"""
        i18n_dir = Path(__file__).parent / "languages"

        for file in i18n_dir.glob("*.json"):
            if file.stem in ["uk", "en"]:
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        self.translations[file.stem] = json.load(f)
                except Exception as e:
                    print(f"Error loading translation file {file}: {str(e)}")

    async def dispatch(self, request: Request, call_next):
        language = self._get_language(request)
        request.state.language = language
        translations = self.translations.get(language, self.translations.get(self.default_language, {}))
        request.state.translations = translations

        response = await call_next(request)
        return response

    def _get_language(self, request: Request) -> str:
        lang_query = request.query_params.get("lang")

        if lang_query and lang_query in self.translations:
            return lang_query

        accept_language = request.headers.get("accept-language")

        if accept_language:
            langs = accept_language.split(",")
            for lang in langs:
                lang_code = lang.split(";")[0].strip().lower()
                if lang_code in self.translations:
                    return lang_code

        return self.default_language


def get_language(request: Request) -> str:
    return request.state.language


def get_translator(request: Request):
    translations = getattr(request.state, "translations", {})

    def translate(key: str, params: Optional[Dict] = None) -> str:
        parts = key.split('.')
        value = translations

        for part in parts:
            if isinstance(value, dict):
                value = value.get(part, key)
            else:
                return key

        if not isinstance(value, str):
            return key

        if params:
            try:
                return value.format(**params)
            except KeyError:
                return value
        return value

    return translate


async def translator(request: Request):
    return get_translator(request)
