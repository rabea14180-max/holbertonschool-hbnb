# part2/run.py
from app.api import create_api

app = create_api()

if __name__ == "__main__":
    app.run(debug=True)
