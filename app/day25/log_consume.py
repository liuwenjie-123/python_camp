import time
import secrets
import logging
import random
import logging.handlers
import os
import multiprocessing
import psutil

CPU_COUNT = multiprocessing.cpu_count()

def log_forver():
    
    last_log_time = 0.0
    last_log_length = 1
    update_logger = logging.getLogger("update")
    while True:
        length = random.randint(2,40)
        log_str = f"{secrets.token_urlsafe(length)},{last_log_length} {last_log_time}ms"

        if last_log_time > 10:
            update_log_str = f"CPU{CPU_COUNT} python write {last_log_length} byte {last_log_time} ms"
            if last_log_time > 50:
                update_logger.error(update_log_str)
            else:
                update_logger.info(update_log_str)

        before = time.time() * 1000
        if last_log_time > 50: # 大于100毫秒
            logging.error(log_str)
        elif last_log_time > 10:
            logging.warning(log_str)
        else:
            logging.info(log_str)

        last_log_length = len(log_str) + len("2020-11-21 11:32:44,632 INFO ")
        last_log_time = time.time() * 1000 - before
        print("last_log_time:", last_log_time)
        time.sleep(1)



LOG_MAX_SIZE = 10*1024*1024
LOG_DIR = r"D:\tools\testIO"
LOG_FILENAME = "test_io.log"
LOG_FULL_FILENAME = LOG_DIR+"\\"+ LOG_FILENAME

def init_log():
    root = logging.getLogger()
    root.setLevel(logging.INFO)
    os.makedirs(LOG_DIR,exist_ok=True)
    h = logging.handlers.RotatingFileHandler(LOG_FULL_FILENAME,'a',LOG_MAX_SIZE,10)
    h.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    root.addHandler(h)


UPDATED_LOG_FILENAME = r"D:\cloudgame_log\py_write.log"

def init_can_updated_log():
    update_logger = logging.getLogger("update")
    update_logger.setLevel(logging.INFO)
    h = logging.handlers.RotatingFileHandler(UPDATED_LOG_FILENAME,'a',LOG_MAX_SIZE,10)
    h.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    update_logger.addHandler(h)

if __name__ == "__main__":
    current_process = psutil.Process()
    current_process.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
    init_log()
    init_can_updated_log()
    log_forver()