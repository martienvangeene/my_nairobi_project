# -*- coding: utf-8 -*-
# Copyright 2018 Therp BV <https://therp.nl>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "Todo Projects",
    "version": "10.0.1.0.0",
    "author": "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Project",
    "summary": "All the projects I need to do",
    "depends": [
        'project',
        'sale',
    ],
    "data": [
        # 'data/todo_data.xml',
        'data/server_actions.xml',
        'views/templates.xml',
        'views/sale_order.xml',
        'report/project_todo_report.xml',
        'report/sale_order_report.xml',
        # 'security/ir.model.access.csv',
    ],
    "qweb": [
    ],
    "test": [
    ],
    "images": [
    ],
    "pre_init_hook": False,
    "post_init_hook": False,
    "uninstall_hook": False,
    "auto_install": False,
    "installable": True,
    "application": False,
    "external_dependencies": {
        'python': [],
    },
}
