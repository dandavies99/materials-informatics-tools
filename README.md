# Materials Screening and Informatics Tools
A collection of tools for high-throughput materials screening and informatics.

Early stages work in progress.

## Examples
 - **Structure Predictor:** Generate a list of suggested structures for a given set of species using Pymatgen. Includes example of generating a pool of parent structures, as well as using multiprocessing to predict structures for many sets of species.

## Materials Project API
Much of the code relies on programmatic access to the Materials Project. It is recommended to add this as an environemnt variable, e.g. in your `~/.bash_profile`/`~/.bashrc`: `export MP_API_KEY=xxxxxxxxxxxxxx`. In doing so, the scripts should work as-is.  

## Dependencies
Not all examples and functions require all dependencies.
- Pymatgen
- SMACT
- Atomate
- Fireworks
- Scikit-learn
