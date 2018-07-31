from github import Github
import logging
import os
from git import Repo

from App.Project_Logger import Console_and_file_logger

##################### params #######################

GITHUBDOMAIN = 'https://api.github.com'
ORGANISATION = 'google'
GITHUB_TOKEN = '927e3c6ec7c80f901c5dbdbb1e8bec671b713be4'
LANGUAGE = 'Java'
MAX_REPOSITORIES = 1
LOCAL_REP_ROOT = './repos/'


####################################################


def ensure_dir(file_path):
    """
    Make sure a directory exists or create it
    :param file_path:
    :return:
    """
    logging.info('Trying to save to {0}'.format(file_path))
    if not os.path.exists(file_path):
        logging.info('Creating directory {}'.format(file_path))
        os.makedirs(file_path)


def clone_repos():
    """
    Clone the first n public git-repositories from a git organisation
    All params are editable in the params section of this script
    :return:
    """
    g = Github(base_url=GITHUBDOMAIN, login_or_token=GITHUB_TOKEN)
    cloned = 0

    for idx, repo in enumerate(g.get_organization(ORGANISATION).get_repos('all')):

        if cloned >= MAX_REPOSITORIES:
            # stop if number of cloned repos >= max repos to clone
            break
        if repo.full_name.startswith(ORGANISATION) and repo.private is False and repo.language == LANGUAGE:
            logging.info('Cloning repository {} from organisation {}'.format(repo.full_name, ORGANISATION))
            cloned += 1

            git_url = repo.git_url
            repo_dir = LOCAL_REP_ROOT + repo.full_name
            ensure_dir(repo_dir)

            Repo.clone_from(git_url, repo_dir)


if __name__ == '__main__':
    clone_repos()

