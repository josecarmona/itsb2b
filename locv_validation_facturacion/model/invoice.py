# coding: utf-8
from odoo import models, fields, api
from odoo.tools.translate import _

from datetime import datetime,date
from dateutil import relativedelta
import logging
_logger = logging.getLogger(__name__)

class AccountMoveInherit(models.Model):
    _inherit = 'account.move'


    ################################### ----Proveedores----####################################################

    nro_planilla_impor = fields.Char('Nro de Planilla de Importacion', size=25)
    nro_expediente_impor = fields.Char('Nro de Expediente de Importacion', size=25)
    fecha_importacion = fields.Date('Fecha de la planilla de Importación')

    supplier_rank1 = fields.Integer(related='partner_id.supplier_rank')

    ################################### ----------Clientes--------------###########################################

    customer_rank1 = fields.Integer(related='partner_id.customer_rank')

    ################################### -------------AMBOS-----------------########################################
    partner_id = fields.Many2one('res.partner', readonly=True,
#                                 states={'draft': [('readonly', False)]},
                                 domain="['|',('customer_rank', '>', 0),('supplier_rank', '>', 0)]",
                                 string='Partner')

    rif = fields.Char(string="RIF", related='partner_id.vat', store=True, states={'draft': [('readonly', True)]})

    identification_id1 = fields.Char('Documento de Identidad', related='partner_id.identification_id', size=20, store=True, states={'draft': [('readonly', True)]})

    nationality1 = fields.Selection([
        ('V', 'Venezolano'),
        ('E', 'Extranjero'),
        ('P', 'Pasaporte')], string="Tipo Documento", related='partner_id.nationality', store=True, states={'draft': [('readonly', True)]})

    people_type_company1 = fields.Selection([
        ('pjdo', 'PJDO    Persona Jurídica Domiciliada'),
        ('pjnd', 'PJND    Persona Jurídica No Domiciliada')
    ], 'Tipo de Persona')

    people_type_individual1 = fields.Selection([
    ('pnre', 'PNRE    Persona Natural Residente'),
    ('pnnr', 'PNNR    Persona Natural No Residente')], 'Tipo de Persona')
    company_type1 = fields.Selection(string='Company Type',
        selection=[('person', 'Individual'), ('company', 'Company')])
    create_invoice =  fields.Boolean('crear factura', default=False)

    ###----------------------------------Funciones-----------------------###########
    @api.onchange('partner_id')
    def _compute_partner(self):
        self.people_type = (self.partner_id.people_type_company)
        self.customer_rank1 = self.partner_id.customer_rank
        self.supplier_rank1 = self.partner_id.supplier_rank
        self.people_type_company1 = (self.partner_id.people_type_company)
        self.people_type_individual1 = (self.partner_id.people_type_individual)
        self.company_type1 = (self.partner_id.company_type)
        return

