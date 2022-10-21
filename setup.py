from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='SEVIA_V1',
    version='0.0.1',
    url='https://github.com/ElisabeteOlimpio/SEVIA_V1.git',
    license='MIT License',
    author='Elisabete Olimpio',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='olimpioelisabete@gmail.com',
    keywords='Pacote',
    description='SEVIA_V1 é uma biblioteca criada para auxiliar o uso dos indices proximais DRAC e MTTC.',
    packages=['SEVIA_V1'],
    install_requires=['numpy'],
)
