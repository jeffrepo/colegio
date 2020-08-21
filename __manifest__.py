# -*- coding: utf-8 -*-
{
    'name': "Colegio",

    'summary': """ Módulo para colegios""",

    'description': """
        Módulo para colegios
    """,

    'author': "SISPAV",
    'website': "http://www.sispav.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base','product','account'],

    'data': [
        'views/colegio_views.xml',
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
        'views/account_view.xml',
    ],
}
