# coding: utf-8
##############################################################################


import ast
import datetime, time

from odoo.tools.translate import _
from odoo import models, fields, api
#



class PurchaseOrderInnherit(models.Model):
    _inherit = 'purchase.order'


    partner_id = fields.Many2one('res.partner',
                                 #                                 states={'draft': [('readonly', False)]},
                                 domain="['|',('customer_rank', '>', 0),('supplier_rank', '>', 0)]",
                                 string='Partner')

    rif = fields.Char(string="RIF", related='partner_id.vat', store=True, states={'draft': [('readonly', True)]})

    identification_id = fields.Char('Documento de Identidad', related='partner_id.identification_id', size=20,
                                     store=True, states={'draft': [('readonly', True)]})

    nationality = fields.Selection([
        ('V', 'Venezolano'),
        ('E', 'Extranjero'),
        ('P', 'Pasaporte')], string="Tipo Documento", related='partner_id.nationality', store=True,
        states={'draft': [('readonly', True)]})

    people_type_company = fields.Selection([
        ('pjdo', 'PJDO    Persona Jurídica Domiciliada'),
        ('pjnd', 'PJND    Persona Jurídica No Domiciliada')
    ], 'Tipo de Persona', related='partner_id.people_type_company')


    people_type_individual = fields.Selection([
        ('pnre', 'PNRE    Persona Natural Residente'),
        ('pnnr', 'PNNR    Persona Natural No Residente')], 'Tipo de Persona', related='partner_id.people_type_individual')

    company_type = fields.Selection(string='Company Type',
                                     selection=[('person', 'Individual'), ('company', 'Company')], related='partner_id.company_type')
