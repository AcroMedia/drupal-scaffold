# invoke

## Requirements

### Python

You very likely already have python on your system

Debian/Ubuntu: `sudo apt install python`
Manual: https://www.python.org/downloads/your package management system on linux, for example on debian `sudo apt install python`

### Pip

Pip is python's package management system, like composer is for PHP. You might also already have pip on your system or it can probably be installed via package manager.

* Debian/Ubuntu: `sudo apt install python-pip`
* Manually: https://pip.pypa.io/en/stable/installing/

### Invoke

Now that you have pip, just do `python -m pip install invoke`

### AWS Authentication (Required to pull from S3)

You'll need to have the AWS authentication script available to authenticate to AWS.

See https://git.acromedia.com/teams/id/devops/infrastructure/blob/master/README.md#install for details

### Python 3

If you prefer to use python3 and it isn't your default, you can replace `python` with `python3` in the commands above

## CLI Usage

Use `inv` or `invoke` to call tasks

```
inv setup
```

To see what commands are available

```
inv --list
```

## Configuration
The included `tasks.py` is just a starting point, you'll want to copy it to your own project and modify it to match your specific requirements.

For more info about invoke, see http://docs.pyinvoke.org/en/stable/getting-started.html