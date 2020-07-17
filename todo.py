from traits.api import HasTraits, Str, List
from traitsui.api import View, Item, CheckListEditor

my_to_list = ['clean car', 'create youtube video', 'feed animals']

class ToDo(HasTraits):

    todo_list = List(Str())
    completed = List(Str())

    my_view = View(
        Item('completed', style='custom', editor=CheckListEditor(name='todo_list')),
        Item('completed', style='readonly')
    )

my_todo = ToDo(todo_list=my_to_list)

my_todo.configure_traits()