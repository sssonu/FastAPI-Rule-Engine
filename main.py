from src.database import init_db
from src.api import app

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
