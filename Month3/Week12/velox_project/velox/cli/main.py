"""
Velox Framework - CLI Main Entry Point
"""
import sys
from velox.cli.project import create_project, create_app
from velox.cli.migrate import make_migrations, migrate


def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: velox <command> [args]")
        print("Commands:")
        print("  makeproject <name>  - Create a new Velox project")
        print("  makeapp <name>      - Create a new app")
        print("  makemigrations      - Create migration files")
        print("  migrate             - Apply migrations")
        return
    
    command = sys.argv[1]
    
    if command == 'makeproject':
        if len(sys.argv) < 3:
            print("Usage: velox makeproject <name>")
            return
        project_name = sys.argv[2]
        create_project(project_name)
    
    elif command == 'makeapp':
        if len(sys.argv) < 3:
            print("Usage: velox makeapp <name>")
            return
        app_name = sys.argv[2]
        create_app(app_name)
    
    elif command == 'makemigrations':
        make_migrations()
    
    elif command == 'migrate':
        migrate()
    
    else:
        print(f"Unknown command: {command}")
        print("Available commands: makeproject, makeapp, makemigrations, migrate")


if __name__ == '__main__':
    main()
