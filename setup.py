from setuptools import setup

setup(
    name="remoteev3",
    version="0.1.0",
    description="Remote API for ev3dev",
    author="Maciej Stryjewski",
    author_email="stryjewski.mac@gmail.com",
    packages=["remoteev3"],
    install_requires=[
        "rpyc==6.0.2",
    ],
)
