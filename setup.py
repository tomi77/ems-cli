from setuptools import find_packages, setup

setup(
    name='ems-cli',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/tomi77/ems-cli',
    license='MIT',
    author='Tomasz Jakub Rup',
    author_email='tomasz.rup@gmail.com',
    install_requires=['pyems'],
    description='CLI for EVO Media Server',
    long_description=open('README.rst').read(),
    entry_points={
        'console_scripts': [
            'ems-add-group-name-alias = ems_cli.add_group_name_alias:main',
            'ems-add-stream-alias = ems_cli.add_stream_alias:main',
            'ems-create-dash-stream = ems_cli.create_dash_stream:main',
            'ems-create-hds-stream = ems_cli.create_hds_stream:main',
            'ems-create-hls-stream = ems_cli.create_hls_stream:main',
            'ems-create-ingest-point = ems_cli.create_ingest_point:main',
            'ems-create-mss-stream = ems_cli.create_mss_stream:main',
            'ems-flush-group-name-aliases = ems_cli.flush_group_name_aliases:main',
            'ems-flush-stream-aliases = ems_cli.flush_stream_aliases:main',
            'ems-get-config-info = ems_cli.get_config_info:main',
            'ems-get-group-name-by-alias = ems_cli.get_group_name_by_alias:main',
            'ems-get-stream-info-by-id = ems_cli.get_stream_info:main_id',
            'ems-get-stream-info-by-name = ems_cli.get_stream_info:main_name',
            'ems-get-streams-count = ems_cli.get_streams_count:main',
            'ems-is-stream-running-by-id = ems_cli.is_stream_running:main_id',
            'ems-is-stream-running-by-name = ems_cli.is_stream_running:main_name',
            'ems-list-config = ems_cli.list_config:main',
            'ems-list-group-name-aliases = ems_cli.list_group_name_aliases:main',
            'ems-list-http-streaming-sessions = ems_cli.list_http_streaming_sessions:main',
            'ems-list-ingest-points = ems_cli.list_ingest_points:main',
            'ems-list-stream-aliases = ems_cli.list_stream_aliases:main',
            'ems-list-streams = ems_cli.list_streams:main',
            'ems-list-streams-ids = ems_cli.list_streams_ids:main',
            'ems-pull-stream = ems_cli.pull_stream:main',
            'ems-push-stream = ems_cli.push_stream:main',
            'ems-record = ems_cli.record:main',
            'ems-remove-config-by-id = ems_cli.remove_config:main_id',
            'ems-remove-config-by-group-name = ems_cli.remove_config:main_name',
            'ems-remove-group-name-alias = ems_cli.remove_group_name_alias:main',
            'ems-remove-ingest-point = ems_cli.remove_ingest_point:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Multimedia :: Video',
    ]
)
