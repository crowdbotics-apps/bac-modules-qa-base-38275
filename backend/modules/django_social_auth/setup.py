from setuptools import setup
from setuptools.command.build import build


# Override build command
class BuildCommand(build):
    def initialize_options(self):
        build.initialize_options(self)
        self.build_base = "/tmp"


setup(
    name="cb_django_social_auth",
    version="0.1",
    packages=["social_auth"],
    install_requires=["dj-rest-auth==2.2.5"],
    cmdclass={"build": BuildCommand},
)
