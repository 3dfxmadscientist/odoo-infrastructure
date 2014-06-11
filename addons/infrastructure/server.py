# -*- coding: utf-8 -*-
##############################################################################
#
#    Infrastructure
#    Copyright (C) 2014 Ingenieria ADHOC
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import re
from openerp import netsvc
from openerp.osv import osv, fields

class server(osv.osv):
    """"""
    
    _name = 'infrastructure.server'
    _description = 'server'
    _inherits = {  }
    _inherit = [ 'mail.thread','ir.needaction_mixin' ]

    _track = {
    }
    _columns = {
        'name': fields.char(string='Name', required=True),
        'ip_address': fields.char(string='IP Address', required=True),
        'ssh_port': fields.char(string='SSH Port', required=True),
        'main_hostname': fields.char(string='Main Hostname', required=True),
        'user_name': fields.char(string='User Name', required=True),
        'password': fields.char(string='Password', required=True),
        'holder_id': fields.many2one('res.partner', string='Holder', required=True),
        'owner_id': fields.many2one('res.partner', string='Owner', required=True),
        'user_id': fields.many2one('res.partner', string='user_id', required=True),
        'software_data': fields.html(string='Software Data'),
        'hardware_data': fields.html(string='Hardware Data'),
        'contract_data': fields.html(string='Contract Data'),
        'note': fields.html(string='Note'),
        'hostname_ids': fields.one2many('infrastructure.hostname', 'server_id', string='Hostnames'), 
        'change_ids': fields.one2many('infrastructure.change', 'server_id', string='Changes'), 
        'environment_ids': fields.one2many('infrastructure.environment', 'server_id', string='Environments', context={'from_server':True}), 
    }

    _defaults = {
    }


    _constraints = [
    ]




server()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
