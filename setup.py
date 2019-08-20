import setuptools

setuptools.setup(
    name="govuk-frontend-jinja",
    version="0.2.0-alpha",
    author="Laurence de Bruxelles",
    author_email="author@example.com",
    description="Tools to use the GOV.UK Design System with Jinja-powered Python apps",
    packages=setuptools.find_packages(),
    install_requires=[
        "jinja2",
    ],
    extras_require={
        "Flask": ["Flask"],
    },
)
