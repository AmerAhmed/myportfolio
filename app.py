"""
The main entry point for applications!
Amer Ahmed
Version 0.0.1
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
