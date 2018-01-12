# -*- coding: utf-8 -*-

"""
# Model untuk mengkostumisasi hr.employee,
# agar ada informasi tambahan tentang berkas yang diunggah
# author @CakJuice <hd.brandoz@gmail.com>
"""

from odoo import models, fields, api

class HrEmployeeInherit(models.Model):
	_inherit = 'hr.employee'

	# buat field count_attachment, untuk menampilkan jumlah berkas yang ada.
	count_attachment = fields.Integer(compute='_compute_attachment', string="Berkas")

	@api.multi
	def _compute_attachment(self):
		for employee in self:
			employee.count_attachment = self.env['ir.attachment'].search_count([
				('res_model', '=', employee._name),
				('res_id', '=', employee.id),
			])

	@api.multi
	def action_view_employee_attachment(self):
		"""
		Sebuah action untuk sebuah button,
		yang digunakan untuk menampilkan daftar berkas yang diunggah
		"""
		return {
			'name': 'Attachment',
			'domain': [('res_model', '=', self._name), ('res_id', '=', self.id)],
			'res_model': 'ir.attachment',
			'type': 'ir.actions.act_window',
			'view_mode': 'kanban,tree,form',
			'view_type': 'form',
			'limit': 80,
			'context': {
				'default_res_model': self._name,
				'default_res_id': self.id,
			}
		}