import os

DATA_PATH = "data/cours"

def save_course_file(title, category, content):
    filename = title.replace(" ", "_").lower() + ".md"
    category_path = os.path.join(DATA_PATH, category)
    os.makedirs(category_path, exist_ok=True)
    filepath = os.path.join(category_path, filename)

    with open(filepath, "w") as file:
        file.write(content)

def read_course_file(category, filename):
    filepath = os.path.join(DATA_PATH, category, filename)
    with open(filepath, "r") as file:
        return file.read()

def list_courses():
    courses = []
    for root, dirs, files in os.walk(DATA_PATH):
        for file in files:
            if file.endswith(".md"):
                courses.append(os.path.join(root, file))
    return courses