#     Copyright 2014 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
from setuptools import setup

setup(
    name='security_monkey',
    version='0.8.0',
    long_description=__doc__,
    packages=['security_monkey'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'APScheduler==2.1.2',
        'Flask==0.10.1',
        'Flask-Mail==0.9.0',
        'Flask-Migrate==1.3.1',
        'Flask-Principal==0.4.0',
        'Flask-RESTful==0.3.3',
        'Flask-SQLAlchemy==1.0',
        'Flask-Script==0.6.3',
        # 'Flask-Security==1.7.4',
        'Flask-Security-Fork==1.8.2',
        'Flask-WTF>=0.14.2',
        'Jinja2>=2.8.1',
        'SQLAlchemy==0.9.2',
        'boto>=2.41.0',
        'ipaddr==2.1.11',
        'itsdangerous==0.23',
        'psycopg2==2.6.2',
        'bcrypt==3.1.2',
        'Sphinx==1.5.1',
        'gunicorn==18.0',
        'cryptography==1.7.1',
        'boto3>=1.4.2',
        'botocore>=1.4.81',
        'dpath==1.3.2',
        'pyyaml==3.11',
        'jira==0.32',
        'cloudaux>=1.1.3',
        'joblib>=0.9.4',
        'pyjwt>=1.01',
    ],
    extras_require = {
        'onelogin': ['python-saml>=2.2.0'],
        'tests': [
            'nose==1.3.0',
            'mixer==5.5.7',
            'mock==1.0.1',
            'moto==0.4.30',
            'freezegun>=0.3.7',
            'mixer==5.5.7'
        ]
    }
)
