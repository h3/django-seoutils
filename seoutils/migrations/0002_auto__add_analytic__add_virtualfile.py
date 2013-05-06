# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Analytic'
        db.create_table('seoutils_analytic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.CharField')(default='Main Analytic', max_length=250, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('seoutils', ['Analytic'])

        # Adding model 'VirtualFile'
        db.create_table('seoutils_virtualfile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('seoutils', ['VirtualFile'])

    def backwards(self, orm):
        # Deleting model 'Analytic'
        db.delete_table('seoutils_analytic')

        # Deleting model 'VirtualFile'
        db.delete_table('seoutils_virtualfile')

    models = {
        'seoutils.analytic': {
            'Meta': {'object_name': 'Analytic'},
            'code': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'Main Analytic'", 'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'seoutils.meta': {
            'Meta': {'object_name': 'Meta'},
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'desc_fr': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'extra_js': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'keywords_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'keywords_fr': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'seoutils.virtualfile': {
            'Meta': {'object_name': 'VirtualFile'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['seoutils']