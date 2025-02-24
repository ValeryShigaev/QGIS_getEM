# -*- coding: utf-8 -*-
"""
/***************************************************************************
 getEM
                                 A QGIS plugin
 Allows you to get maps from EM
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-11-18
        copyright            : (C) 2024 by shigaevaler@gmail.com
        email                : shigaevaler@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load getEM class from file getEM.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .getEM import getEM
    return getEM(iface)
