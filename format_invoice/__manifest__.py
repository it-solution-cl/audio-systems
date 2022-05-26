# -*- coding: utf-8 -*-
{
    'name': 'Report Invoice',
    'version': '14.3',
    'description': 'Format Invoice',
    'author': 'IT Solution SpA',
    'website': 'https://it-solution.cl/',
    'license': 'LGPL-3',
    'category': 'account',
    'depends': [
        'base',
        'account',
        'sale',
        'purchase',
        'base_setup',
        'l10n_cl_edi'
    ],
    'data': [
        'views/template.xml',
        'views/report_purchase_template.xml',
        'views/report_invoice_action.xml',
        'views/report_invoice_template.xml', 
        'views/reporte.xml', 
                  
        
    ],
    'auto_install': False,
    'application': False,
}
