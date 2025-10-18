from .client.main_menu.main_menu import router as client_router
from .debug.states_data import router as debug_router
from .admin.menu import router as admin_router

list_routers = [
    admin_router,
    client_router,
    debug_router,
]