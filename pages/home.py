from nicegui import ui
from components.decorators import page_with_layout
from loguru import logger

@page_with_layout('/')
def home_page():
    logger.info("首页加载")  # 页面加载时记录日志
    ui.label('NiceGUI 布局示例').classes('text-3xl font-bold text-center w-full')
    with ui.row().classes('justify-center'):
        text_input = ui.input(label='姓名', placeholder='请输入您的姓名').classes('w-64')
        ui.label('年龄').classes('text-center')
        slider = ui.slider(min=0, max=100, step=1, value=50).classes('w-64')

    with ui.column().classes('justify-end'):
        ui.label('性别').classes('text-center')
        radio = ui.radio(['男', '女']).classes('flex justify-center')
        checkbox = ui.checkbox('同意条款').classes('flex justify-center')

    dropdown = ui.select(label='选择颜色', options=['红色', '绿色', '蓝色']).classes('w-64 justify-end')

    def on_button_click():
        logger.info(f"按钮点击，值为 - 姓名: {text_input.value}, 年龄: {slider.value}, 性别: {radio.value}, 同意条款: {checkbox.value}, 颜色: {dropdown.value}")
        ui.notify(
            f'姓名: {text_input.value}, 年龄: {slider.value}, 性别: {radio.value}, 同意条款: {checkbox.value}, 颜色: {dropdown.value}')

    ui.button('提交', on_click=on_button_click).classes('justify-end')

    def open_modal():
        logger.info("模态对话框打开")  # 模态对话框打开时记录日志
        with ui.dialog() as dialog, ui.card():
            ui.label('这是一个模态对话框').classes('text-center')
            ui.button('关闭', on_click=dialog.close).classes('justify-center')
        dialog.open()

    ui.button('打开模态对话框', on_click=open_modal).classes('justify-end')

    with ui.card().classes('mx-auto p-4'):
        ui.label('卡片内容').classes('text-center')
        ui.button('卡片按钮').classes('justify-center')

    with ui.grid(columns=2).classes('mx-auto'):
        ui.label('网格单元1').classes('text-center')
        ui.label('网格单元2').classes('text-center')
        ui.label('网格单元3').classes('text-center')
        ui.label('网格单元4').classes('text-center')
