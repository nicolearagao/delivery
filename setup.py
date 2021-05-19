from setuptools import setup, find_packages


def read(filename):
    requirements = []
    for requirement in open(filename).readlines():
        requirements.append(requirement.strip())
    return requirements


setup(
    author="Nicole Aragão",
    name="delivery",
    version="0.1.0",  # major(próxima versão), minor(versão de fato), patch (correção bug)
    description="Delivery app with flask-admin dashboard",
    packages=find_packages(exclude="./venv"),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={
        "dev": read("requirements-dev.txt")
    }
)
