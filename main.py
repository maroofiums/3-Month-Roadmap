import os
from datetime import datetime, timedelta

roadmap = {
    "Month1": {
        "start": "2025-11-23",
        "end": "2025-12-20",
        "weeks": {
            "Week1": ["Arrays / Strings"],
            "Week2": ["Linked List"],
            "Week3": ["Stack / Queue"],
            "Week4": ["Trees / BST"]
        }
    },
    "Month2": {
        "start": "2025-12-21",
        "end": "2026-01-17",
        "weeks": {
            "Week5": ["REST API + CRUD"],
            "Week6": ["Async / Await"],
            "Week7": ["Authentication + Middleware"],
            "Week8": ["Caching + Mini Project"]
        }
    },
    "Month3": {
        "start": "2026-01-18",
        "end": "2026-02-22",
        "weeks": {
            "Week9": ["ML Basics"],
            "Week10": ["ML API Integration"],
            "Week11": ["System Design Lite"],
            "Week12": ["Integrated Projects"]
        }
    }
}

base_dir = ""

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

for month, info in roadmap.items():
    month_dir = os.path.join(base_dir, month)
    os.makedirs(month_dir, exist_ok=True)

    start_date = datetime.strptime(info["start"], "%Y-%m-%d")
    end_date = datetime.strptime(info["end"], "%Y-%m-%d")

    week_names = list(info["weeks"].keys())
    week_dates = list(daterange(start_date, end_date))
    days_per_week = len(week_dates) // len(week_names)

    for i, week in enumerate(week_names):
        week_dir = os.path.join(month_dir, week)
        os.makedirs(week_dir, exist_ok=True)

        start_idx = i * days_per_week
        end_idx = (i + 1) * days_per_week if i != len(week_names) - 1 else len(week_dates)
        week_days = week_dates[start_idx:end_idx]

        for day_idx, day_date in enumerate(week_days):
            day_folder = os.path.join(week_dir, f"Day{day_idx+1}_{day_date.strftime('%d_%b_%Y')}")
            os.makedirs(day_folder, exist_ok=True)

            readme_path = os.path.join(day_folder, "README.md")
            py_path = os.path.join(day_folder, "solution.py")

            with open(readme_path, "w") as f:
                f.write(f"# {month} - {week} - Day {day_idx+1}\n")
                f.write(f"**Date:** {day_date.strftime('%d %b %Y')}\n\n")
                f.write(f"**Topic:** {info['weeks'][week][0]}\n\n")
                f.write("**Focus:** \n\n")
                f.write("**Problem / Exercise:** \n\n")
                f.write("**Notes / Mini Experiment:** \n\n")

            with open(py_path, "w") as f:
                f.write("# Write your code here\n")

print(f"Rebel roadmap folder structure generated in '{base_dir}'")
