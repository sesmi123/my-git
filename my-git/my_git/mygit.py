import sys
from git_client import GitClient

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python mygit.py <command> <arguments>")
        sys.exit(1)

    gc = GitClient()
    command = sys.argv[1]
    
    gc.run_command(command, *sys.argv[2:])

