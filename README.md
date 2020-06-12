## INTRODUCTION

This package aims to be all you need to add Docker4Drupal to your project.

## REQUIREMENTS

### Python 3

You very likely have some version installed on your system, but you'll need to make sure you have Python 3 for Invoke to work properly.

- Debian/Ubuntu: `sudo apt install python3`
- Manual: https://www.python.org/downloads/your package management system on linux, for example on debian `sudo apt install python3`

### Pip

Pip is python's package management system, like composer is for PHP. You might also already have pip on your system or it can probably be installed via package manager.

- Debian/Ubuntu: `sudo apt install python3-pip`
- Manually: https://pip.pypa.io/en/stable/installing/

### Invoke

Now that you have pip, just do `python3 -m pip install invoke`

## INSTALLATION

### Composer File Changes

There are a couple changes you need to make to your project's `composer.json` before running `composer require`.

1. Add the repository definition
    ```
    ...
    "repositories": [
        ...,
        {
            "type": "git",
            "url": "https://git.acromedia.com/cbanman/local-dev-docker4drupal"
        }
    ],
    ...
    ```
2. Add package to the `allowed-packages` for drupal-scaffold
    ```
    ...
    "extra": {
        "allowed-packages": [
            "cbanman/local-dev-docker4drupal"
        ]
        ...
    }
    ...
    ```
3. Create the file `auth.json` in your base directory and add your [personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)
   to authenticate with Gitlab to be able to pull the package. Be sure to add it to your `.gitignore`
    ```
    {
      "http-basic": {
        "git.acromedia.com": {
          "username": "___token___",
          "password": "<personal_access_token>"
        }
      }
    }
    ```
4. Use composer to add package as a dev dependency
    ```
    composer require cbanman/local-dev-docker4drupal --dev
    ```

## CONFIGURATION

Once the package has been installed copy the contents of `example.docker4drupal.env` into your `.env`. You can configure these variables as needed.

For more details see the [Docker4Drupal Documentation](https://wodby.com/docs/stacks/drupal/local/)

## RUNNING

When you've finished configuring your set up, you can use invoke commands to start everything up. 

```
inv docker-up
```

To see a list of other available invoke commands, use `inv --list`. Commands for Docker4Drupal are prefixed with `docker-`.