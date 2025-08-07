import sys
from logger_setup import init_logger
from path_utils import recursive_directory_walk
from table_types import create_table
from table_registry import TableRegistry


class NoExcelFilesFound(Exception): pass


from pathlib import Path

if __name__ == "__main__":
    logger = init_logger()
    try:
        logger.info(f"Запуск {sys.argv[0]}")
        current_dir = Path(__file__).parent
        table_paths = recursive_directory_walk(current_dir / "data", ".xlsx")
        if len(table_paths) == 0:
            raise NoExcelFilesFound("Не найдено ни одной таблицы")
        logger.info(f"Найдено {len(table_paths)} таблиц")
        registry = TableRegistry()
        for filepath in table_paths:
            logger.debug(f"Проверка таблицы {filepath}")
            table = create_table(filepath)
            registry.register(table)
        registry.check()

    except Exception as exception:
        logger.error(exception)
