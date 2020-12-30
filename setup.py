# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(
    name='image_resizer',  # Required
    version='1.0.0',  # Required
    description='Resize images to specific filesize',  # Optional
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    author='C. Schaffer',  # Optional
    author_email='cfmschaffer@hotmail.com',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='PIL, images, resizing',  # Optional
    packages=find_packages(),  # Required
    python_requires='>=3.5, <4',
    install_requires=['PIL'],  # Optional
)