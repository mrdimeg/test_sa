
from os import rename
from git import Repo
from git.exc import GitError

PATH_OF_GIT_REPO = r'/Users/dmitrirodioskin/Documents/git_repositories/test_sa/'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push_gitlab():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(all=True)
        repo.index.commit(COMMIT_MESSAGE)
        
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured on Gitlab while pushing the code')

def git_push_github():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(all=True)
        repo.index.commit(COMMIT_MESSAGE)
        
        origin = repo.remote(name='origin_github')
        origin.push()
    except:
        print('Some error occured on Github while pushing the code')
 
git_push_github()
git_push_gitlab()

