# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import

__author__ = 'Matthew L. Bendall'
__copyright__ = "Copyright (C) 2017 Matthew L. Bendall"

def get_annotation_class(annotation_class_name):
    if annotation_class_name == 'htseq':
        from ._annotation_htseq import _AnnotationHTSeq
        return _AnnotationHTSeq
    elif annotation_class_name == 'intervaltree':
        from ._annotation_intervaltree import _AnnotationIntervalTree
        return _AnnotationIntervalTree
    else:
        raise NotImplementedError('Choices are "htseq" or "intervaltree".')