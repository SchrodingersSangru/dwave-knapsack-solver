from setuptools import setup

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setup(
    name='dwave_knapsack_solver',
    version='1.1.0',
    license='MIT',    
    description='A knapsack problem solver package using dwave quantum annealer',
    author='Sangram Deshpande', 
    author_email='deshpande.sangram156@gmail.com',
    url = 'https://github.com/SchrodingersSangru/quantum-knapsack-solver/archive/refs/tags/1.1.0.zip',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/SchrodingersSangru/quantum-knapsack-solver/archive/refs/tags/1.1.0.tar.gz',
    keywords = ['knapsack_problem', 'Quantum_annealing', 'Quantum_genetic_algorithm', 'dwave_knapsack_solver', 'solve_knapsack_using_quantum', 'dwave_package'],     
    packages= ['dwave-knapsack-solver'], #find_packages(),
    install_requires=[
        'dwave-ocean-sdk',
        'random2',
    ],
    python_requires='>=3.6',

 classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Developers',      # Define that your audience is developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   # Again, pick a license

    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
## write test cases to it first. \\
