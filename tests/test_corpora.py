#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <discoursegraphs.programming@arne.cl>

import pkgutil
from tempfile import NamedTemporaryFile, mkdtemp

import pytest

import discoursegraphs as dg
from discoursegraphs.corpora import pcc


maz_1423 = pcc['maz-1423']


def test_write_brackets():
    """convert a PCC document into a brackets file."""
    temp_file = NamedTemporaryFile()
    temp_file.close()
    dg.write_brackets(maz_1423, temp_file.name)


def test_write_brat():
    """convert a PCC document into a brat file."""
    temp_file = NamedTemporaryFile()
    temp_file.close()
    dg.write_brat(maz_1423, temp_file.name)


def test_write_exb():
    """convert a PCC document into a exb file."""
    temp_file = NamedTemporaryFile()
    temp_file.close()
    dg.write_exb(maz_1423, temp_file.name)


def test_write_graphml():
    """convert a PCC document into a graphml file."""
    temp_file = NamedTemporaryFile()
    temp_file.close()
    dg.write_graphml(maz_1423, temp_file.name)


def test_write_gexf():
    """convert a PCC document into a gexf file."""
    temp_file = NamedTemporaryFile()
    temp_file.close()
    dg.write_gexf(maz_1423, temp_file.name)


def test_write_paula():
    """convert a PCC document into a paula file."""
    temp_dir = mkdtemp()
    dg.write_paula(maz_1423, temp_dir)


@pytest.mark.slowtest
def test_pcc():
    """
    create document graphs for all PCC documents containing all annotation
    layers.
    """
    assert len(pcc.document_ids) == 176

    for doc_id in pcc.document_ids:
        docgraph = pcc[doc_id]
        assert isinstance(docgraph, dg.DiscourseDocumentGraph)
