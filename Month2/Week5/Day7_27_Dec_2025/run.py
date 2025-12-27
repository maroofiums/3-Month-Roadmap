import sys
import uvicorn

sys.path.insert(0, r"d:\Roadmap\3-Month-Roadmap\Month2")

from Week5.Day7_27_Dec_2025.app.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
