import gevent

bind = "0.0.0.0:5000"
#workers = multiprocessing.cpu_count() * 2 - 5
#workers = 4
#threads = workers
timeout = 240 #120
worker_class = "gevent"
#graceful_timeout = 0
preload_app = True