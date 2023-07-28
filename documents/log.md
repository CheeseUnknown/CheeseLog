# **日志记录**

本系统默认提供10种记录方式，但其中9种都是由`default(...)`衍生而来的。

如果你需要输出自定义等级的消息，请使用`default(...)`手动设置标签。

- **`def default(level: str, message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

    - **colorfulMessage**

        不满足于自动的色彩填充，可以选择自定义的控制台内容。

        它仅会改变消息内容，对消息等级以及时间的样式不会有影响。

        禁用彩色，该值不生效。

    - **logger**

        应该不会用到...指定其他的日志实例输出消息。

- **`def debug(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

- **`def info(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

- **`def starting(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

- **`def ending(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

- **`def warning(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

- **`def danger(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

- **`def error(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

- **`def http(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**

- **`def websocket(message: str, colorfulMessage: Optional[str] = None, logger: Optional[Logger] = logger)`**
