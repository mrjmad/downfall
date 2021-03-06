# -*- coding:utf-8 -*-

"""
  Definition of downfall errors

  Author: Tristan Colombo <tristan.colombo@info2dev.com>
                          (@TristanColombo)

  Date: 09-26-2013 

  Last modification: 09-26-2013

  Licence: GNU GPL v3
"""

class Error(object):
 
  # Input/Output Errors (writing, moving or copying file or directory)
  IOFILE = 1
  # Syntax error in yaml file
  YAML_SYNTAX = 2
