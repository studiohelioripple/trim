# wsgi.py (or main.py)
import os
from app import app

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    
    # Production: Use Gunicorn programmatically
    from gunicorn.app.base import BaseApplication
    
    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()
        
        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key.lower(), value)
        
        def load(self):
            return self.application
    
    options = {
        'bind': f'0.0.0.0:{port}',
        'workers': 4,
        'worker_class': 'sync',
        'timeout': 120,
        'accesslog': '-',
        'errorlog': '-',
    }
    
    StandaloneApplication(app, options).run()
