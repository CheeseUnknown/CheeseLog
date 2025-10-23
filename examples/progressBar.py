import time, random

import __init__
from CheeseLog import CheeseLogger, Message, ProgressBar

logger = CheeseLogger(key = 'myLogger', filePath = 'logs/%Y-%m-%d.log')

loadingMessage = Message('LOADING')
logger.addMessage(loadingMessage)
loadedMessage = Message('LOADED', 20, messageTemplate_styled = '(<green>%k</green>) <black>%t</black> > %c')
logger.addMessage(loadedMessage)

progressbar = ProgressBar()
i = 0
while i < 100:
    bar, bar_styled = progressbar(i / 100)
    logger.print(bar, bar_styled, messageKey = 'LOADING', refresh = i != 0)
    time.sleep(random.uniform(0.05, 0.15))
    i += random.uniform(0.5, 1)
logger.print('Loading complete!', messageKey = 'LOADED', refresh = True)
