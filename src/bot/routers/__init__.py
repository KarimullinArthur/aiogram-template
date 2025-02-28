import os
import importlib.util


def recursive_import_routers(directory: str):
    routers = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                # Формируем путь к модулю
                module_path = os.path.join(root, file)
                module_name = os.path.relpath(module_path, directory).replace(os.sep, ".")[:-3]

                # Импортируем модуль
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Проверяем, есть ли объект router
                if hasattr(module, "router"):
                    routers[module_name] = getattr(module, "router")

    return routers


class RouterManager:
    def __init__(self, routers: dict):
        """
        Инициализирует RouterManager, добавляя роутеры как атрибуты.
        :param routers: Словарь {"имя_роутера": роутер}
        """
        self._routers = routers  # Сохраняем оригинальный словарь
        for name, router in routers.items():
            setattr(self, name, router)  # Создаем атрибуты для каждого роутера

    def _resolve_router_names(self, routers):
        """
        Преобразует входные данные (имена роутеров или объекты) в список имён.
        :param routers: Список или одиночный объект (имя или атрибут).
        :return: Список имён роутеров.
        """
        if routers is None:
            return []
        if not isinstance(routers, (list, set, tuple)):
            routers = [routers]
        resolved_names = []
        for router in routers:
            if isinstance(router, str):
                resolved_names.append(router)
            else:
                # Если передан объект, находим его имя в словаре
                for name, obj in self._routers.items():
                    if router is obj:
                        resolved_names.append(name)
                        break
        return resolved_names

    def get_all_except(self, exclude=None, as_list: bool = True):
        """
        Возвращает все роутеры, кроме указанных.
        :param exclude: Список имен или объектов роутеров, которые нужно исключить.
        :param as_list: Если True, возвращает список значений.
        :return: Словарь или список оставшихся роутеров.
        """
        exclude = self._resolve_router_names(exclude)
        result = {name: router for name, router in self._routers.items() if name not in exclude}
        return list(result.values()) if as_list else result

    def get_only(self, include=None, as_list: bool = True):
        """
        Возвращает только указанные роутеры.
        :param include: Список имен или объектов роутеров, которые нужно включить.
        :param as_list: Если True, возвращает список значений.
        :return: Словарь или список выбранных роутеров.
        """
        include = self._resolve_router_names(include)
        result = {name: router for name, router in self._routers.items() if name in include}
        return list(result.values()) if as_list else result


directory = "routers"
routers = recursive_import_routers(directory)
router_manager = RouterManager(routers)

for name, router in routers.items():
    print(f"Module: {name}, Router: {router}")
