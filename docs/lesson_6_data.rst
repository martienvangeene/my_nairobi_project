
        Module  - Module structure basic 2
        ==================================


        Intro
        -----

          In this lesson we will learn how to add hardcoded data to our module. Data we can rely on in our program, use
          and refer to in our code. 

          There are many reasons one might want this: Eg. hardcoded Accounting charts, Hardcoded Categories or Hardcoded website charateristics.

          Data can also be used to modify existing data from previous models of wich we know the existence.


        Data files XML - records - XMLID/ExternalID
        -------------------------------------------

          The " data " structure in odoo, in canonical module structure is placed in the /data directory. Not because it is significantly 
          different from other XML records we have previously discussed but to logically order them and distinguish them from views and templates.

          Data XML's must be included in the manifest under the 'data' key.

          The XMLID is an unique unifier for a record in a database. It is assigned and managed by the Odoo framework and accessible to the programmer by knowing simple rules about it's nomenclature.
          An id is a record of model ir.model.data

          https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_model.py#L982


          An XML_ID follows the momenclature  {ModuleName}.{RecordName} and can be declared both with it's complete name ( like sale.myview) or incomplete name
          a myview record


          A data record is declared as so in our /data file

          <record id="project_todo.mydata" model="todo">
               
          <record>

          or:

          <record id="mydata" model="somemodel">

          <record>

          *in the project_todo module*

          As you can see: the unique and fully qualifying  XMLID of this record is  "project_todo.mydata" , and is aoutocompleted here if not completely given:

          https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_model.py#L1009

          Also note that we have given the ID and the model in this record, wich are the only  
          required fields in the model.

          noupdate = fields.Boolean(string='Non Updatable', default=False)
          model = fields.Char(string='Model Name', required=True)

          also 'module' is required. But the module as we said before is inferred by the placement of the record itself.
          If it is in sale we know it wil be sale.XXXXX , if it is in project_todo we know it will be called project_todo.xxxxx


          As you can see the odoo Framework is used internally to implement parsers, interpreters and models for supporting data structures.

         
          Data records can be used to modify or create ir.model.data records.
          If the full XML_ID exists the definition modifies the existing record. If it does not exist it creates a new record.

          For example, if in our project_todo we create a record:


          ::

                <record id = "project.mt_task_new" model="mail.message.subtype">
                        <field name="name">Task Opened!</field>
                </record>

          ::


                we are modifying :

                 https://github.com/OCA/OCB/blob/10.0/addons/project/data/project_data.xml#L39

                and changing it's name from Task Opened to Task Opened!

                In this case we must be sure that project_todo depends on 'project'

                but if we write in our module :
                ::

                <record id = "mt_task_new" model="mail.message.subtype">
                        <field name="name">Task Opened!</field>
                </record>

                ::

                We are creating a new record with unique XML ID "project_todo.mt_task_new" and it will generate an error , because not all required fields of the model
                "mail.message.subtype" are defined and it will be impossible to create a new record.



                  THe order with wich the XML IDS are evaluated is decided by the module inheritance tree. So if you are modifying an existing Data record or if you 
                  refer to an existing data record, make sure your module depends on the module that conains the definition of the data record you change/refer to.

                  In this way you are sure the data you need is already loaded when you start creating yours.

                  Wrong inheritance definition is a common source of bugs.


        self.env.ref()
        --------------
                Our enviroment variable, wich is a property of any model can call and resolve an XMLID, in order to fetch back the information it contains, by using the function ref().

                self.env.ref('Full XML ID ') will return the record (allways unique!!!!) of that particular XMLID.

                SO for example  if i define:

                ::

                <record id ="todo_data" model="todo">
                        <field name="name">Task Opened!</field>
                </record>

                ::



                self.env.ref('project_todo.todo_data') will return a record of the todo model , fully accessible.
               

        menuitem  act_windows and domains
        ---------------------------------


                Records are the basis of data insertion in odoo, everyhing is a record, views, menues, "data", actions , and odoo interprets them according to their specified nature.

                menuitem tag: creates menu items   ---->  its just a shortcut for creating a record of model ir.ui.menu ! 
                        https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_ui_menu.py#L18

                act_window: creates window actions  ----> its just a shortcut for creating a record of model ir.actions.act_window !
                        https://github.com/OCA/OCB/blob/10.0/odoo/addons/base/ir/ir_actions.py#L237
                                 
                        (note here how the table of this model is specifically imposed, remember this when navigating the database)

                To have a grasp of these convenience shortcuts , here is where they are "converted" by odoo core (ORM).

                        https://github.com/OCA/OCB/blob/10.0/odoo/tools/convert.py#L200

                        and , menuitem:
                        
                        https://github.com/OCA/OCB/blob/10.0/odoo/tools/convert.py#L494

                * knowing these internals is important, because every "convenience"  method/tag/function , while making our lives easier for rapid development is a level
                  of abstraction that obfucates comprehension in case something goes wrong. *
                (personally i would prefer to tag everything as a record, it is coherent and mantains tighter connection to the data, but it is not commony done)


                Now let's add to our module a menu for opening an action that opens a tree view for out 'todo' model.

                Normally menuitems and actions are not contained in the /data folder but in the /views folder together with formviews, 
                on the other hand, when we will study  wizards, which  is a special type of model (transient model) , we will see them contained in the /wizard folder.
                Logically it makes no difference , it's about code readability.
                                
                        Internal view priorities.
                        ------------------------

                        *other than module dependency, which gives us the order in which the XML files are loaded, the order they are placed in the manifest and the order they are declared in the single
                        XML files are also important*


                Add Menu item:

                <menuitem id="todo_menu"
                parent="project.menu_main_pm"                                       <!--we know we have it because we inherited project-->
                name="My TODO">



                        (GO back to link and for ir.ui.menu and checkout the model's fields.)


           noupdate modifier
           -----------------
            If the data should never be changed by the user. we can add to our <odoo> tag <odoo nopudate="1">
            the default is noupdate=0, most data is intended to be modified after module install.


           
         
           Security groups
           ---------------

           In later lessons we will study the ODOO ACL ( Access control Layer) and will learn the various checks odoo uses to control access to models on  various levels.
           As everything in odoo , even access groups are  .....records!

           here we are modifying the record base.user_demo  of model res.users to have a new access group.

           https://github.com/OCA/OCB/blob/10.0/addons/project/data/project_demo.xml#L6

           we can assign groups to menuitem 


         Demo Data
         ---------
         Demo Data is the same of normal data, it is in the manifest under the key "demo" not "data", this means it will be loaded only if we have demo data enabled.


         Some Common errors
         ------------------
        
         3 levels of precedence in data :
                Module, Manifest and File order (in this hierarchy of importance)

         bad cases:

         1. Move action to invalidate File order hierarchy
         2. Remove dependency to invalidate Module hierarchy
         3. Duplicate XMLID of two views to invalidate XMLID uniqueness.


         Reflections/thoughts
         --------------------
         A) We have this giant hierarchy of records we can modify (given we have respected the 3 rules of precedence in odoo data). What are the possible pittfals? what procedures would you follow not to have incompatibilities between "DATA" and "LOGIC". think about a couple of places where a record overwrite can break code and be hard to debug.

         B) Using the  MVC (model view controller) paradigm , where do the things we saw today fit in? can they sqarely be fit in? or is it a little blurred?

         EXERCISES
         ---------


          EXERCISE 1
                Create a set of 10 TODO objects with content , connected to the user defined in:
                https://github.com/OCA/OCB/blob/10.0/addons/project/data/project_demo.xml#L6
                (identify XML ID and access it)

          EXERCISE 2 
                create via module data a set of 2 todo Types  "work todos"  "house todo"  

          EXERCISE 3
                Change some of the new todo objects and give them one of the types you just made.

          EXERCISE 4  
                Read and comprehend the code linked in this lesson.

