# import os
# import sys
# import inspect
# import importlib.util
# 
# 
# routers = []
# path = os.path.dirname(__file__) + '/'
# 
# 
# def import_from_path(module_name, file_path):
#     spec = importlib.util.spec_from_file_location(module_name, file_path)
#     module = importlib.util.module_from_spec(spec)
#     sys.modules[module_name] = module
#     spec.loader.exec_module(module)
#     return module
# 
# 
# def get_modules(postfix_path: str = ''):
# #     path = os.path.dirname(__file__) + '/' + postfix_path
#     ls = os.popen(f"ls {postfix_path}").read()[:-1].split("\n")
#     try:
#         ls.remove("__pycache__")
#         ls.remove("__init__.py")
#     except ValueError:
#         pass
# 
#     for module in routers:
#         try:
#             class_module = sys.modules[module.__class__.__module__]
#             class_path = inspect.getfile(class_module)
#             if postfix_path == class_path:
#                 ls.remove(f"{module.__name__}.py")
#         except ValueError:
#             pass
# 
#     return ls
# 
# 
# 
# # while get_modules(sub_module)[0] != '':
# # while True:
# #     for module in get_modules():
# #         if module[-3:] != ".py":
# #             for sub_module in get_modules(module):
# #                 print(module)
# #                 print(sub_module)
# #                 path_module =  path + module + '/' + sub_module
# #                 print(path_module)
# #                 routers.append(import_from_path(sub_module[:-3], path_module).router)
# #                 get_modules()
# #         else:
# #             routers.append(import_from_path(module[:-3], path + module).router)
# #         print(routers)
# #         break
# #     break
# 
# def load_modules(path):
#     for module in get_modules(path):
#         if module[-3:] != ".py":
#             print(module)
#             for sub_module in get_modules(module):
#                 path_submodule =  path + module + '/' + sub_module
#                 if sub_module[-3:] != ".py":
#                     load_modules(path_submodule)
#                     break
#                 else:
#                     routers.append(import_from_path(sub_module[:-3], path_submodule).router)
# #                 path_module = '/'.join(path_submodule.split('/')[:-1])
#         if module == '':
#             return
#         else:
#             routers.append(import_from_path(module[:-3], path + "/" + module).router)
# load_modules(path)


# import os
# import importlib.util
# 
# def recursive_import_routers(directory: str):
#     routers = []
# 
#     for root, _, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".py") and not file.startswith("__"):
#                 # Формируем путь к модулю
#                 module_path = os.path.join(root, file)
#                 module_name = os.path.relpath(module_path, directory).replace(os.sep, ".")[:-3]
#                 
#                 # Импортируем модуль
#                 spec = importlib.util.spec_from_file_location(module_name, module_path)
#                 module = importlib.util.module_from_spec(spec)
#                 spec.loader.exec_module(module)
#                 
#                 # Проверяем, есть ли объект router
#                 if hasattr(module, "router"):
#                     routers.append(getattr(module, "router"))
#     
#     return routers
# 
# # Пример использования
# directory = "routers"  # Путь к директории с роутерами
# routers = recursive_import_routers(directory)
# for router in routers:
#     print(router)


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
