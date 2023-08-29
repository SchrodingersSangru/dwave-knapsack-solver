from setuptools import setup, find_packages

setup(
    name='dwave-knapsack-solver',
    version='0.1',
    
    description='A knapsack problem solver package using dwave quantum annealer',
	author='Sangram Deshpande', 
	author_email='deshpande.sangram156@gmail.com',
	
    packages= ['dwave-knapsack-solver'], #find_packages(),
    install_requires=[
        'dwave-ocean-sdk',
        'random2', 
        'dwave.system'
        # Add any necessary dependencies
    ],
)

