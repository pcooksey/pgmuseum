# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SiteName'
        db.create_table(u'datasheet_sitename', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Code', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('site_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'datasheet', ['SiteName'])

        # Adding model 'TreeSpecie'
        db.create_table(u'datasheet_treespecie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('tree_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datasheet', ['TreeSpecie'])

        # Adding model 'FlowerSpecie'
        db.create_table(u'datasheet_flowerspecie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flower_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'datasheet', ['FlowerSpecie'])

        # Adding model 'ExplorationTime'
        db.create_table(u'datasheet_explorationtime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'datasheet', ['ExplorationTime'])

        # Adding model 'CountTime'
        db.create_table(u'datasheet_counttime', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.TimeField')()),
            ('end', self.gf('django.db.models.fields.TimeField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'datasheet', ['CountTime'])

        # Adding model 'Observed'
        db.create_table(u'datasheet_observed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('loners', self.gf('django.db.models.fields.IntegerField')()),
            ('sunners', self.gf('django.db.models.fields.IntegerField')()),
            ('fliers', self.gf('django.db.models.fields.IntegerField')()),
            ('grounders', self.gf('django.db.models.fields.IntegerField')()),
            ('dead', self.gf('django.db.models.fields.IntegerField')()),
            ('mating', self.gf('django.db.models.fields.IntegerField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'datasheet', ['Observed'])

        # Adding model 'Weather'
        db.create_table(u'datasheet_weather', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skypercentage', self.gf('django.db.models.fields.IntegerField')()),
            ('BFT', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
            ('precip', self.gf('django.db.models.fields.CharField')(default='none', max_length=10)),
            ('wind', self.gf('django.db.models.fields.IntegerField')()),
            ('winddirection', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('temp', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'datasheet', ['Weather'])

        # Adding model 'Note'
        db.create_table(u'datasheet_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('waterSource', self.gf('django.db.models.fields.CharField')(default='No', max_length=3)),
            ('waterNotes', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('nectarSource', self.gf('django.db.models.fields.CharField')(default='No', max_length=3)),
            ('nectarNotes', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('additionalNotes', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'datasheet', ['Note'])

        # Adding model 'Basic'
        db.create_table(u'datasheet_basic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('createdBy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('site_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasheet.SiteName'])),
            ('number_of_observers', self.gf('django.db.models.fields.IntegerField')()),
            ('observers', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('exploration_time', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['datasheet.ExplorationTime'], unique=True)),
            ('butterflies_observed', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['datasheet.Observed'], unique=True)),
            ('weather', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['datasheet.Weather'], unique=True)),
            ('count_time', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['datasheet.CountTime'], unique=True)),
            ('notes', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['datasheet.Note'], unique=True)),
        ))
        db.send_create_signal(u'datasheet', ['Basic'])

        # Adding model 'ClusterInfo'
        db.create_table(u'datasheet_clusterinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('basic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasheet.Basic'])),
            ('number_Clustered', self.gf('django.db.models.fields.IntegerField')()),
            ('number_tagged', self.gf('django.db.models.fields.IntegerField')()),
            ('tree_species', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasheet.TreeSpecie'])),
            ('number_of_trees', self.gf('django.db.models.fields.IntegerField')()),
            ('aspect', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'datasheet', ['ClusterInfo'])

        # Adding model 'Flowers'
        db.create_table(u'datasheet_flowers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('basic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasheet.Basic'])),
            ('flower', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['datasheet.FlowerSpecie'])),
            ('eating', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'datasheet', ['Flowers'])


    def backwards(self, orm):
        # Deleting model 'SiteName'
        db.delete_table(u'datasheet_sitename')

        # Deleting model 'TreeSpecie'
        db.delete_table(u'datasheet_treespecie')

        # Deleting model 'FlowerSpecie'
        db.delete_table(u'datasheet_flowerspecie')

        # Deleting model 'ExplorationTime'
        db.delete_table(u'datasheet_explorationtime')

        # Deleting model 'CountTime'
        db.delete_table(u'datasheet_counttime')

        # Deleting model 'Observed'
        db.delete_table(u'datasheet_observed')

        # Deleting model 'Weather'
        db.delete_table(u'datasheet_weather')

        # Deleting model 'Note'
        db.delete_table(u'datasheet_note')

        # Deleting model 'Basic'
        db.delete_table(u'datasheet_basic')

        # Deleting model 'ClusterInfo'
        db.delete_table(u'datasheet_clusterinfo')

        # Deleting model 'Flowers'
        db.delete_table(u'datasheet_flowers')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'datasheet.basic': {
            'Meta': {'object_name': 'Basic'},
            'butterflies_observed': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['datasheet.Observed']", 'unique': 'True'}),
            'count_time': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['datasheet.CountTime']", 'unique': 'True'}),
            'createdBy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'exploration_time': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['datasheet.ExplorationTime']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['datasheet.Note']", 'unique': 'True'}),
            'number_of_observers': ('django.db.models.fields.IntegerField', [], {}),
            'observers': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datasheet.SiteName']"}),
            'weather': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['datasheet.Weather']", 'unique': 'True'})
        },
        u'datasheet.clusterinfo': {
            'Meta': {'object_name': 'ClusterInfo'},
            'aspect': ('django.db.models.fields.IntegerField', [], {}),
            'basic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datasheet.Basic']"}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_Clustered': ('django.db.models.fields.IntegerField', [], {}),
            'number_of_trees': ('django.db.models.fields.IntegerField', [], {}),
            'number_tagged': ('django.db.models.fields.IntegerField', [], {}),
            'tree_species': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datasheet.TreeSpecie']"})
        },
        u'datasheet.counttime': {
            'Meta': {'object_name': 'CountTime'},
            'end': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'total': ('django.db.models.fields.IntegerField', [], {})
        },
        u'datasheet.explorationtime': {
            'Meta': {'object_name': 'ExplorationTime'},
            'end': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.TimeField', [], {}),
            'total': ('django.db.models.fields.IntegerField', [], {})
        },
        u'datasheet.flowers': {
            'Meta': {'object_name': 'Flowers'},
            'basic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datasheet.Basic']"}),
            'eating': ('django.db.models.fields.IntegerField', [], {}),
            'flower': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['datasheet.FlowerSpecie']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'datasheet.flowerspecie': {
            'Meta': {'object_name': 'FlowerSpecie'},
            'flower_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'datasheet.note': {
            'Meta': {'object_name': 'Note'},
            'additionalNotes': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nectarNotes': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'nectarSource': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '3'}),
            'waterNotes': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'waterSource': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '3'})
        },
        u'datasheet.observed': {
            'Meta': {'object_name': 'Observed'},
            'dead': ('django.db.models.fields.IntegerField', [], {}),
            'fliers': ('django.db.models.fields.IntegerField', [], {}),
            'grounders': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loners': ('django.db.models.fields.IntegerField', [], {}),
            'mating': ('django.db.models.fields.IntegerField', [], {}),
            'sunners': ('django.db.models.fields.IntegerField', [], {}),
            'total': ('django.db.models.fields.IntegerField', [], {})
        },
        u'datasheet.sitename': {
            'Code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'Meta': {'object_name': 'SiteName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'datasheet.treespecie': {
            'Code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'Meta': {'object_name': 'TreeSpecie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tree_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'datasheet.weather': {
            'BFT': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'Meta': {'object_name': 'Weather'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precip': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '10'}),
            'skypercentage': ('django.db.models.fields.IntegerField', [], {}),
            'temp': ('django.db.models.fields.IntegerField', [], {}),
            'wind': ('django.db.models.fields.IntegerField', [], {}),
            'winddirection': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['datasheet']