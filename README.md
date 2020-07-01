## INTRODUCTION

This package aims to be all you need to meet full Acro Standards development specifications on your project.

## INSTALLATION

### Composer

1. You will need to specifically allow non-standard scaffold packages. Add the following to your composer.json
    ```
    "extra": {
        "drupal-scaffold": {
            "allowed-packages": [
                "acromedia/drupal-scaffold"
            ],
            "locations": {
                "web-root": "./web",
                "project-root": "."
            }
        }
    }
    ```

2. Use composer to add package as a dev dependency
    ```
    composer require acromedia/drupal-scaffold --dev
    ```

3. (Optional) Setup your project name
   ```
   inv setname
   ```
   This will set the correct project name in the lando and phpunit config, otherwise you will have to do so manually

## Overridding

### Invoke

This package provides standard tasks but you can also provide your own. It is recommended to provide your own additional tasks as opposed to overriding the existing tasks. Since everything is python based, you can also call on individual functions.

### Lando

This package provides a `.lando.base.yml` with a standard Drupal setup, you should provide your specific customization in a `.lando.yml` file and commit that to your project. If you wish to have specific config only to you, you can provide a `.lando.local.yml` file.

[Lando Docs](https://docs.lando.dev/config/lando.html)

### NPM/Yarn - Package.json

NPM does not have any mechanism for base files or overrides. This package provides package.json changes as appends, to hopefully work with your existing files, but you may have to manually merge changes.

### Composer

Like NPM, composer doesn't have any mechanism for base files, so the same append workflow is used.




