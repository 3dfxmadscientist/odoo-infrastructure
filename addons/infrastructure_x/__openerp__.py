# -*- coding: utf-8 -*-
{
    'name': 'Infrastructure Management',
    'version': '1.0',
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'description': """
Infrastructure Management
=========================
    """,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'images': [
    ],
    'depends': [
        'infrastructure'
    ],
    'data': [
        'view/server_view.xml',
    ],
    'demo': [
        'data/demo/res.partner.csv',
        'data/demo/infrastructure.server.csv',
        'data/demo/infrastructure.environment_version.csv',
        'data/demo/infrastructure.environment.csv',
        'data/demo/infrastructure.db_filter.csv',
        'data/demo/infrastructure.instance.csv',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: