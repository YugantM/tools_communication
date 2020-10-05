from distutils.core import setup
setup(
  name = 'target',         
  packages = ['target'],   
  version = '1.0',      
  license='MIT',        
  description = '',   
  url = 'https://github.com/YugantM/tools_communication',   
  download_url = 'https://github.com/YugantM/tools_communication.git',
  entry_points = {
              'console_scripts': ['target = target.__main__:main',],
              },
  scripts=['scripts/target'],  
  keywords = ['search', 'json'],  
  
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)