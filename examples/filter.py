import __init__
from CheeseLog import CheeseLogger, Message

logger = CheeseLogger(key = 'myLogger')
logger.setFilter({
    'weight': 20,
    'messageKeys': [ 'FILTERED' ]
})

lowWeight_message = Message('LOW_WEIGHT', 10)
logger.addMessage(lowWeight_message)
highWeight_message = Message('HIGH_WEIGHT', 50)
logger.addMessage(highWeight_message)
filtered_message = Message('FILTERED', 100)
logger.addMessage(filtered_message)

logger.print('This is a low weight message.', messageKey = 'LOW_WEIGHT') # 不会输出
logger.print('This is a high weight message.', messageKey = 'HIGH_WEIGHT')
logger.print('This is a filtered message.', messageKey = 'FILTERED') # 不会输出
