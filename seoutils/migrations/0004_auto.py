# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing index on 'Meta', fields ['path_info']
        db.delete_index('seoutils_meta', ['path_info'])

    def backwards(self, orm):
        # Adding index on 'Meta', fields ['path_info']
        db.create_index('seoutils_meta', ['path_info'])

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