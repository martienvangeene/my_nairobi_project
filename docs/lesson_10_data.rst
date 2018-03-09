

ODOO ORM BASIC
--------------


search & search_count
_____________________
THe ORM  provides a standard search functionality.

https://github.com/OCA/OCB/blob/10.0/odoo/models.py#L1487
https://github.com/OCA/OCB/blob/10.0/odoo/models.py#L1497


both definitions we can see are decorated with @api.model, in order to allow core functionality to be ported to new API, while maintaining compatibility 
Also @model tells us it is not a function where a id of a particular record is passed.


We can use it as so:

Create a domain

domain = [
('name', 'like', 'coding'),
('todo_type.type', '=', urgent)
]

The and operator for simple domains is to be condidered default.
call the domain with search on an empty recordset:

self.env['project.todo'].search(domain)


an will return a recordset of the records that correspond to that domain criteria.




Computed fields
_______________


A computed field is a field the value of wich is determined by some computation.
We set a field as computed by adding the keyword "compute".

So for example in our todo we would like to compute how many characters are in the text:

len_of_todo = fields.Integer('how long is this todo?', compute=_compute_len_todo)

        ACTIVE RECORD MODE
        -------------------

        Recordsets provide an "Active Record" interface: model fields can be read and written directly from the record, 
        but only on singletons (single-record recordsets). Setting a field's value triggers an update to the database.

We will write our compute function keeping this in mind therefore decorating it with @multi and then for saftey iterating the recordset.

If our compute field calculation uses other fields to be calculate we decorate with @depends
This decorator will trigger the call to the decorated function if any of the fields specified in the decorator is altered by ORM or changed in the form.
in are case text_todo is the field we will depend on.

@api.multi
@api.depends('text_todo')
def _compute_len_todo(self):
    for this in self:
        this.len_of_todo = len(this.text_todo)  # in this context will have the same effect as a write

By default it is not stored in the DB.



Inverse function
________________

As the compute is the 'get' feature for a computed field. the 'inverse' keyword is the 'set' function for a computed field. in other words it gives us the logic needed to write to the computed field.

example: we have a computed function to tell us number of urgent jobs(deadline less than 3 days away)


    is_urgent = fields.Boolean(compute=_compute_is_urgent)
             
    def _compute_is_urgent(self):
        for this in self:
            this.is_urgent = True if days_left < 3  else False 






Stored computed fields
_____________________
A stored computed field is never recomputed, the value is kept in the db.
To trigger recomputation it is necessary to decorate the compute function with the decorator
@depends. a Non-stored computed field may be computed every single time it is shown if it has no @dependsconstraints. A non stored computed field has no database permanence and will not be availiable if we do direct queries using the data base cursor.




Related fields
--------------
Reason for related field. Availiability of fields on client side (no dot notation avaiable there)


We add the keyword related to the definition:

 todo_type_importance = fields.Integer(related='todo_type.importance',  readonly=True)




All the field properties ..are in the code!
-------------------------------------------
https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_model.py#L208



Debugging Session
-----------------

Removing the default from the deadline field. We crash, Why?

