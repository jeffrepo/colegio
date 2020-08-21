# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID, _

class Partner(models.Model):
    _inherit = "res.partner"

    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino')], 'Género')
    # colegio_historial = fields.One2many('colegio.historial','partner_id',string='Secciones')
    matricula = fields.Char('Matricula')
    grado_id = fields.Many2one('colegio.grado','Grado', track_visibility='onchange')
    seccion_id = fields.Many2one('colegio.seccion','Seccion', track_visibility='onchange')
    jornada_id = fields.Many2one('colegio.jornada','Jornada', track_visibility='onchange')
    ciclo_id = fields.Many2one('colegio.ciclo','Ciclo', track_visibility='onchange')
    geducar_id = fields.Integer('Geducar id', track_visibility='onchange')
