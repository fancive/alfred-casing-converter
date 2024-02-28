import re
import subprocess
import sys
from workflow import Workflow, ICON_WEB


# Convert camel case to snake case
def camel_to_snake_case(input_str):
    str1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", input_str)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", str1).lower()


# Adjust camel case conversion logic
def camel_case_convert(input_str):
    # Consider camel case when splitting the string
    if "_" in input_str or "-" in input_str or " " in input_str:
        components = re.split(r"[-_\s]+", input_str)
        return components[0].lower() + "".join(x.title() for x in components[1:])
    else:  # If input is already in camel case, do not convert
        return input_str


# Adjust snake case conversion logic
def snake_case_convert(input_str):
    # Convert to snake case if input is in camel case
    if re.search("(.)([A-Z][a-z]+)", input_str):
        input_str = camel_to_snake_case(input_str)
    components = re.split(r"[-\s]+", input_str)
    return "_".join(x.lower() for x in components)


# Get clipboard data
def get_clipboard_data():
    p = subprocess.Popen(["pbpaste"], stdout=subprocess.PIPE)
    return p.communicate()[0].decode("utf-8")


# Process clipboard or argument
def process_input(workflow, input_str):
    # Apply camel and snake case conversion
    snake_case = snake_case_convert(input_str)
    camel_case = camel_case_convert(input_str)

    workflow.add_item(
        title="Camel Case: " + camel_case,
        subtitle="Convert input to Camel Case",
        arg=camel_case,
        valid=True,
        icon=ICON_WEB,
    )

    workflow.add_item(
        title="Snake Case: " + snake_case,
        subtitle="Convert input to Snake Case",
        arg=snake_case,
        valid=True,
        icon=ICON_WEB,
    )


def main(workflow):
    # Check if there are arguments passed to the script
    if len(sys.argv) > 1:
        input_str = sys.argv[1].strip()

    if input_str == "":
        # If no arguments, use clipboard content
        input_str = get_clipboard_data().strip()

    process_input(workflow, input_str)
    workflow.send_feedback()


if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
