##
#    This file is part of Overkill-mail.
#
#    Overkill-mail is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Overkill-mail is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Overkill-mail.  If not, see <http://www.gnu.org/licenses/>.
##

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
