# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID, _

class ColegioGrado(models.Model):
    _name = "colegio.grado"
    _rec_name = "nombre"


    nombre = fields.Char('Nombre')
    # seccion_ids = fields.Many2many('colegio.seccion',string='Secciones')
    # seccion_id = fields.Many2one('colegio.seccion')
    # jornada_id = fields.Many2one('colegio.jornada')
    # ciclo_id = fields.Many2one('colegio.ciclo')
    geducar_id = fields.Integer('Geducar id')


class ColegioSeccion(models.Model):
    _name = "colegio.seccion"
    _rec_name = 'nombre'

    nombre = fields.Char('Nombre')
    geducar_id = fields.Integer('Geducar id')

    # @api.model
    # def create(self, vals):
    #     seccion = super(ColegioSeccion, self).create(vals)
    #     return seccion

    # @api.multi
    # def write(self, values):
    #     return super(ColegioSeccion, self).write(values)
# class ColegioSeccionLine(models.Model):
#     _name = "colegio.seccion.line"

#     seccion_id = fields.Many2one('colegio.seccion','Seccion')
#     geducar_id = fields.Integer('Geducar id')

class ColegioJornada(models.Model):
    _name = "colegio.jornada"
    _rec_name = "nombre"

    nombre = fields.Char('Nombre')
    geducar_id = fields.Integer('Geducar id')

class ColegioCiclo(models.Model):
    _name = "colegio.ciclo"
    _rec_name = "nombre"

    nombre = fields.Integer('Ciclo')
    geducar_id = fields.Integer('Geducar id')
