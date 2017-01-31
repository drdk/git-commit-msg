# git-commit-msg

Simple git commit-msg hook to ensure that commit messages contain Jira issue id's


## Requirements

- Python 2.6
- bash


## Installation

Copy the following files to the .git/hook directory in the repository you are going to use the commit-msg hook.

```
commit-msg
jira-commit-msg.py
```

Both files have to be executables.

```
chmod +x filename
```


## Naming standard

Currently the naming standard is based on a simple regex.

A sample commit message should look like this

```
JIRA-ISSUE. Message.
```

eg.

```
DDC-1234. Sample commit message.
```


## Customize

To customize the message validation to your liking simply modify the existing regex.

line 6 in jira-commit-msg.py

```
REGEX = '^DDC-[\d]{4}\. [\w\d .,:;+]*\.$'
```

To test your regex you can simply do so [here](http://pythex.org/)


## License

git-commit-msg is released under the MIT license.
