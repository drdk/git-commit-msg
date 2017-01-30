#!/usr/bin/python

import sys
import re

REGEX = '^(DDC-[0-9]*)\. [\w .,+]*\.$'

def valid_commit_message(message):
  """Function to validate the commit message.

  Args:
    message (str): The message to validate.

  Returns:
    bool: True for valid messages, False otherwise.
  """
  if not re.match(REGEX, message):
    print 'ERROR: Missing Jira number in commmit message.'
    print 'Format "DDC-XXXX. Message."'
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
