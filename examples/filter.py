import __init__
from CheeseLog import CheeseLogger, Message

logger = CheeseLogger(key = 'myLogger')
logger.set_filter({
    'weight': 20,
    'message_keys': [ 'FILTERED' ]
})

low_weight_message = Message('LOW_WEIGHT', 10)
logger.add_message(low_weight_message)
high_weight_message = Message('HIGH_WEIGHT', 50)
logger.add_message(high_weight_message)
filtered_message = Message('FILTERED', 100)
logger.add_message(filtered_message)

logger.print('LOW_WEIGHT', 'This is a low weight message.') # 不会输出
logger.print('HIGH_WEIGHT', 'This is a high weight message.')
logger.print('FILTERED', 'This is a filtered message.') # 不会输出
