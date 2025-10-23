import __init__
from CheeseLog import CheeseLogger, Message

logger = CheeseLogger(key = 'myLogger', filePath = 'logs/%Y-%m-%d.log')

logger.debug('This is a debug message.')
logger.info('This is an info message.')
logger.warning('This is a warning message.')
logger.danger('This is a danger message.')
logger.error('This is an error message.')

logger.addMessage(Message('CUSTOM', 30, messageTemplate_styled = '(<blue>%k</blue>) <black>%t</black> > %c'))
logger.print('This is a custom message.', messageKey = 'CUSTOM')
