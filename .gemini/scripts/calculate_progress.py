
import sys
import os
import re
import json

def calculate_progress(feature_name):
    try:
        tasks_file_path = os.path.join(".kiro", "specs", feature_name, "tasks.md")
        if not os.path.exists(tasks_file_path):
            print(json.dumps({"error": "tasks.md not found"}), file=sys.stderr)
            return {}

        with open(tasks_file_path, "r", encoding="utf-8") as f:
            content = f.read()

        total_tasks = len(re.findall(r"- \[ \]", content))
        completed_tasks = len(re.findall(r"- \[x\]", content))
        
        # The regex for total_tasks should be for both checked and unchecked boxes
        total_tasks = completed_tasks + total_tasks

        if total_tasks == 0:
            progress = 100
        else:
            progress = round((completed_tasks / total_tasks) * 100)

        return {
            "total": total_tasks,
            "completed": completed_tasks,
            "progress": progress
        }

    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return {}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        feature_name = sys.argv[1]
        progress_data = calculate_progress(feature_name)
        print(json.dumps(progress_data))
    else:
        print(json.dumps({"error": "Feature name not provided"}), file=sys.stderr)
