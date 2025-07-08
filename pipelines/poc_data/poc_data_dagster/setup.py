from setuptools import find_packages, setup

setup(
    name="poc_data_dagster",
    packages=find_packages(exclude=["poc_data_dagster_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
