from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    service_delivery_date = fields.Date(
        string="Fecha de Inicio de Servicio",
        compute="_compute_service_dates",
        store=True,
        readonly=True
    )
    service_completion_date = fields.Date(
        string="Fecha de Finalización de Servicio",
        compute="_compute_service_dates",
        store=True,
        readonly=True
    )




    
    @api.depends('requisition_id', 'x_studio_tipo_de_contrato')
    def _compute_service_dates(self):
        for record in self:
            if record.x_studio_tipo_de_contrato and record.x_studio_tipo_de_contrato.id in [2, 4] and record.requisition_id:
                req = record.requisition_id
                record.service_delivery_date = req.service_delivery_date
                record.service_completion_date = req.service_completion_date
              
            else:
                record.service_delivery_date = False
                record.service_completion_date = False
     




