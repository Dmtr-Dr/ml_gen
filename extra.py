from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt

def mol_image(chemical_formula):
  molecule = Chem.MolFromSmiles(chemical_formula)
  img = Draw.MolToImage(molecule)
  img_matplotlib = Draw.MolToMPL(molecule)
  return(img_matplotlib)
