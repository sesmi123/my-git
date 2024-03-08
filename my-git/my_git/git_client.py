import os
from git_init import GitInitializer
from git_cli_helper import GitCommandLineHelper

class GitClient:
    def __init__(self):
        self.repo_path = os.getcwd()

    def _git_init(self, repo_name) -> None:
        GitInitializer(repo_name).init()

    def _command_help(self, command) -> None:
        GitCommandLineHelper().help(command)

    def _general_help(self) -> None:
        print("Usage: python mygit.py <command> <arguments>")
        print("Available commands:")
        print("  init     Create an empty Git repository or reinitialize an existing one")
        print("  commit   Record changes to the repository")
        print("  push     Update remote refs along with associated objects")

    def run_command(self, command, *args) -> None:
        if command in ('help', '--help', '-h'):
            self._general_help()
        elif command == 'init':
            if len(args) > 0 and args[0] in ('help', '--help', '-h'):
                self._command_help(command)
            elif len(args) != 1:
                self._command_help(command)
            else:
                self._git_init(args[0])
        else:
            print(f"Command '{command}' not recognized.")
            print("Use 'python mygit.py help | --help | -h' to see available commands.")

