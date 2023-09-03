from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dwave_knapsack_solver',
    version='1.1.0',
    
    description='A knapsack problem solver package using dwave quantum annealer',
    author='Sangram Deshpande', 
    author_email='deshpande.sangram156@gmail.com',
    

    url = 'https://github.com/SchrodingersSangru/dwave_knapsack_solver',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/SchrodingersSangru/dwave_knapsack_solver/archive/refs/tags/0.1.tar.gz',    # I explain this later on
    keywords = ['knapsack_problem', 'Quantum_annealing', 'Quantum_genetic_algorithm', 'dwave_knapsack_solver', 'solve_knapsack_using_quantum', 'dwave_package'],
        
    packages= ['dwave-knapsack-solver'], #find_packages(),
    install_requires=[
        'dwave-ocean-sdk',
        'random2',
    ],
    python_requires='>=3.6',
)


## write test cases to it first. 