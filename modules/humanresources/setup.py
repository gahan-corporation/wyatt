"""Setup tools config for the current package."""
import setuptools


setuptools.setup(
    name='humanresources',

    version='0.0.1',

    description='Basic human resource management.',
    long_description='Still basic human resources.',

    author='Gahan Corporation',
    author_email='gahan.corporation@gmail.com',

    license='The Unlicense',

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=['timesheets', 'toggl'],
    zip_safe=True,
)
