# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SignUp'
        db.create_table('signups_signup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('for_you', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('signups', ['SignUp'])


    def backwards(self, orm):
        # Deleting model 'SignUp'
        db.delete_table('signups_signup')


    models = {
        'signups.signup': {
            'Meta': {'object_name': 'SignUp'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True', 'null': 'True'}),
            'for_you': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True', 'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['signups']