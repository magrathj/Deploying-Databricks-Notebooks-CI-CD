import os
from setuptools import setup, find_packages

def get_version():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(curr_dir, "version.txt")) as version_file:
        return version_file.read().strip()

setup(
    name="poc-pyspark-docker".replace("-", "_"),
    version=get_version(),
    description="ETL to generate nyork taxi data",
    author="priyan",
    author_email="priyan@infinitelambda.com",
    url="git@gitlab.infinitelambda.com:infinitelambda/poc-docker_pyspark_databricks_aws.git",
    platforms="any",
    package_data={"src": ["job_data/*"]},
    packages=find_packages(exclude=["tests", "tests.*"]),
)