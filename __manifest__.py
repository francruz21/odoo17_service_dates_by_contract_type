{
    'name': 'Purchase Sync Dates',
    'version': '1.0',
    'depends': ['purchase', 'purchase_requisition','pn_settings','base'],
    'data': [
        'views/purchase_order_views.xml',
    ],
    'category': 'Purchases',
    'description': 'Sincroniza fechas de entrega y finalización desde la requisición a la orden de compra.',
    'installable': True,
    'auto_install': False,
    'application': False,
}
