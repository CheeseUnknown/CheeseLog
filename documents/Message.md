# **Message**

```python
from CheeseLog import Message
```

## **`def __init__(self, key: str, weight: int = 10, message_template: str | None = None, timer_template: str | None = None, styledmessage_template: str | None = None)`**

- **weight**

    权重，更高的权重意味着更高的日志级别。

- **message_template**

    日志消息模板，未设置时默认为`CheeseLogger`实例的`message_template`。

- **timer_template**

    日期模板，未设置时默认为`CheeseLogger`实例的`timer_template`。

- **styledmessage_template**

    message_template_styled: 带样式的日志消息模板，未设置时默认为`CheeseLogger`实例的`message_template_styled`。

## **5种默认消息等级**

```python
{
    'DEBUG': Level(10),
    'INFO': Level(20, styledmessage_template = '(<green>%l</green>) <black>%t</black> > %c'),
    'WARNING': Level(30, styledmessage_template = '(<yellow>%l</yellow>) <black>%t</black> > %c'),
    'DANGER': Level(40, styledmessage_template = '(<red>%l</red>) <black>%t</black> > %c'),
    'ERROR': Level(50, styledmessage_template = '(<magenta>%l</magenta>) <black>%t</black> > %c')
}
```
