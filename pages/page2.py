from nicegui import ui
from datetime import datetime
from components.decorators import page_with_layout
from loguru import logger


@page_with_layout('/page2')
def page2_page():
    logger.info("进入 page2 页面")
    ui.label('示例页面 2').classes('text-2xl font-bold text-center w-full')

    with ui.row().classes('mx-auto'):
        ui.timer(1.0, lambda: ui.notify('定时通知', type='positive'))
        ui.label('这个页面有个每秒触发的定时器').classes('text-lg')

    with ui.column().classes('items-center gap-4'):
        ui.toggle({1: '选项A', 2: '选项B', 3: '选项C'}).props('outline')
        ui.upload(on_upload=lambda e: ui.notify(f'上传了文件: {e.name}'))

    logger.info("page2 页面初始化完成")
