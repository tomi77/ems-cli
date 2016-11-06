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
            'ems = ems_cli.__main__:main',
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
            'ems-list-streams = ems_cli.list_streams:main',
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
