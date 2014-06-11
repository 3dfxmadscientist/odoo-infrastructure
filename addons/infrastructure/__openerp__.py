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


{   'active': False,
    'author': u'Ingenieria ADHOC',
    'category': u'base.module_category_knowledge_management',
    'demo_xml': [],
    'depends': [u'mail'],
    'description': u'Infrastructure',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Infrastructure',
    'test': [],
    'update_xml': [   u'security/infrastructure_group.xml',
                      u'view/instance_view.xml',
                      u'view/database_view.xml',
                      u'view/environment_step_view.xml',
                      u'view/db_filter_view.xml',
                      u'view/hostname_view.xml',
                      u'view/server_view.xml',
                      u'view/environment_view.xml',
                      u'view/environment_version_view.xml',
                      u'view/partner_view.xml',
                      u'view/change_view.xml',
                      u'view/infrastructure_menuitem.xml',
                      u'data/instance_properties.xml',
                      u'data/database_properties.xml',
                      u'data/environment_step_properties.xml',
                      u'data/db_filter_properties.xml',
                      u'data/hostname_properties.xml',
                      u'data/server_properties.xml',
                      u'data/environment_properties.xml',
                      u'data/environment_version_properties.xml',
                      u'data/partner_properties.xml',
                      u'data/change_properties.xml',
                      u'data/instance_track.xml',
                      u'data/database_track.xml',
                      u'data/environment_step_track.xml',
                      u'data/db_filter_track.xml',
                      u'data/hostname_track.xml',
                      u'data/server_track.xml',
                      u'data/environment_track.xml',
                      u'data/environment_version_track.xml',
                      u'data/partner_track.xml',
                      u'data/change_track.xml',
                      'security/ir.model.access.csv'],
    'version': 'No version',
    'website': ''}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
