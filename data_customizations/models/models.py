from odoo import models,fields

class happydays(models.Model):
       #_name = 'happy.project'    #OR NOTHING IS BETTER (less possibilities of mistakes)
       _inherit = 'res.partner'
       # now we add a couple of fields

       know_person = fields.Boolean(string = "Do yo know this person well?")
       meeting_place = fields.Char(string = "Where did you meet?")
       like_person = fields.Boolean(string = "do you like this person?")
       my_lucky_day = fields.Date(string = "Lucky Day")

       # we could  now  show these fields in ANY view that is of model project.project
       # we will see this in the  view inheritance lesson this afternoon, in the meantime we will
       # add them toa view via interface.
       # ADD FIELDS TO INTERFA



