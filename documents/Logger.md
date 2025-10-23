# **Logger**

日志系统的主体。

```python
from CheeseLog import CheeseLogger
```

## **`CheeseLogger.instances: dict[str, CheeseLogger] = {}`**

所有CheeseLogger实例

## **`def __init__(self, key: str | None = None, filePath: str | None = None, *, messages: dict[str, Message] = {}, messageTemplate: str = '(%k) %t > %c', timerTemplate: str = '%Y-%m-%d %H:%M:%S.%f', messageTemplate_styled: str = '(<black>%k</black>) <black>%t</black> > %c', filter: CheeseLog.Filter = {})`**

- **filePath**

    日志文件路径，若不设置则不会写入文件

- **messages**

    消息类型

- **messageTemplate**

    消息模版；支持的占位符有：

    - %k: key
    - %t: 时间模版
    - %c: 内容

- **timerTemplate**

    时间模版

- **messageTemplate_styled**

    带样式的消息模版；支持的占位符有：

    - %k: key
    - %t: 时间模版
    - %c: 内容

- **filter**

    过滤器

## **`self.key: str`**

## **`self.filePath: str | None`**

    日志文件路径

## **`self.messages: dict[str, CheeseLog.Message]`**

## **`self.messageTemplate: str`**

消息模版

## **`self.timerTemplate: str`**

时间模版

## **`self.messageTemplate_styled: str`**

带样式的消息模版

## **`self.filter: CheeseLog.Filter`**

过滤器

## **`self.is_running: bool`**

## **`self.has_console: bool`**

是否有控制台输出

## **`def addMessage(self, message: CheeseLog.Message)`**

## **`def deleteMessage(self, key: str)`**

## **`def start(self)`**

## **`def stop(self)`**

## **`def setFilter(self, filter: CheeseLog.Filter)`**

## **`def print(self, content: str, content_styled: str | None = None, messageKey: str = 'DEBUG', *, end: str = '\n', refresh: bool = False)`**

- **Args**

    - **content**

        消息内容

    - **key**

        消息类型

    - **content_styled**

        带样式的消息内容

    - **end**

        结尾符

    - **refresh**

        是否刷新终端输出

## **`def debug(self, content: str, content_styled: str | None = None, *, end: str = '\n', refresh: bool = False)`**

## **`def info(self, content: str, content_styled: str | None = None, *, end: str = '\n', refresh: bool = False)`**

## **`def warning(self, content: str, content_styled: str | None = None, *, end: str = '\n', refresh: bool = False)`**

## **`def danger(self, content: str, content_styled: str | None = None, *, end: str = '\n', refresh: bool = False)`**

## **`def error(self, content: str, content_styled: str | None = None, *, end: str = '\n', refresh: bool = False)`**

## **`def encode(self, content: str) -> str`**

    当内容中有`'<'`和`'>'`字符时，进行转义
