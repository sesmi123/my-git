import os

class GitInitializer:
    def __init__(self, repo_name) -> None:
        self.repo_name = repo_name

    def _init_git_files(self):
        os.makedirs(os.path.join(self.repo_name, '.git', 'objects'))
        os.makedirs(os.path.join(self.repo_name, '.git', 'refs', 'heads'))
        os.makedirs(os.path.join(self.repo_name, '.git', 'hooks'))
        os.makedirs(os.path.join(self.repo_name, '.git', 'info'))

        open(os.path.join(self.repo_name, '.git', 'HEAD'), 'w').close()
        open(os.path.join(self.repo_name, '.git', 'config'), 'w').close()
        open(os.path.join(self.repo_name, '.git', 'description'), 'w').close()

        with open(os.path.join(self.repo_name, '.git', 'HEAD'), 'w') as f:
            f.write('ref: refs/heads/master\n')

    def init(self):
        git_path = os.path.join(self.repo_name,'.git')
        if os.path.exists(git_path):
            self._init_git_files()
            print(f"Reinitialized existing Git repository in {os.path.abspath(self.repo_name)}/.git/")
        else:
            os.makedirs(git_path)
            self._init_git_files()
            print(f'Initialized empty Git repository in {os.path.abspath(self.repo_name)}/.git/')


