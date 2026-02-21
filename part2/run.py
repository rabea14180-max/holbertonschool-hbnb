#part2/run.py
from app import create_app
from app.api import create_api

app = create_app()
api = create_api(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
