#!/usr/bin/python

import sys
import re
import subprocess


REGEX = '^DDC-[\d]{4}\. [\w\d .,:;+]*\.$'


def current_branch_name():
  """Gets the current GIT branch name.

  Returns:
    string: The current branch name.
  """
  return subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])


def get_jira_issue_hint(branch_name):
  """Extracts the Jira issue number from the branch name.

  Args:
    branch_name (str): The branch name to parse.

  Returns:
    string: The Jira issue number, or sample issue number.
  """
  match = re.findall('feature/(DDC-[\d]{4})-', branch_name)
  if match and match[0]:
    return match[0]
  return 'DDC-XXXX'


def valid_commit_message(message):
  """Function to validate the commit message.

  Args:
    message (str): The message to validate.

  Returns:
    bool: True for valid messages, False otherwise.
  """
  if not re.match(REGEX, message):
    name = current_branch_name()
    issue_number = get_jira_issue_hint(name)
    print 'ERROR: Missing Jira number in commmit message.'
    print 'Hint: {0}. Commit message.'.format(issue_number)
    return False

  print 'Commit message is valid.'
  return True


def main():
  """Main function."""
  message_file = sys.argv[1]
  try:
    txt_file = open(message_file, 'r')
    commit_message = txt_file.read()
  finally:
    txt_file.close()

  if not valid_commit_message(commit_message):
    sys.exit(1)

  sys.exit(0)


if __name__ == "__main__":
  main()
