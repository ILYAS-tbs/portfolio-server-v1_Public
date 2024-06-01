# gunicorn.conf


command='/home/ilyasss/Desktop/z_programs/z_django_projects_done/portfolio_server/venv/bin/gunicorn'

# path to the whole django project - 
pythonpath='/home/ilyasss/Desktop/z_programs/z_django_projects_done/portfolio_server/portfolio_server/'

# The address and port on which your application will run
bind = "127.0.0.1:8001"

# The number of worker processes (adjust according to your system's capabilities)
workers = 3

# The WSGI module and application
module = 'portfolio_server.wsgi:application'