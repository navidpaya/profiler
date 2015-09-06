from setuptools import setup

setup(
    name='Profiler',
    version='0.1',
    py_modules=['profiler'],
    install_requires=[
        'Click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        profiler=profiler:runner
    ''',
)
