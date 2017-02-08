# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2017 Pravitha V.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


# -*- coding: utf-8 -*-
{
    'name': 'Export Excel',

    'summary': """
        Exports reports in excel format
        """,

    'description': """
Export Excel Report
====================
Module to export current active tree view in to an excel report
   
    """,

    'author': "Pravitha V",
    'website': "http://www.qpr.qa",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Web',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/export_excel_view.xml',
        ],
    
    'qweb': [
        
        'static/src/xml/export_excel.xml'
        ],

    'installable': True,
    'auto_install': False,
    'application': True,
    'web_preload': False,
}