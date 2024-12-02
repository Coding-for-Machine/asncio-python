
import asyncio
from typing import Dict, Any, Callable, Union, List

class AsyncValidator:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.errors = {}

    async def validate_field(self, field: str, rule: Union[Callable, List[Callable]]):
        """ Validatsiya qoidalarini bitta maydon uchun bajaradi. """
        try:
            if isinstance(rule, list):
                for r in rule:
                    self.data[field] = await r(self.data.get(field))
            else:
                self.data[field] = await rule(self.data.get(field))
        except Exception as e:
            self.errors[field] = self.errors.get(field, []) + [str(e)]

    async def validate(self, rules: Dict[str, Union[Callable, List[Callable]]]):
        """ Barcha maydonlar uchun validatsiya qoidalari. """
        tasks = [self.validate_field(field, rule) for field, rule in rules.items()]
        await asyncio.gather(*tasks)
        if self.errors:
            raise ValueError({"validation_errors": self.errors})
        return self.data

    def add_error(self, field: str, message: str):
        """ Xatolik qo'shish yordamchi funksiyasi. """
        self.errors[field] = self.errors.get(field, []) + [message]

    async def validate_nested(self, rules: Dict[str, Union[Callable, List[Callable]]], parent_key: str = ""):
        """ Ichma-ich (nested) validatsiya qoidalari. """
        for field, rule in rules.items():
            full_key = f"{parent_key}.{field}" if parent_key else field
            if isinstance(rule, dict):  # Agar qoidalar ichma-ich bo'lsa
                await self.validate_nested(rule, full_key)  # Rekursiv chaqirish
            else:
                await self.validate_field(full_key, rule)


async def validate_username(value):
    if not value or len(value) < 3:
        raise ValueError("Username must be at least 3 characters long")
    return value
async def validate_username_max(value):
    if not value or len(value) > 10:
        raise ValueError("Username must be at least 10 characters long")
    return value

async def validate_email(value):
    if "@" not in value:
        raise ValueError("Invalid email address")
    return value

async def validate_street(value):
    if not value:
        raise ValueError("Street name cannot be empty")
    return value

async def validate_city(value):
    if not value or len(value) < 2:
        raise ValueError("City name must be at least 2 characters long")
    return value
