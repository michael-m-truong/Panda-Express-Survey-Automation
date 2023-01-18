import multiprocessing

bind = "0.0.0.0:5000"
workers = multiprocessing.cpu_count() * 2 - 5
#workers = 4
threads = workers
timeout = 120
#worker_class = "sync"
#graceful_timeout = 0
preload_app = True