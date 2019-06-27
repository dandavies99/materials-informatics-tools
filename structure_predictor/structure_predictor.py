import pymatgen
from pymatgen.analysis.bond_valence import BVAnalyzer
from pymatgen import Structure, Specie
import os
from pymatgen.analysis.structure_prediction.substitutor import Substitutor
from multiprocessing import Pool
from functools import partial

bva = BVAnalyzer()

def _decorate_structure(structure):
    ''' Wrapper for using pymatgen structure decorator en masse.
        Doesn't give an error if a structure can't be decorated,
        just returns None.
    '''
    try:
        decorated_struc = bva.get_oxi_state_decorated_structure(structure)
    except:
        decorated_struc = None
    return decorated_struc

def decorate_structures(structures, nproc=8, verbose=False):
    ''' Decorating structures using multiprocessing.
    '''
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
                undecoratable.append(structures[n].composition.reduced_formula)
        print("Compounds that could not be decorated: ")
        print(undecoratable)

    return(decorated_structures)

def _predict_structure(species):
    ''' Wrapper for using pymatgen structure predictor.
        helper function for predict_structures function.
    '''



def predict_structures(species_list, parent_structures, threshold=1E-6, nproc=8, verbose=False)
    sub = Substitutor(threshold=threshold)
    with Pool(processes=nproc) as pool:
        suggested_strucs = pool.map(_predict_structure, species_list)
