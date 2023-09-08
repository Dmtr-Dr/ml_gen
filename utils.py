from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
import numpy as np
import deepchem as dc
import os
from deepchem.molnet import load_hiv, featurizers
from deepchem.feat.molecule_featurizers import MolGraphConvFeaturizer


def set_checkpoint(model, model_type: str):
    """Set checkpoints from dir"""
    if model_type == 'hiv':
        os.chdir('checkpoints/checkpoints_hiv')
        model.restore(checkpoint='checkpoint1.pt')

    elif model_type == 'qm':
        os.chdir('checkpoints')
        model.restore(model_dir='checkpoints_qm')

    else:
        print('UNKNOWN MODEL')

    os.chdir('../..')


def txt_parser(file: str) -> list:
    """Parse SMILES from .txt"""
    smiles_lst = []
    with open(file, 'r') as f:
        content = f.readlines()

    for s in content:
        smiles_lst.append(s.replace('\n', ''))

    return smiles_lst


def txt_construct(smiles_lst, predict_hiv):
    with open('report_test.txt', 'w') as f:
        for i in range(0, len(smiles_lst)):
            f.writelines(f'Compound #{i + 1}\n')
            f.writelines(f'{smiles_lst[i]}\n')
            f.writelines(f'Inactive: {predict_hiv[i][0][0]}, Active: {predict_hiv[i][0][1]}\n')

