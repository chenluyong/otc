
import subprocess,os,datetime

VERSION_MAIN = 1
VERSION_SUB = 0

def get_git_commit_count():
    """Return a numeric identifier of the latest git changeset.
    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    git_log = subprocess.run(
        ['git', 'rev-list', '--all', '--count'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        shell=True, cwd=repo_dir, universal_newlines=True,
    )
    commit_count = git_log.stdout
    return int(commit_count)

def get_git_changeset():
    """Return a numeric identifier of the latest git changeset.
    The result is the UTC timestamp of the changeset in YYYYMMDDHHMMSS format.
    This value isn't guaranteed to be unique, but collisions are very unlikely,
    so it's sufficient for generating the development version numbers.
    """
    repo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    git_log = subprocess.run(
        ['git', 'log', '--pretty=format:%ct', '--quiet', '-1', 'HEAD'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        shell=True, cwd=repo_dir, universal_newlines=True,
    )
    timestamp = git_log.stdout
    try:
        timestamp = datetime.datetime.utcfromtimestamp(int(timestamp))
    except ValueError:
        return None
    return timestamp.strftime('%Y%m%d%H%M%S')

def get_complete_version(version=None):
    """
    Return a tuple of the django version. If version argument is non-empty,
    check for correctness of the tuple provided.
    """
    if version is None:
        # from django import VERSION as version
        version = (VERSION_MAIN,VERSION_SUB, get_git_commit_count(),"final",0)
    else:
        assert len(version) == 5
        assert version[3] in ('alpha', 'beta', 'rc', 'final')

    return version

def get_main_version(version=None):
    """Return main version (X.Y[.Z]) from VERSION."""
    version = get_complete_version(version)
    parts = 2 if version[2] == 0 else 3
    return '.'.join(str(x) for x in version[:parts])

def get_version(version=None):
    """Return a PEP 440-compliant version number from VERSION."""
    version = get_complete_version(version)

    # Now build the two parts of the version number:
    # main = X.Y[.Z]
    # sub = .devN - for pre-alpha releases
    #     | {a|b|rc}N - for alpha, beta, and rc releases

    main = get_main_version(version)

    sub = ''
    if version[3] == 'alpha' and version[4] == 0:
        git_changeset = get_git_changeset()
        if git_changeset:
            sub = '.dev%s' % git_changeset

    elif version[3] != 'final':
        mapping = {'alpha': 'a', 'beta': 'b', 'rc': 'rc'}
        sub = mapping[version[3]] + str(version[4])
    return main + sub

# print(get_version())