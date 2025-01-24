from nicegui import ui
from functools import wraps
from .nav import create_nav  # 默认布局
from loguru import logger


def page_with_layout(path, layout=create_nav):
    def decorator(func):
        @ui.page(path)
        @wraps(func)
        async def wrapped(**kwargs):
            # 创建指定布局
            logger.info(f"为路径 {path} 创建 [{layout.__name__}] 布局")
            layout()

            # 执行页面函数
            logger.info(f"调用函数: {func.__name__}，参数: {kwargs}")
            result = func(**kwargs)
            logger.info(f"函数 {func.__name__} 返回: {result}")
            return result

        return wrapped

    return decorator