class Task:
    def __init__(self, name, description, date, start_time, end_time, category, resources=None):
        if resources is None:
            resources = {}
        self.name = name
        self.description = description
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.resources = resources
        self.category = category