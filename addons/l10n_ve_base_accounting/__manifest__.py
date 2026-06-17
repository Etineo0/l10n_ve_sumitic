{
    'name': 'Localización Venezolana - Base Contable',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Localizations',
    'summary': 'Configuraciones base para la contabilidad en Venezuela',
    'author': 'SUMITIC',
    'depends': ['account'],  # <--- AQUÍ ESTÁ LA CLAVE PARA QUE INSTALE CONTABILIDAD
    'data': [
        'data/account_chart_template.xml',
    ],
    'installable': True,
    'application': True, # Cambiado a True para que aparezca en el menú de Apps
    'license': 'LGPL-3',
}
