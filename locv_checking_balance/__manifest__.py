# -*- coding: utf-8 -*-
{
    'name': "Informe Balance de Comprobacion",

    'summary': """Module_checking_Balance""",

    'description': """
      Generación del informe financiero Balance de Comprobación, en
formato PDF y en XLS.
    """,
    'version': '1.0',
    'author': 'Localizacion Venezolana',
    'category': 'Tools',

    # any module necessary for this one to work correctly.
    'depends': ['base', 'account', 'locv_withholding_islr', 'locv_retention_islr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_checking_balance.xml',
        'report/report_checking_balance_pdf.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    'application': True,
}
