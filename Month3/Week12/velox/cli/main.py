import sys
from velox.cli.project import makeproject
from velox.cli.app import makeapp
from velox.cli.migrate import makemigrations_cmd, migrate_cmd

def main():
    command = sys.argv[1]

    if command == "makeproject":
        makeproject(sys.argv[2])

    elif command == "makeapp":
        makeapp(sys.argv[2])

    elif command == "makemigrations":
        makemigrations_cmd()

    elif command == "migrate":
        migrate_cmd()
