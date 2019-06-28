import pymatgen
from pymatgen.analysis.bond_valence import BVAnalyzer
from pymatgen import Structure, Specie
import os
from pymatgen.analysis.structure_prediction.substitutor import Substitutor
from multiprocessing import Pool

bva = BVAnalyzer()

def _decorate_structure(structure):
    try:
        decorated_struc = bva.get_oxi_state_decorated_structure(structure)
    except:
        decorated_struc = None
    return decorated_struc

def decorate_structures(structures, nproc=4, verbose=False):
    with Pool(processes=nproc) as pool:
        decorated_structures = pool.map(_decorate_structure, structures)

    # Work out how many were successfully decorated
    not_decorated = [i for i in decorated_structures if i is None]
    n_decorated = len(decorated_structures) - len(not_decorated)
    print("{}  out of {} structures successfully decorated with oxidation states".format(n_decorated,
                                                                            len(decorated_structures)))

    if verbose:
        undecoratable = []
        for n,i in enumerate(decorated_structures):
            if i == None:
                undecoratable.append(structures[n].composition.formula)
        print("Compounds that could not be decorated: ")
        print(undecoratable)

    return(decorated_structures)
