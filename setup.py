import setuptools

setuptools.setup(
    name="govuk-frontend-python",
    version="0.1.0-alpha",
    author="Laurence de Bruxelles",
    author_email="author@example.com",
    description="Tools to use the GOV.UK Design System with Python apps",
    packages=setuptools.find_packages(),
    install_requires=[
        "jinja2",
    ],
    extras_require={
        "Flask": ["Flask"],
    },
)
