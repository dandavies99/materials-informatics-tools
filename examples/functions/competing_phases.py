from pymatgen.analysis.phase_diagram import PhaseDiagram, PDEntry
from pymatgen import Composition

def get_competing(entry, competing_list):
    competing_phases = []
    for i in competing_list:
        if i['chemsys'].issubset(entry['chemsys']):
            competing_phases.append(i)
    return competing_phases

def get_decomp_product_ids(structures, competing_phases):
    # Create phase diagrams for each of the new structure chemical systems
    phase_diagrams = []
    for competing in competing_phases:
        # Add competing phases
        entries = [PDEntry(Composition(i['full_formula']), i['final_energy'],
                           name=i['task_id']) for i in competing]
        pd = PhaseDiagram(entries)
        phase_diagrams.append(pd)

    # Put new structures on phase diagram to get the set of decomp products
    all_decomp_prods = []
    for new_struc, pd in zip(structures,phase_diagrams):
        comp = new_struc['structure'].composition.element_composition
        decomp_prods = pd.get_decomposition(comp=comp)
        all_decomp_prods.extend([i.name for i in decomp_prods])

    # Reduce decomposition products to unique set
    all_decomp_prods = list(set(all_decomp_prods))
    print('{} unique competing phases to calculate'.format(len(all_decomp_prods)))
    return(all_decomp_prods)
