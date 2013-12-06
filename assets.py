from fabric.api import task, local


@task
def watch_styles():
    local('compass watch -c {{ cookiecutter.assets_dir }}/sass/config.rb')


@task
def compile_styles():
    local('compass compile -c {{ cookiecutter.assets_dir }}/sass/config.rb')


@task
def watch_scripts():
    local('coffee -c -w -j {{ cookiecutter.static_dir }}/scripts/master.js '
          '{{ cookiecutter.assets_dir }}/coffeescripts')


@task
def compile_scripts():
    local('coffee -c -j {{ cookiecutter.static_dir }}/scripts/master.js '
          '{{ cookiecutter.assets_dir }}/coffeescripts')


@task
def livereload():
    url = 'http://dev:35729/livereload.js'
    print (
        'To livereload your web pages add the following script tag to '
        'your HTML:'
    )
    print ''
    print '    <script type="text/javascript" src="{}"></script>'.format(url)
    print ''
    local('livereload')
