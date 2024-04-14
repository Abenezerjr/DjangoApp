""""
A **Django QuerySet** is a powerful tool that allows you to interact with your database in a Pythonic way. Let's dive into the details:

1. **Creating Objects**:
    - To represent database-table data in Python objects, Django uses an intuitive system:
        - A **model class** represents a database table.
        - An instance of that class represents a particular record in the database table.
    - To create an object:
        - Instantiate it using keyword arguments to the model class.
        - Call `save()` to save it to the database.
    - Example:
        ```python
        from blog.models import Blog
        b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
        b.save()
        ```
        This performs an **INSERT SQL statement** behind the scenes.

2. **Saving Changes to Objects**:
    - To save changes to an existing object in the database:
        - Use `save()`.
        - Example:
            ```python
            b5 = Blog.objects.get(pk=5)
            b5.name = "New name"
            b5.save()
            ```
        - This performs an **UPDATE SQL statement**.

3. **Foreign Key and Many-to-Many Fields**:
    - Updating a **ForeignKey** field:
        - Assign an object of the right type to the field.
        - Example:
            ```python
            entry = Entry.objects.get(pk=1)
            cheese_blog = Blog.objects.get(name="Cheddar Talk")
            entry.blog = cheese_blog
            entry.save()
            ```
    - **ManyToManyField** fields work similarly.

Remember, a **QuerySet** represents a collection of objects from your database, and filters allow you to narrow down query results based on parameters. It's like a SELECT statement in SQL, and filters act as limiting clauses (e.g., WHERE or LIMIT)

(3) Django QuerySet - W3Schools. https://www.w3schools.com/django/django_queryset.php.
(4) Django ORM and QuerySets Tutorial - Learn Django. https://learndjango.com/tutorials/django-querysets-tutorial.

 in django model if you went to reterive data in the databese in this form

 queryset=ModelName.objects.all()
                            .get() # get single object
                            .filter()
                            .exclude()


 queryset='Variable that hold the response'
 ModelName="Modelname or database name"
 objects="Modle Objects attribute"
 all()='Method'


...

#Be sure to import a model first before making queries

from models import Model Name

#all() Retrieves all objects from table

queryset ModelName.objects.all()

#get(attribute 'value') Retrieve a single object based on matched attribute

queryItem ModelName.objects.get(attribute='value')

filter(attribute='value') Returns all items from table that match a particular attribute value

# queryset ModelName.object.filter(attribute='value')

.filter(attribute_startswith='value')

.filter(attribute contains='value')

.filter(attribute_icontains='value')

.filter(attribute_gt='value')

.filter(attribute_gte='value')

.filter(attribute_lt='value')

.filter(attribute_lte='value')

exclude(attribute='value') Excludes any object matching a particular filter

# queryset ModelName.object.exclude(attribute='value')

sorder by() Order a queryset by a particular attribute, Multiple parameters are allowed queryset Project.object.filter(title="first project").order_by('value1', 'value2')

#order can be reversed by adding before the attribute naine

queryset Project.object.filter(title="first project").order_by('-value', '-value2')

#create() Create an instance of a model

item ModelName.objects.create(attribute='value')

#save()- Save changes made to a particular object item ModelName.objects.get(attribute='value')

item.title = "New Value"

item.save()

#delete() Deletes a particular object

item.delete()

item = Model Name.objects.last()

#Query Models Children

item ModelName.object.first()

item.childmodel_set.all()

#Query Many ToMany Fields

item ModelName.object.first()

item.relationshipname.all()

#Add Many ToMany Field

item ModelName.object.first()

item.relationshipname.add(otheritem)

otheritem OtherModule.objects.create(attribute='value')
"""""


