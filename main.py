import argparse
import subprocess
import pyperclip
from rich import print
from slugify import slugify


def handle_args():
    parser = argparse.ArgumentParser(description="Generate git branch name.")

    parser.add_argument("name", type=str, help="Name of the branch")
    parser.add_argument(
        "--prefix",
        "-p",
        type=str,
        help="Prefix of the branch name",
    )
    parser.add_argument(
        "--type",
        "-t",
        type=str,
        help="Task type (feature, bugfix, hotfix, etc.)",
        default="feature",
    )
    parser.add_argument(
        "--checkout",
        "-c",
        action="store_true",
        help="Checkout the branch after creation",
    )
    parser.add_argument(
        "--clipboard",
        "-cb",
        action="store_true",
        help="Copy the branch name to the clipboard",
    )
    parser.add_argument(
        "--prefix-only",
        "-po",
        action="store_true",
        help="Only use the prefix in the branch name",
    )

    return parser.parse_args()


def git_checkout(branch: str):
    command = ["git", "checkout", "-b", branch]
    subprocess.run(command)


def copy_to_clipboard(branch: str):
    pyperclip.copy(branch)


def main():
    args = handle_args()

    slug = slugify(args.name)

    if args.prefix_only:
        branch = f"{args.type}/{args.prefix}"
    else:
        branch = f"{args.type}/{args.prefix}-{slug}"

    if args.checkout:
        git_checkout(branch)
        print(f"[bold green]Branch {branch} created and checked out[/bold green]")

    if args.clipboard:
        copy_to_clipboard(branch)
        print("[bold green]Branch name copied to clipboard[/bold green]")


if __name__ == "__main__":
    main()
