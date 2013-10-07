from setuptools import setup, find_packages
setup(
    name = "overkill-extra-mail",
    version = "0.1",
    install_requires=["overkill"],
    packages = find_packages(),
    namespace_packages = ["overkill", "overkill.extra"],
    author = "Steven Allen",
    author_email = "steven@stebalien.com",
    description = "Maildir data source and notification sink for overkill.",
    extras_require = {
        "Notification Sink": ["overkill-extra-notify"]
    },
    license = "GPL3",
    url = "http://stebalien.com"
)
