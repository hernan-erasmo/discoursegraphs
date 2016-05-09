#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <discoursegraphs.programming@arne.cl>

"""
This module contains code to convert discourse graphs into bracketed strings
for FREQT.
"""

import codecs
import os

from discoursegraphs import istoken
from discoursegraphs.readwrite.tree import sorted_bfs_successors
from discoursegraphs.util import create_dir


def node2freqt(docgraph, node_id, child_str='', include_pos=False):
    """convert a docgraph node into a FREQT string."""
    node_attrs = docgraph.node[node_id]
    if istoken(docgraph, node_id):
        token_str = node_attrs[docgraph.ns+':token']
        if include_pos:
            pos_str = node_attrs.get(docgraph.ns+':pos', '')
            return u"({pos}({token}){child})".format(
                pos=pos_str, token=token_str, child=child_str)
        else:
            return u"({token}{child})".format(token=token_str, child=child_str)

    else:  # node is not a token
        label_str=node_attrs.get('label', '')
        return u"({label}{child})".format(label=label_str, child=child_str)


def docgraph2freqt(docgraph, root=None, successors=None, include_pos=False):
    """convert a docgraph into a FREQT string."""
    if root is None:
        root = docgraph.root
    if successors is None:
        successors = sorted_bfs_successors(docgraph, root)

    if root in successors:
        embed_str = u"".join(docgraph2freqt(docgraph, child, successors,
                                            include_pos=include_pos)
                             for child in successors[root])
        return node2freqt(docgraph, root, embed_str, include_pos=include_pos)
    else:
        return node2freqt(docgraph, root, include_pos=include_pos)


def write_freqt(docgraph, output_filepath, include_pos=False):
    """convert a docgraph into a FREQT input file (one sentence per line)."""
    path_to_file = os.path.dirname(output_filepath)
    if not os.path.isdir(path_to_file):
        create_dir(path_to_file)
    with codecs.open(output_filepath, 'w', 'utf-8') as output_file:
        for sentence in docgraph.sentences:
            output_file.write(docgraph2freqt(docgraph, sentence,
                              include_pos=include_pos)+'\n')
