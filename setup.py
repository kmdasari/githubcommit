import setuptools

setuptools.setup(
    name="githubcommit",
    version='0.1.0',
    url="https://github.com/8451/githubcommit",
    author="Shaleen Anand Taneja - modified by Krishna Dasari",
    description="Jupyter extension to enable user push notebooks to a git repo",
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil',
        'notebook',
        'gitpython'
    ],
    package_data={'githubcommit': ['static/*']},
)
