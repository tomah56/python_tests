from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='bobpack',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package requires here
    ],
    author='ttokesi',
    author_email='t.tomah@hotmail.com',
    description='This is a test package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tomah56',
    license='MIT',  # or any other license you prefer
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='bob',
    # Add other package metadata like author, description, etc.
)
