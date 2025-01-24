from nicegui import ui
from datetime import datetime
from components.decorators import page_with_layout
from loguru import logger
def err_page():
    # 页面标题
    ui.label('404 - 页面未找到').classes('text-4xl font-bold text-red-500 mt-10')

    # 显示当前时间
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ui.label(f'当前时间: {current_time}').classes('text-lg text-gray-600 mt-4')

    # 提示信息
    ui.label('抱歉，您访问的页面不存在。').classes('text-xl text-gray-800 mt-6')

    # 返回首页的链接
    ui.link('返回首页', '/').classes('text-blue-500 hover:text-blue-700 mt-8')

    # 添加一个图片或图标（可选）
    ui.image('https://via.placeholder.com/150').classes('mt-10')

    # 记录日志
    logger.error(f'404 Error: Page not found at {datetime.now()}')
