import git
import typing as t


def get_all_branches(repo_path) -> t.List[str]:
    repo = git.Repo(repo_path)
    branches = [str(branch) for branch in repo.branches]
    return branches


def get_latest_commit_time(repo_path, branch_name):
    repo = git.Repo(repo_path)
    branch = repo.branches[branch_name]
    latest_commit = branch.commit
    return latest_commit.committed_datetime


def compare_branches(repo_path, branch1, branch2):
    time_branch1 = get_latest_commit_time(repo_path, branch1)
    time_branch2 = get_latest_commit_time(repo_path, branch2)

    print(f"Latest commit time for {branch1}: {time_branch1}")
    print(f"Latest commit time for {branch2}: {time_branch2}")

    if time_branch1 > time_branch2:
        print(f"{branch1} is ahead of {branch2}")
        return True
    elif time_branch1 < time_branch2:
        print(f"{branch2} is ahead of {branch1}")
        return False
    else:
        print(f"{branch1} and {branch2} have the same latest commit time")
        return None


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--repo", help="repo path.")
    args = parser.parse_args()
    if args.repo:
        branches = get_all_branches(args.repo)
        pairs = []

        for branch in branches:
            time_branch = get_latest_commit_time(args.repo, branch)
            pairs.append((time_branch, branch))

        res = sorted(pairs, key=lambda pair: pair[0])
        print(res)
    else:
        print("Error: no repo selected.")


if __name__ == "__main__":
    main()
