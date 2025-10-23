import concurrent.futures, os, time

import __init__
from CheeseLog import CheeseLogger

def task(logger: CheeseLogger):
    for _ in range(100000):
        logger.debug('Extreme stress test log message.')

if __name__ == '__main__':
    now = time.time()

    if os.path.exists('logs/extreme.log'):
        os.remove('logs/extreme.log')
    logger = CheeseLogger('extremeLogger', 'logs/extreme.log')

    max_workers = os.cpu_count()
    # max_workers = 1
    with concurrent.futures.ThreadPoolExecutor(max_workers = max_workers) as executor:
        for i in range(max_workers):
            executor.submit(task, logger)
