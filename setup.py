import setuptools

setuptools.setup(
    name="dagster_proj",
    packages=setuptools.find_packages(exclude=["dagster_proj_tests"]),
    install_requires=[
        "dagster==0.11.9",
        "dagit==0.11.9",
        "pytest",
    ],
)
