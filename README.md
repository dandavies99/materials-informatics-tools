# Materials Screening and Informatics Tools
A collection of tools for high-throughput materials screening and informatics.

Early stages work in progress.

## Examples
### Pre-DFT calculation 
 - **Structure predictor:** Generate a list of suggested structures for a given set of species using Pymatgen. Includes example of generating a pool of parent structures, as well as using multiprocessing to predict structures for many sets of species.

- **Competing phase generator:** Read in a list of pymatgen structures and find likely decomposition products. These can then be exported as a reduced set of structures necessary to calculate to get reliable E_hull values for the original set of structures.

### VASP Calculation setup / automation
- **VASP input generator:** Use pymatgen to generate sets of VASP input files for a list of structures. 

- **Atomate structure optimization:** Use the Atomate package to set up a set of typical, simple DFT structure optimization calculations. 

- **Atomate hybrid calculation:** Use the Atomate package to set up a set of typical static HSE06 calculations to get a band gap using a uniform k-point grid. 

### Misc
- **Get all structure IDs:** Use the MP API to make a query and save a list of MPIDs for future use. 

## Materials Project API
Much of the code relies on programmatic access to the Materials Project. It is recommended to add this as an environemnt variable, e.g. in your `~/.bash_profile`/`~/.bashrc`: `export MP_API_KEY=xxxxxxxxxxxxxx`. In doing so, the scripts should work as-is.  

## Dependencies
Not all examples and functions require all dependencies.
- Pymatgen
- SMACT
- Atomate
- Fireworks
- Scikit-learn
