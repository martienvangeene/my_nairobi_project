intro
-----

In this lesson we will see some "magic" elements provided by odoo views. Obviously magic does not exist in Opensource, and we will see how and why they work and how to modify them.

We will also  see how to add buttons connected to fuctions or actions in odoo.

The second  part will be a concise expalantion of decorators and some of the decorators provided by odoo since version 8, in particular connected to ORM data managment and retro compatibility with previous versions of odoo.




Buttons and Functions
---------------------
Adding a button in a view is doneby using the tag "button".
Buttons may be of two types: Action (calls an Action) or "object" (calls a function)


<button type="action"
name="%(FULLXMLIDFORTHEACTION)d"
string="Open a new view" />

<button type="object"
name="do_todo"
string="Done" />

The More Button - demistifying magic box coding -we read the code
-----------------------------------------------------------------
All the data visualizations we have seen up to now work on a form or tree or menu.
Everything outside that scope are not reachable by they type of records we have been creating,
because the odoo ORM does not allow for "out of the lines" interpretation on views: (e.g. change something in the top bar)

of course this is possible let's review the structure of how odoo


   |Views - MENUES| ------- | ODOO ORM - VIEW PARSER| ----- | JAVASCRIPT "Backend" renderer


THe more button is one of such places where odoo allows us to add commands, and it is a standard feature in odoo. We will find automatically (injected by ORM) server actions related to the model of the current view.

here are the shortcuts the client understands

key2 = client_action_multi   (our action will end up in more...)
key2 = clinet_print_multi   (will end up in print ......)

there is an automatic addition HERE:

https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_actions.py#762




SERVER ACTIONS
--------------


A server action is a model that odoo uses to achieve automation. WHe can describe actions to perform on a certain model if certain conditions are met.

https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_actions.py#L417
class IrActionsServer(models.Model)

As we can see a bare documentation is often included in the source code. Explaining the potential of server actions.

Server actions can call actions, functions, writes, or multiple actions. But the most powerful activity is to associate to a server action random python code.

This code runs in a limited enviroment , described here:
https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_actions.py#L446

Server actions work on  a specific model. in our case project.todo

        <record id="todo_dosomething" model="ir.actions.server">
           <field name="name">Do something with my todo(s)</field>  
            <field name="model_id" ref="model_project_todo"/>  <--- it's done on this model
            <field name="condition">True</field>
            <field name="type">ir.actions.server</field>      
            <field name="state">code</field>                   <--- we use python code
           <field name="code">record.server_action_was_here()</field>   <---we access record (see docs)
         </record>



We can create server actions via interface (configuration --> Technical --> Actions --> server actions).
But this interface form , as we have seen is just creating a ir.actions.server record.










Going out of the "lines" of the ORM renderer 
--------------------------------------------
In our last lessons we will see how to change the JS backend of odoo in order to have complete freedom to do whatever we want in the interface.
for example by extending javascript elements like "ControlPanel" or "ViewManager" and adding / removing things that  we want.
This type of modifications is less user friendly, but often needed and , thanks to opensource , there are many examples of this being done in the /WEB repository of the OCA.






Decorators in Python
--------------------
Consider these statements:

        A function is a object like everything else in python
        A function can return a function object.
        A function can take a function as an argument.

Let those statements settle. (10 seconds of silence).

A decorator is a python function that wraps another function, in other words, it takes a function in imput, does something to it and spits out another function.


Explictly there it is:

def  i_decorate(function):
    def wrap_this(myString):
        return mystring + 'i\'m decorated'
    return wrap_this

this function "i_decorate" takes a function that has 1 argument "mystring" and makes that function do whatever it does , but it changes mystring to something cooler.

this decorator is good only for functions that have one non keyword argument , but i can make a universal decorator by using star-args and star-star-kwargs ! depending on what i want to do.

Tis is a very powerful way to modularize and reuse code.

So I have a function:

def giovannis_function(my_name):
    return 'I have a name, its %' % my_name


I can decorate it 

i_decorate(giovannis_function('gio'))

and get as a result:

'I have a name, its gio , i'm decorated'


The decorator syntax is just short cut for this
if i write:

@i_decorate
def giovannis_function(my_name):
    return 'I have a name, its %' % my_name



everytime i call giovanni's function , it's going to be decorated!


Decorators in Odoo
------------------
Odoo offers a vas amount of decorators.


Most are made to help backwards compatibility between v8 and previous.
Some are very powerful tools.

examples:

@api.constraints
@api.onchange    (difference between v7 onchange and v8 onchange)

Add onchange to views from decorator
addons/base/ir/ir_ui_view.py#L810


A decorator definition, naturally in api
https://github.com/OCA/OCB/blob/10.0/odoo/api.py#L170

this decorator takes any amount of non keyword arguments.




@api.model
----------
Api model is used when This decorator will convert old API calls to decorated function to new API signature. It allows to be polite when migrating code.


OLD SIGNATURE v7 and below:

        def(self, cr, uid, id, ( other arguments)  , context)


New SIgnature

        cr, uid, id, and context are all implicit in the enviroment and allways passed, allowing for cleaner code!


But how to make them coexist?

A decorator is the solution


we use @api.model when the function did not have an ID and the currentID is unimportant for the code.
(like a create function)



@api.multi - "for this in self"
--------------------------------
Api multi  means This decorator loops automatically on Records of RecordSet for you. Self is redefined as current record.

so we will be receiving a recordset.
We must ensure we are not breaking code, by , if necessary looping explictly the recordset in our code.



ensure_one()
------------

utility provided by framework will raise error if recordset is of cardinality not 1.




EXERCISE 1 : have a function to confirm the todo list item from state todo to state done

EXERCISE 2 : reverse , from state done to state draft

EXERCISE 3 : write a function that will send a recordset of 2 elements to a function that uses ensure_one and trigger it.





