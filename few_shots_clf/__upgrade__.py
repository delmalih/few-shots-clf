##########################
# Function
##########################


def upgrade_version():
    """[summary]
    """
    # Read current version
    with open("few_shots_clf/__version__.txt", "r") as version_file:
        current_version = version_file.read()

    # Update version
    major, minor, build = map(int, current_version.split("."))
    build += 1
    new_version = f"{major}.{minor}.{build}"

    # Save version
    with open("few_shots_clf/__version__.txt", "w") as version_file:
        version_file.write(new_version)


##########################
# Main
##########################


if __name__ == "__main__":
    upgrade_version()
