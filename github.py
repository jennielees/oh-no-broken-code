# I'm so close with this one.. I've got it to print out some stuff I got
# from the GitHub API, but not what I want!
# I saved the API stuff in a file to save time! :-)

import json

def github_api_response():
    with open('github.json') as f:
        github = json.loads(f.read())
    return github


def print_user_repository_names():

    # I just want to print out the names and descriptions of the repositories..
    # like 'Hackbright-Curriculum: Exercises for the Hackbright Academy Fellowship Program'

    repos = github_api_response()

    for repo in repos:
        # I don't think I have these keys right
        # Also I'd like to print it on one line.
        print repo['repo_name']
        print repo['repo_description']


if __name__=="__main__":
    print_user_repository_names()