# -*- coding: utf-8 -*-
"""

"main concept of MongoDB is embed whenever possible"
Ref: http://stackoverflow.com/questions/4655610#comment5129510_4656431
"""
from __future__ import absolute_import, unicode_literals
from datetime import datetime

from mongoengine import (DateTimeField, Document, EmailField, ListField,
                         ReferenceField, StringField)


class Institute(Document):
  """Represents an institute linked to multiple collaborating users."""
  internal_id = StringField(primary_key=True, required=True)
  display_name = StringField(required=True)
  sanger_recipients = ListField(EmailField())
  cases = ListField(ReferenceField('Case'))
  created_at = DateTimeField(default=datetime.now)

  def count_cases(self):
    """Return the number of cases linked to the institute."""
    return len(self.cases)

  def __unicode__(self):
    return self.display_name
  
  def __repr__(self):
    return "Institute(internal_id={0}, display_name={1}, "\
           "sanger_recipients={2}, cases={3}, created_at={4})".format(
             self.internal_id, self.display_name, self.sanger_recipients,
             self.cases, self.created_at
             )
