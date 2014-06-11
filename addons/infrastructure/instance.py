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

class instance(osv.osv):
    """"""
    
    _name = 'infrastructure.instance'
    _description = 'instance'

    _columns = {
        'name': fields.char(string='Name', required=True),
        'instance_type': fields.selection([(u'secure', u'Secure'), (u'none_secure', u'None Secure')], string='Instance Type', required=True),
        'xml_rpc_port': fields.integer(string='xml rpc Port', required=True),
        'xml_rpcs_port': fields.integer(string='xml rpcs Port'),
        'longpolling_port': fields.integer(string='Longpolling Port'),
        'db_filter': fields.many2one('infrastructure.db_filter', string='Db filter', required=True),
        'user': fields.char(string='User', readonly=True),
        'environment_id': fields.many2one('infrastructure.environment', string='Environment', ondelete='cascade', required=True), 
        'database_ids': fields.one2many('infrastructure.database', 'instance_id', string='Databases', context={'from_instance':True}), 
    }

    _defaults = {
    }


    _constraints = [
    ]


    def get_user(self, cr, uid, ids, context=None):
        """"""
        raise NotImplementedError



instance()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
