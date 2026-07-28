# Dynamic Report Generator

# Decorator to format the report
def format_report(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("              DYNAMIC REPORT")
        print("=" * 50)
        print(func(*args, **kwargs))
        print("=" * 50)
    return wrapper


class Report:
    # Default template
    default_template = "Standard"

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.template = Report.default_template

    # Class method to change template
    @classmethod
    def set_template(cls, template):
        cls.default_template = template

    # Magic method
    def __str__(self):
        return (
            f"Title    : {self.title}\n"
            f"Content  : {self.content}\n"
            f"Template : {self.template}"
        )

    # Method to display report
    @format_report
    def display(self):
        return str(self)


# Create first report
report1 = Report(
    "Python OOP",
    "This report explains Object-Oriented Programming concepts."
)

report1.display()

# Change the template using class method
Report.set_template("Professional")

# Create second report
report2 = Report(
    "Dynamic Report Generator",
    "This report is generated using Python OOP concepts."
)

report2.display()