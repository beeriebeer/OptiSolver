from setuptools import find_packages, setup

setup(
    name='OptiSolver',
    packages=find_packages(include=['OptiSolver']),
    version='0.1.0',
    description='Optimization Solver with AI',
    author='Berend Wentges',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)