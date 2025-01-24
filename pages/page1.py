from nicegui import ui
from datetime import datetime
from components.decorators import page_with_layout
from loguru import logger

@page_with_layout('/page1')
def page1_page():
    logger.info("页面1加载开始")

    ui.label('示例页面 1').classes('text-2xl font-bold text-center w-full')
    logger.debug("显示示例页面1标签")

    # 使用进度条替代图表
    progress = ui.linear_progress(value=0.5).classes('w-64 mx-auto')
    logger.debug("显示进度条，值为50%")
    ui.label('进度条示例（50%）').classes('text-center')

    # 添加时间显示
    time_label = ui.label().classes('text-xl text-center')
    logger.debug("初始化时间标签")

    def update_time():
        current_time = datetime.now().strftime("%H:%M:%S")
        time_label.text = f'当前时间: {current_time}'
        logger.debug(f"更新时间标签: {current_time}")

    ui.timer(1.0, update_time)
    logger.info("页面1加载完成")
