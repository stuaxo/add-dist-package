from distutils.core import setup
setup(name='add-dist-packages',
      version='0.1',
      scripts=['add-dist-package'],
      license='LICENSE',
      description='Create symlinks to system packages inside the current or specified virtualenv'
      long_description=open('README.txt').read(),
      author='Stuart Axon',
      author_email='stu.axon+adp@gmail.com',
      )
