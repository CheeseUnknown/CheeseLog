# **消息等级**

## **预设等级**

本系统默认提供9种消息等级，分别为`'DEBUG'`,`'INFO'`,`'STARTING'`,`'ENDING'`,`'HTTP'`,`'WEBSOCKET'`,`'WARNING'`,`'DANGER'`,`'ERROR'`。

各等级的权重也分为5档，这只是粗略的分别，有需要的话可以自定义更详细的权重分类。

```python
{
    'DEBUG': Level(10, '34', None),
    'INFO': Level(20, '32', None),
    'STARTING': Level(20, '32', None),
    'ENDING': Level(20, '34', None),
    'HTTP': Level(20, None, None),
    'WEBSOCKET': Level(20, None, None),
    'WARNING': Level(30, '33', None),
    'DANGER': Level(40, '31', None),
    'ERROR': Level(50, '35', None)
}
```

## **`class Level`**

你可以通过该类创造自定义的等级。

- **`def __init__(self, weight: NonNegativeInt, color: Optional[str] = None, messageTemplate: Optional[str] = None)`**

    - **weight**

        权重。小于日志过滤权重的消息会被忽略。

    - **color**

        控制台打印的等级标签样式。

    - **messageTemplate**

        消息格式，默认为`logger.messageTemplate`。

