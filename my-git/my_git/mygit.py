import sys
from git_client import GitClient

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python mygit.py <command> <arguments>")
        sys.exit(1)

    gc = GitClient()
    command = sys.argv[1]
    
    gc.run_command(command, *sys.argv[2:])

    # if len(sys.argv) != 3 or sys.argv[1] != "ccgit" or sys.argv[2] != "init":
    #     print("Usage: python main.py mygit init <repo_name>")
    #     sys.exit(1)
