from setuptools import setup, find_packages

test_deps = [
    "pip>=21.3.1",
]

serve_deps = [
    "dploy-kickstart>=0.1.5",
]

extras = {"test": test_deps, "serve": serve_deps}


setup(
    name="real-estate-valuation",
    version="0.1.0",
    url="github.com/kolahimself/real-estate-valuation",
    author="James Kola Ojoawo",
    author_email="ojameskola03@gmail.com",
    description="A simple implementation of gradient boosting regression on real estate transactions using scikit learn",
    packages=find_packages(),
    install_requires=["pandas>=1.4.3", "scikit-learn>=1.1.1", 'joblib>=1.1.0', "matplotlib>=3.5.1", "numpy>=1.23.1", "openpyxl>=3.0.9"]

)
