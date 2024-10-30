# Pyqt-fluent-widget实例代码解析

## 一、目录结构解析

- common :存放公共文件，包括配置文件、图标、标题文字显示、风格样式配置、全局信号
- components :存放组件文件，包括按钮、输入框、标签、进度条、滑块、单选框、复选框、单选框等
- config :存放缓存配置文件，包括主题配置、字体配置等,重启时加载更新
- resource :存放静态资源文件，包括图片、字体等
- view :存放界面文件，包括各模块子界面、主界面等
- main.py :主程序文件，负责启动程序，加载配置文件，加载主题，加载字体，加载主界面等

## 二、界面视图解析
### 1. 主界面视图（共15个子界面）
- 主界面视图：main_view.py
- 首页界面：home_interface.py
- 图标界面：icon_interface.py
- 基本输入界面：basic_input_interface.py
- 日期和时间界面：date_time_interface.py
- 对话框界面：dialog_interface.py
- 布局界面：layout_interface.py
- 材料界面：material_interface.py
- 菜单界面：menu_interface.py
- 导航界面：navigation_view_interface.py
- 滚动界面：scroll_interface.py
- 状态信息界面：state_info_interface.py
- 文本界面：text_interface.py
- 视图界面：view_interface.py
- 设置界面：setting_interface.py
- 帮助界面：gallery_interface.py

## 三、组件解析
### 1. 首页链接卡片模块
### 2. 首页实列卡片模块