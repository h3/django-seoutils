# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Meta'
        try:
            db.create_table('seoutils_meta', (
                ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('path_info', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
                ('title', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
                ('title_en', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
                ('title_fr', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
                ('keywords', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
                ('keywords_en', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
                ('keywords_fr', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
                ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
                ('desc_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
                ('desc_fr', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
                ('extra_js', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ))
            db.send_create_signal('seoutils', ['Meta'])
        except:
            pass

    def backwards(self, orm):
        # Deleting model 'Meta'
        db.delete_table('seoutils_meta')

    models = {
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
        }
    }

    complete_apps = ['seoutils']
