from nicegui import ui


def create_nav():
    # 导航栏容器（保持纯CSS布局）
    with ui.row().classes('''
        w-full justify-center items-center
        gap-8 py-4 bg-white shadow-md
        fixed top-0 z-50
        '''):
        # 导航项配置
        nav_items = [
            ('home', '主页', '/'),
            ('rocket', '示例1', '/page1'),
            ('widgets', '示例2', '/page2')
        ]

        # 创建独立路由链接
        for icon, text, target in nav_items:
            ui.link(text, target).classes('''
                flex flex-col items-center
                text-gray-600 hover:text-blue-600
                no-underline transition-all
                duration-300
                ''').props('active-class="text-blue-600 font-bold"')  # 激活状态样式

        # 右侧用户菜单（独立路由链接）
        ui.link('个人中心', '/profile').classes('''
            absolute right-4 flex items-center
            text-gray-600 hover:text-blue-600
            no-underline
            ''')
