import time, random

import __init__
from CheeseLog import CheeseLogger, Message, ProgressBar

logger = CheeseLogger(key = 'myLogger', file_path = 'logs/%Y-%m-%d.log')

loadingMessage = Message('LOADING')
logger.add_message(loadingMessage)
loadedMessage = Message('LOADED', 20, message_template_styled = '(<green>%k</green>) <black>%t</black> > %c')
logger.add_message(loadedMessage)

progress_bar = ProgressBar()
i = 0
while i < 100:
    bar, bar_styled = progress_bar(i / 100)
    logger.print('LOADING', bar, bar_styled, refresh = i != 0)
    time.sleep(random.uniform(0.05, 0.15))
    i += random.uniform(0.5, 1)
logger.print('LOADED', 'Loading complete!', refresh = True)
