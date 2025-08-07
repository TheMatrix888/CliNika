from typing import List, Optional
from table_types import (
    Table,
    DailyCashTable,
    DailyNonCashTable,
    CurrentAccountTable,
    MedicinesInventoryTable,
    PetFoodInventoryTable,
    UnknownTable,
)


class UnknownTableError(Exception): pass


class DuplicateTableError(Exception): pass


class NoDailyTablesError(Exception): pass


class TableRegistry:
    def __init__(self):
        self.daily_cash: List[DailyCashTable] = []
        self.daily_noncash: List[DailyNonCashTable] = []
        self.current_account: Optional[CurrentAccountTable] = None
        self.medicines: Optional[MedicinesInventoryTable] = None
        self.pet_food: Optional[PetFoodInventoryTable] = None

    def register(self, table: Table):
        table_path = table.table_path
        if isinstance(table, UnknownTable):
            raise UnknownTableError(f"Неизвестная таблица: {table_path}")
        elif isinstance(table, DailyCashTable):
            self.daily_cash.append(table)
        elif isinstance(table, DailyNonCashTable):
            self.daily_noncash.append(table)
        elif isinstance(table, CurrentAccountTable):
            if self.current_account:
                raise DuplicateTableError(f"Найден дубликат таблицы \"расчётный счёт\" {table_path}")
            self.current_account = table
        elif isinstance(table, MedicinesInventoryTable):
            if self.medicines:
                raise DuplicateTableError("Найден дубликат таблицы \"препараты наличие\"")
            self.medicines = table
        elif isinstance(table, PetFoodInventoryTable):
            if self.pet_food:
                raise DuplicateTableError("Найден дубликат таблицы \"корма наличие\"")
            self.pet_food = table

    def check(self):
        if len(self.daily_cash) == 0:
            raise NoDailyTablesError("Не найдено ни одной таблицы НАЛ")
        if len(self.daily_noncash) == 0:
            raise NoDailyTablesError("Не найдено ни одной таблицы БЕЗНАЛ")
