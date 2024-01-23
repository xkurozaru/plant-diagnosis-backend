#
# Gunicorn config file
#
wsgi_app = "src.main:app"

# Server Mechanics
# ========================================
# current directory
chdir = "/app"

# daemon mode
daemon = False

# environment variables
raw_env = ["ENV_TYPE=production"]

# Server Socket
# ========================================
bind = "0.0.0.0:8000"

# Worker Processes
# ========================================
workers = 2

# Worker Class
# ========================================
worker_class = "uvicorn.workers.UvicornWorker"


#  Logging
# ========================================
# access log
accesslog = "-"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# gunicorn log
errorlog = "-"
loglevel = "info"
