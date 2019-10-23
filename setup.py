from setuptools import setup

setup(name='drivel',
    version='0.0333',
    description='A python wrapper for Google Drive use in Linux',
    url='https://github.com/Dual-Exhaust/drivel',
    author='Dual-Exhaust',
    author_email='kylecsacco@gmail.com',
    license='MIT',
    packages=['drivel'],
    scripts=['bin/drlist', 'bin/drget'],
    install_requires=[
        'google-api-python-client',
        'google-auth',
        'google-auth-httplib2',
        'google-auth-oauthlib'],
    include_package_data=True,
    zip_safe=False)
