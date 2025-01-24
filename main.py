from __future__ import annotations
from loguru import logger
from nicegui import ui
import importlib
from pathlib import Path
from typing import Iterable, Callable
from pages.err import err_page
from components.decorators import page_with_layout


def auto_register_pages(
        pages_dir: Path = Path(__file__).parent / "pages",
        excludes: Iterable[str] = ("base_page.py",),
        page_predicate: Callable[[str], bool] = lambda x: x.endswith("_page")
) -> None:
    """自动路由注册解决方案

    Args:
        pages_dir: 页面目录路径
        excludes: 排除文件名集合
        page_predicate: 页面函数判断条件
    """
    exclude_set = {'__init__', *excludes}
    logger.info(f"开始自动注册页面，目录: {pages_dir}")

    for py_file in pages_dir.glob("*.py"):
        file_name = py_file.name
        logger.debug(f"处理文件: {file_name}")

        # 跳过隐藏文件和排除文件
        if file_name.startswith('_') or py_file.stem in exclude_set:
            logger.debug(f"跳过文件: {file_name} [排除规则匹配]")
            continue

        # 动态导入模块
        try:
            module = importlib.import_module(f"pages.{py_file.stem}")
            logger.success(f"模块加载成功: {py_file.stem}")
        except Exception as e:
            logger.error(f"模块加载失败: {py_file.stem} ({e})")
            continue

        # 注册页面路由
        registered = 0
        for name in dir(module):
            if page_predicate(name):
                obj = getattr(module, name)
                if callable(obj):
                    route_path = f"/{py_file.stem.replace('_page', '')}"
                    try:
                        ui.page(route_path)(obj)
                        logger.info(f"路由注册成功: {route_path} => {name}()")
                        registered += 1
                    except Exception as e:
                        logger.error(f"路由注册失败: {route_path} ({e})")
                else:
                    logger.warning(f"跳过非可调用对象: {name}")
        if not registered:
            logger.warning(f"模块中未找到有效页面: {py_file.stem}")


if __name__ == "__main__":
    logger.info("应用初始化...")
    auto_register_pages()


    @page_with_layout('/{_:path}')
    def catch_all():
        err_page()


    ui.run(
        title='我的应用',
        favicon='./icon.svg',
        reload=False
    )
    logger.success("应用启动完成")
