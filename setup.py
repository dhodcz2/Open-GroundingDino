import os
import subprocess
import os

from setuptools import setup, find_packages
from setuptools.command.build_py import build_py as _build_py
from setuptools.command.install import install as _install

class CustomBuildCommand(_build_py):
    def run(self):
        # Run the nested setup.py
        self.run_subprocess('open_groundingdino/models/GroundingDINO/ops')
        super().run()

    def run_subprocess(self, directory):
        subprocess.check_call(
            ['python', './setup.py', 'build', 'install'], cwd=directory
        )
        subprocess.check_call(
            ['python', 'test.py'], cwd=directory
        )

class CustomInstallCommand(_install):
    def run(self):
        self.run_subprocess('open_groundingdino/models/GroundingDINO/ops')
        super().run()

    def run_subprocess(self, directory):
        subprocess.check_call(
            ['python', './setup.py', 'build', 'install'], cwd=directory
        )
        subprocess.check_call(
            ['python', 'test.py'], cwd=directory
        )

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name="open_groundingdino",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires='>=3.11',
    include_package_data=True,
    cmdclass={
        'build_py': CustomBuildCommand,
        'install': CustomInstallCommand,
    },
    install_requires=install_requires,
    entry_points={},
)
