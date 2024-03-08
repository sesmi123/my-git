class GitCommandLineHelper():

    def __init__(self) -> None:
        self.command_help = {
            'init': self._git_init_help,
            'commit': self._git_commit_help,
            'push': self._git_push_help
        }

    def help(self, command: str) -> None:
        self.command_help.get(command, self._unsupported_command)()

    def _unsupported_command(self):
        print("Unrecognized command! Couldn't find help.")

    def _git_init_help(self):
        print("Usage: python mygit.py init <repository_name>")

    def _git_commit_help(self):
        print("Usage: python mygit.py commit <commit_message>")

    def _git_push_help(self):
        print("Usage: python mygit.py push <args>")
