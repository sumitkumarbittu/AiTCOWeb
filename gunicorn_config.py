import multiprocessing

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 50

# Socket
bind = '0.0.0.0:10000'

# Logging
loglevel = 'info'
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stderr

# Timeouts
timeout = 300  # 5 minutes
graceful_timeout = 30
keepalive = 2

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Debugging
reload = False
preload_app = True
