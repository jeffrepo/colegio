# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _
from odoo.tools import float_is_zero, float_compare, pycompat
from odoo.tools.misc import formatLang

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    grado_id = fields.Many2one('colegio.grado','Grado', store=True)
    seccion_id = fields.Many2one('colegio.seccion','Seccion', store=True)
    jornada_id = fields.Many2one('colegio.jornada','Jornada', store=True)
    ciclo_id = fields.Many2one('colegio.ciclo','Ciclo', store=True)
    metodo_pago_id = fields.Many2one('account.journal','Metodo de pago')

    # @api.onchange('partner_id') # if these fields are changed, call method
    # def check_change(self):
    #     if self.partner_id:
    #         self.grado_id = self.partner_id.grado_id
    #         self.seccion_id = self.partner_id.seccion_id
    #         self.jornada_id = self.partner_id.jornada_id
    #         self.ciclo_id = self.partner_id.ciclo_id
