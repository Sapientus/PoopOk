from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.entity.models import User
from src.i18n.i18n_repository import I18nRepository, check_admin_rights
from src.i18n.i18n_service import I18nService
from src.i18n.i18n_schema import TranslationCreate, TranslationUpdate, Language
from src.services.auth import auth_service

router = APIRouter(prefix="/i18n", tags=["i18n"])


async def get_i18n_service():
    repository = I18nRepository()
    return I18nService(repository)


@router.post("/validate")
async def validate_translations(
        service: I18nService = Depends(get_i18n_service),
        current_user: User = Depends(auth_service.get_current_user),
):
    """Завантажити всі переклади.

    Зібрати всі ключі з усіх мов.

    Перевірити, чи всі ключі присутні в кожній мові.

    Повернути результат перевірки.

    """
    check_admin_rights(current_user)
    is_valid, missing_keys = await service.validate_translations()
    return {
        "valid": is_valid,
        "missing_keys": missing_keys
    }


@router.get("/{language}")
async def get_translations(
        language: Language,
        current_user: User = Depends(auth_service.get_current_user),
        service: I18nService = Depends(get_i18n_service)
):
    """Отримати вибраний переклад"""
    check_admin_rights(current_user)
    language_value = language.value

    translations = await service.get_translations(language_value)
    return {"translations": translations}


@router.post("/{language}")
async def create_translations(
        language: Language,
        data: TranslationCreate,
        service: I18nService = Depends(get_i18n_service),
        current_user: User = Depends(auth_service.get_current_user),
        db: AsyncSession = Depends(get_db)
):
    """Вложені ключі пишемо через роздільник '.' (крапка)
        по типу key1.key2.key3.key4 etc. Зайві ключі без потреби можна просто видалити -> 'additionalProp' """
    check_admin_rights(current_user)
    language_value = language.value
    translations = await service.create_translations(language_value, data.translations)
    return {"message": "Translations created successfully"}


@router.put("/{language}")
async def update_translation(
        language: Language,
        data: TranslationUpdate,
        service: I18nService = Depends(get_i18n_service),
        current_user: User = Depends(auth_service.get_current_user),
):
    """Вложені ключі пишемо через роздільник '.' (крапка)
    по типу key1.key2.key3.key4 etc."""
    check_admin_rights(current_user)
    language_value = language.value
    await service.update_translation(language_value, data.key, data.value)
    return {"message": "Translation updated successfully"}


@router.delete("/{language}/{key}")
async def delete_translation(
        language: Language,
        key: str,
        service: I18nService = Depends(get_i18n_service),
        current_user: User = Depends(auth_service.get_current_user),
):
    """Видаляємо по ключу"""
    check_admin_rights(current_user)
    language_value = language.value
    await service.delete_translation(language_value, key)
    return {"message": "Translation deleted successfully"}
