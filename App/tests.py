# First create a Github instance:

# using username and password
# g = Github("minority4u", "Sven250486!")

# or using an access token
# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# public github repo
# g = Github(base_url="https://api.github.com", login_or_token="927e3c6ec7c80f901c5dbdbb1e8bec671b713be4")

# curl -u 927e3c6ec7c80f901c5dbdbb1e8bec671b713be4:x-oauth-basic -s https://api.github.com/orgs/irqed/repos\?per_page\=200 | ruby -rubygems -e 'require "json"; JSON.load(STDIN.read).each { |repo| %x[git clone #{repo["ssh_url"]} ]}'

# Then play with your Github objects:
# for idx, repo in enumerate(g.get_user().get_repos('all')):
#     #print(repo._identity)
#     if repo._identity.startswith('minority4u') and repo.private == False:
#         print(repo.name)
#
#         git_url = repo.git_url
#         repo_dir = "./test_" + repo._identity
#         ensure_dir(repo_dir)
#
#         Repo.clone_from(git_url, repo_dir)