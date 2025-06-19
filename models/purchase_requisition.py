from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    descripcion = fields.Char(string="Descripcion")