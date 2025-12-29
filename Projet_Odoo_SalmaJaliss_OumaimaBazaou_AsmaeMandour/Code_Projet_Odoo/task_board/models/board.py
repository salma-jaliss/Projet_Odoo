from odoo import models, fields, api

class TaskBoard(models.Model):
    _name = 'task.board'
    _description = 'Tableau de Tâches'

    name = fields.Char(string='Nom', required=True)
    description = fields.Text(string='Description')
    user_ids = fields.Many2many('res.users', string='Membres')

    # Computed fields for task counts
    todo_count = fields.Integer(string='À Faire', compute='_compute_task_counts', store=True)
    in_progress_count = fields.Integer(string='En Cours', compute='_compute_task_counts', store=True)
    done_count = fields.Integer(string='Terminé', compute='_compute_task_counts', store=True)

    @api.depends('task_ids.state')
    def _compute_task_counts(self):
        for board in self:
            tasks = board.task_ids
            board.todo_count = len(tasks.filtered(lambda t: t.state == 'todo'))
            board.in_progress_count = len(tasks.filtered(lambda t: t.state == 'in_progress'))
            board.done_count = len(tasks.filtered(lambda t: t.state == 'done'))

    task_ids = fields.One2many('task.task', 'board_id', string='Tâches')
