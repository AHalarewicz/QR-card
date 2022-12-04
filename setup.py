from distutils.core import setup


def readme():
    """Import the README.md Markdown file and try to convert it to RST format."""
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        with open('README.md') as readme_file:
            return readme_file.read()


setup(
    name='qrcode',
    version='0.1',
    description='Generate QR Codes for cards.',
    long_description=readme(),
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    # Substitute <github_account> with the name of your GitHub account
    url='https://https://github.com/AHalarewicz/qr-card',
    author='Adrian Halarewicz',  # Substitute your name
    author_email='alhalarewicz@gmail.com',  # Substitute your email
    license='MIT',
    packages=['qrcode'],
)