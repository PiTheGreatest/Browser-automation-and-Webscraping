import base64
from github import Github
from github import InputGitTreeElement

user = "GithubUsername"
password = "*********"
g = Github(user,password)
repo = g.get_user().get_repo('solve-this-webscraping-issue') # repo name
file_list = [
    'C:\\Users\jesse\Dropbox\Swell-Forecast\git-test\index.html',
    'C:\\Users\jesse\Dropbox\Swell-Forecast\git-test\margin_table.html'
]
file_names = [
    'index.html',
    'margin_table.html'
]
commit_message = 'python commit'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)

element_list = list()
for i, entry in enumerate(file_list):
    with open(entry) as input_file:
        data = input_file.read()
    if entry.endswith('.png'): # images must be encoded
        data = base64.b64encode(data)
    element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
    element_list.append(element)

tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)