from odoo import models, fields, api

class TaskTask(models.Model):
    _name = 'task.task'
    _description = 'Tâche'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nom', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    board_id = fields.Many2one('task.board', string='Tableau', required=True, tracking=True)
    assigned_to = fields.Many2one('res.users', string='Assigné à', tracking=True)
    state = fields.Selection([
        ('todo', 'À Faire'),
        ('in_progress', 'En Cours'),
        ('done', 'Terminé'),
    ], string='État', default='todo', tracking=True)
    deadline = fields.Datetime(string='Échéance', tracking=True)
    priority = fields.Selection([
        ('low', 'Faible'),
        ('medium', 'Moyenne'),
        ('high', 'Élevée'),
    ], string='Priorité', default='medium', tracking=True)
    attachment_ids = fields.Many2many('ir.attachment', string='Pièces Jointes')

    def action_mark_done(self):
        for task in self:
            task.state = 'done'
