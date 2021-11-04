import setuptools

setuptools.setup(
    name="govuk-frontend-jinja",
    version="0.5.8-alpha",
    author="Laurence de Bruxelles",
    author_email="author@example.com",
    description="Tools to use the GOV.UK Design System with Jinja-powered Python apps",
    packages=setuptools.find_packages(),
    install_requires=[
        "jinja2~=3.0",
    ],
    extras_require={
        "Flask": ["Flask"],
        "dev": [
            "pytest",
            "pytest-flakes",
            "pytest-helpers-namespace",
        ],
    },
)
