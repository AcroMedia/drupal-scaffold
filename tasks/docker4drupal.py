from invoke import task
import multiprocessing

projectName = 'project'
dockerDrupalRoot = '/var/www/html/web'
cpuCount = multiprocessing.cpu_count()

@task
def docker_up(c):
    """
    Start up docker containers.
    """
    print('Starting up containers for {}...'.format(projectName))
    c.run('docker-compose pull')
    c.run('docker-compose up -d --remove-orphans')

@task(docker_up)
def docker_start(c):
    """
    Start up docker containers.
    """

@task
def docker_stop(c):
    """
    Stop containers.
    """
    print('Stopping containers for {}...'.format(projectName))
    c.run('docker-compose stop')

@task
def docker_prune(c):
    '''
    Stops containers and removes containers, networks, volumes, and images created by `up`.
    '''
    c.run('docker-compose down -v')

@task(help={'image': "Name of the image to restart. If nothing is provided then all images are restarted."})
def docker_restart(c, image=''):
    '''
    Restart all or a specific container.
    '''
    c.run('docker-compose restart {}'.format(image))

@task(help={'image': "Name of the image to ssh into. Default is `php`."})
def docker_shell(c, image='php'):
    '''
    Access image via sh.
    '''
    c.run('docker-compose exec {} sh'.format(image), pty=True)

@task(help={'command': 'The drush command to run. Multiple drush parameters must be withing quotes. Example: `inv drush "updb -y"`'})
def docker_drush(c, command):
    '''
    Run a drush command. Commands with multiple parameters must be written within quotes. Example: `inv drush "updb -y"`.
    '''
    c.run('docker-compose exec php ./vendor/bin/drush -r {} {}'.format(dockerDrupalRoot, command), pty=True, echo=True)

@task(help={'container': "Name of the container to ssh into. If no container provided all logs will be shown."})
def docker_logs(c, container=''):
    '''
    View container logs. To filter the logs by a specific container, use the --container flag.
    '''
    c.run('docker-compose logs -f {}'.format(container))
