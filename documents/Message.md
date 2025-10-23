# **Message**

```python
from CheeseLog import Message
```

## **`def __init__(self, key: str, weight: int = 10, messageTemplate: str | None = None, timerTemplate: str | None = None, styledMessageTemplate: str | None = None)`**

- **weight**

    权重，更高的权重意味着更高的日志级别。

- **messageTemplate**

    日志消息模板，未设置时默认为`CheeseLogger`实例的`messageTemplate`。

- **timerTemplate**

    日期模板，未设置时默认为`CheeseLogger`实例的`timerTemplate`。

- **styledMessageTemplate**

    messageTemplate_styled: 带样式的日志消息模板，未设置时默认为`CheeseLogger`实例的`messageTemplate_styled`。

## **5种默认消息等级**

```python
{
    'DEBUG': Level(10),
    'INFO': Level(20, styledMessageTemplate = '(<green>%l</green>) <black>%t</black> > %c'),
    'WARNING': Level(30, styledMessageTemplate = '(<yellow>%l</yellow>) <black>%t</black> > %c'),
    'DANGER': Level(40, styledMessageTemplate = '(<red>%l</red>) <black>%t</black> > %c'),
    'ERROR': Level(50, styledMessageTemplate = '(<magenta>%l</magenta>) <black>%t</black> > %c')
}
```
