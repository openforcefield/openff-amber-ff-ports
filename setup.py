"""
openff-amber-ff-ports
"""
import sys
from setuptools import setup, find_namespace_packages
import versioneer

short_description = __doc__.split("\n")

# https://github.com/pytest-dev/pytest-runner#conditional-requirement
needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

try:
    with open("README.md", "r") as handle:
        long_description = handle.read()
except:
    long_description = "\n".join(short_description[2:]),


setup(
    name='openff-amber-ff-ports',
    author='The Open Force Field Initiative',
    author_email='info@openforcefield.org',
    description=short_description[0],
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='CC-BY-4.0',
    packages=find_namespace_packages(include=['openff.*']),
    package_data={'openff.amber_ff_ports/': ["offxml/*"]},
    include_package_data=True,
    setup_requires=[] + pytest_runner,
    url='https://github.com/openforcefield/openff-amber-ff-ports',
    platforms=['Linux',
               'Mac OS-X',
               'Unix'],
    entry_points={
        'openforcefield.smirnoff_forcefield_directory' : [
            'get_forcefield_dirs_paths = openff.amber_ff_ports.amber_ff_ports:get_forcefield_dirs_paths',
        ],
    }
)
