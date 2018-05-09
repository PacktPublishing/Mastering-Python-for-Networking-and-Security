# -*- coding: utf-8 -*-


"""
This file contains main data structures of project
"""

import six

from datetime import datetime


# --------------------------------------------------------------------------
class GlobalParameters:
    """Global parameters of project"""

    # ----------------------------------------------------------------------
    def __init__(self, from_argparse=None, **kwargs):
        """
        Setup parameters from argparser of option by option
        """

        # Auto set config from argparser
        if from_argparse is not None:
            from argparse import Namespace
            if isinstance(from_argparse, Namespace):
                for p_name, p_value in six.iteritems(vars(from_argparse)):
                    setattr(self, p_name, p_value)


# --------------------------------------------------------------------------
class GlobalResults:
    """Data structure for tools execution"""

    # ----------------------------------------------------------------------
    def __init__(self, **kwargs):
        """
        :param start_execution: start execution time and date.
        :type start_execution: date

        :param end_execution: end execution time and date.
        :type end_execution: date
        
        :param execution_status: result of execution status. Available values: "oks"|"errors"|"warnings"]
        :type execution_status: str

        """
        self.start_execution = kwargs.get("start_execution", None)
        self.end_execution = kwargs.get("end_execution", None)
        self.execution_status = kwargs.get("execution_status", "ok")

        # Check types
        if not isinstance(self.start_execution, datetime):
            raise TypeError("Expected datetime, got '%s' instead" % type(self.start_execution))
        if not isinstance(self.end_execution, datetime):
            raise TypeError("Expected datetime, got '%s' instead" % type(self.end_execution))
        if not isinstance(self.execution_status, str):
            raise TypeError("Expected str, got '%s' instead" % type(self.execution_status))
        else:
            execution_status_allowed = ("oks", "errors", "warnings")
            if self.execution_status not in execution_status_allowed:
                raise ValueError("Bad '%s' value for 'execution_status' parameter. Allowed: %s" %
                                 ",".join(execution_status_allowed))
