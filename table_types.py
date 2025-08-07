from pathlib import Path
from path_utils import resolve_filename, resolve_filedate
from filename_aliases import FILENAME_ALIASES

# TODO ВОТ ТУТ НУЖНО УКАЗАТЬ ВСЮ ЛОГИКУ

class Table:
    def __init__(self, table_path: Path, name: str):
        self.table_path = table_path
        self.name = name


class UnknownTable(Table):
    def __init__(self, table_path: Path, name: str):
        super().__init__(table_path, name)


class DailyCashTable(Table):
    def __init__(self, table_path: Path, name: str):
        super().__init__(table_path, name)


class DailyNonCashTable(Table):
    def __init__(self, table_path: Path, name: str):
        super().__init__(table_path, name)


class CurrentAccountTable(Table):
    def __init__(self, table_path: Path, name: str):
        super().__init__(table_path, name)


class MedicinesInventoryTable(Table):
    def __init__(self, table_path: Path, name: str):
        super().__init__(table_path, name)


class PetFoodInventoryTable(Table):
    def __init__(self, table_path: Path, name: str):
        super().__init__(table_path, name)

TABLE_NAMES = {
    "daily_cash": DailyCashTable,
    "daily_noncash": DailyNonCashTable,
    "current_account": CurrentAccountTable,
    "medicines_inventory": MedicinesInventoryTable,
    "pet_food_inventory": PetFoodInventoryTable
}

def create_table(table_path: Path) -> Table:
    name = resolve_filename(table_path)
    if name not in TABLE_NAMES:
        return UnknownTable(table_path, name)
    else:
        return TABLE_NAMES[name](table_path, name)
